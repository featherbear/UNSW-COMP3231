---
title: "Assignment 3"
date: 2020-04-15T16:48:20+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Diagram

![](sketch.png)


---

> In this assignment you will implement the virtual memory sub-system of OS/161. The existing VM implementation in OS/161, dumbvm, is a minimal implementation with a number of shortcomings. In this assignment you will adapt OS/161 to take full advantage of the simulated hardware by implementing management of the MIPS software-managed Translation Lookaside Buffer (TLB). You will write the code to manage this TLB.


# The System/161 TLB

In the System/161 machine, each TLB entry includes a 20-bit virtual page number and a 20-bit physical page number as well as the following five fields:

* <s>`global`: 1 bit; if set, ignore the PID bits in the TLB.</s>
* `valid`: 1 bit; set if the TLB entry contains a valid translation.
* `dirty`: 1 bit; enables writing to the page referenced by the entry; if this bit is 0, the page is only accessible for reading.
* <s>`nocache`: 1 bit; unused in System/161. In a real processor, indicates that the hardware cache will be disabled when accessing this page.</s>
* <s>`asid`: 6 bits; a context or address space ID that can be used to allow entries to remain in the TLB after a context switch.</s>

***NOTE: Crossed out ones are not needed in os161.***

All these bits/values are maintained by the operating system (i.e. your code). When the valid bit is set, the TLB entry contains a valid translation. This implies that the virtual page is present in physical memory. A TLB miss occurs when no TLB entry can be found with a matching virtual page and address space ID (unless the global bit is set in which case the address space ID is ignored) and a valid bit that is set.

For this assignment, you may largely ignore the ASID field set to zero for your TLB entries. Note, however, that you must then flush the TLB on a context switch.  
**Why: The ASID field corresponds TLB entries to the correct process. Without ASID field, we need to force all TLB entries to be invalid - so that a new process can not match a TLB entry that existed before its context switch.**

# TLB Access Procedure

(1) Check if entry is VALID  
(2) Check if GLOBAL  
[3] [if not global] Check ASID  (not needed in os161 if a TLB flush is performed)
(4) Set DIRTY  

# Memory Regions

* `kseg2` - TLB-mapped cacheable kernel space - `0xc0000000` to `0xffffffff`
* `kseg1` - direct-mapped uncached kernel space - `0xa0000000` to `0xbfffffff`
* `kseg0` - direct-mapped cached kernel space - `0x80000000` to `0x9fffffff`
* `kuseg` - TLB-mapped cacheable user space - `0x00000000` to `0x7fffffff`

# Address Space Management

OS/161 has an address space data type that encapsulates the book-keeping needed to describe an address space: `struct addrspace`.  
To enable OS/161 to interact with your VM implementation, you will need to implement the functions in `kern/vm/addrspace.c` and potentially modify the data type. The semantics of these functions is documented in `kern/include/addrspace.h`.

_Note: You may use a fixed-size stack region (say 16 pages) for each process._

# Address Translation

The main goal for this assignment is to provide virtual memory translation for user programs.  
To do this, you will need to implement a ***TLB refill handler***. You will also need to implement a ***page table***.  
For this assignment, you will implement a 2-level hierarchical page table.

> [Udacity - Two Level Page Tables](https://www.youtube.com/watch?v=8kBPRrHOTwg)  
Split the MSB into two segments. First MSB indexes to a second table, second MSB indexes to the correct frame  
[MIT Notes](https://people.csail.mit.edu/rinard/teaching/osnotes/h11.html)

Note that a hierarchical page table is a lazy data-structure.  
This means that the contents of the page table, including the second-level nodes in the hierarchy, are only allocated when they are needed.  

You may find allocating the required pages at load time helps you start your assignment, however, ***your final solution should allocate pages only when a page-fault occurs***.

* What information do you need to store for each page?
* How does the page table get populated?

Note: Applications expect pages to contain zeros when first used.  
This implies that newly allocated frames that are used to back pages should be ***zero-filled prior to mapping***

# Hints

To implement a page table, have a close look at the `dumbvm` implementation, especially `vm_fault()`.  
Although it is simple, you should get an idea on how to approach the rest of the assignment.

One approach to implementing the assignment is in the following order:

* Understand how the page table works, and its relationship with the TLB.
* Understand the specification and the supplied code.
* Work out a basic design for your page table implementation.
* Modify `kern/vm/vm.c` to insert, lookup, and update page table entries, and keep the TLB consistent with the page table.
* Implement the TLB exception handlers in vm.c using your page table.
* Implement the functions in `kern/vm/addrspace.c` that are required for basic functionality (e.g. `as_create()`, `as_prepare_load()`, etc.). Allocating user pages in `as_define_region()` may also simplify your assignment, however good solution allocate pages in `vm_fault()`.
* Test and debug this. Use the debugger!

Note: Interrupts should be disabled when writing to the TLB, see `dumbvm` for an example.  
Otherwise, unexpected concurrency issues can occur.

`as_activate()` and `as_deactivate()` can be copied from dumbvm.

# Linux File Permission to Page Table Bits

| Linux | Page Table |
|:-----:|:----------:|
|rwx|DV|
|rw-|DV|
|r-x|-V|
|r--|-V|
|-wx|DV|
|-w-|DV|
|--x|-V|
|---|--|

# TLB Data

Look at the MIPS R300 manual page: 6-3.

Two 4-byte registers represent a TLB entry...  
EntryHi:EntryLo

* EntryHi: 20 bits - VPN, 6 bits - ASID (ignore for OS161), 6 bits - 000000
* EntryLo: 20 bits - PFN, 1 bit - Non-Cacheable (ignore for OS161), 1 bit - Dirty, 1 bit - Valid, 1 bit - Global

* Can keep ASID as 0

* tlb_probe to check if it is valid / exists

* Always use `tlb_random` - we are not assessed on any efficient TLB algorithm.

# struct addrspace

`struct addrspace` contains our two level page table (add a pointer)

* `as_prepare_load` -> load with vop_write; force writable (ie writing)
* `as_complete_load` -> reset read write permissions

# Clearing the TLB

* Disable interrupts - `int spl = splhigh()`
* Write invalid entries into the TLB - `tlb_write(TLBHI_INVALID(i), TLBLO_INVALID(), i)`
* Enable interrupts - `splx(spl)`

Clear the TLB in as_activate() and as_deactivate()

# Memory Mapping

* kseg2 - 1GB
* kseg1 - 512MB non-cacheable
* kseg0 - 512MB cacheable
* useg - 2GB

* Start stack address at USERSTACK

# vm_fault

* Check if fault address is null
  * Return `EFAULT` if address is null
* Check fault type
  * Return `EFAULT` if fault type is read only
  * Return `EINVAL` if fault type is not read nor write
* Check page table
  * If page entry doesn't exist, then allocate a new frame (`KVADDR_TO_PADDR(alloc_kpages(1))`)
* Check the access flags for the matched memory region in the address space
* Store the value into the TLB (`tlb_random(entryHi, entryLo)`)
  * Write fault address into the 10 MSB of entryHi
  * Write physical address into the 10 MSB of entryLo
  * Write Dirty and Valid bits into entryLo according to [this table](#linux-file-permission-to-page-table-bits)
