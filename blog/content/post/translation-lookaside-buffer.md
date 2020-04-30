---
title: "TLB - Translation Lookaside Buffer"
date: 2020-04-30T18:32:48+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams:
  enable: false
  options: ""
---

The TLB is a _hardware cache_ of the page table entries.  
In the os/161 system, the TLB can cache 64 entries.

When a virtual memory location is requested, the TLB cache is accessed.

If the memory location exists and is valid within the TLB cache, the physical memory address is returned.  
If the virtual address is not valid within the TLB cache, a **TLB Miss** occurs.

When a TLB Miss occurs, depending on the device - the software or hardware may be responsible for refilling the TLB.

- Hardware Loaded TLB (i.e. Pentium) - TLB managed by hardware - On TLB miss, the hardware performs the pagetable lookup and refill
- Software Loaded TLB (i.e. MIPS) - On TLB miss, the hardware generates a TLB exception. The software exception handler performs a look up and refills the TLB

# Amdahl's Law

> "The improvement of overall performance is limited by the fraction of time an enhancement can be used"

TL;DR 1 - A program with optimised code is only better if that optimised code is actually used.  
TL;DR 2 - Check for the common cases first, so that the CPU will execute the priority parts first.

# R300 Implementation

As TLB Misses are expected to be frequent, the CPU is optimised to handle these events.

There is an exception vector in `0x80000000`

- `TLB Refill` - A fast routine to populate the TLB with the right mapping entry
- `TLB Mod` - TLB Modification Exception - Writing to a read-only page
- `TLB Load` - Loading from a page that is invalid (i.e. doesn't exist)
- `TLB Store` - Storing to a page that is invalid

## c0 Registers

- `c0_EPC` - Exception return address
- `c0_status` - Kernel/User mode? Interrupt control flags
- `c0_cause` - What caused the exception
- `c0_badvaddr` - THe address that caused the exception

## TLB Entries

![](Screenshot from 2020-04-30 18-52-20.png)

Each TLB entry is 8 bytes (64 bits) long, and is a pair of `EntryHi:EntryLo` registers positioned with an index.

The `EntryHi` register contains the **page number** and **address space ID**.  
The `EntryLo` register contains the **frame number** and **permission bits**

### MIPS Instructions

- `tlbr` - TLB Read - Retrieve by Index
- `tlbp` - TLB Probe - Lookup by Page Number
- `tlbwr` - TLB Write Random - Write to a random Index
- `tlbwi` - TLB Write Index - Write by Index
