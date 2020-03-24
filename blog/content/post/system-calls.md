---
title: "System Calls"
date: 2020-03-05T12:09:11+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

**System calls** are special function calls to access kernel functionality in a controlled and managed way.

They allow the processor to enter kernel mode and exit back into user mode without the user needing to explicitly implement that functionality. They also prevent access of secure locations

# Fetch-Execute Cycle

* Fetch
* Set PC (_??? before or after ???_)
* Execute

---

# x86 - Privileged-only Instructions

* `cli` - clear interrupt (disable interrupts)
* `sti` - set interrupt (enable interrupts)

**Only executes in kernel mode.**

---

Divide the memory into a kernel-only region, and a shared region.

--

# Steps to make a System Call

* Push arguments to the stack
* Set up relevant registers
* Execute syscall call
* Kernel Trap!!!
  * _We are now in Kernel Space (the OS)_
* Dispatcher checks trapframe
* Do whatever needs to be done for the syscall
* Return to caller
* Increment SP

# User -> Privileged Mode change

* Processor mode switch
* Stack pointer switch
* Program counter switch
* Registers used to pass data to and from kernel.
* Memory used to pass data to and from kernel.

--- 

# MIPS R3000

Has a co-processor (CP0) that manages the state of the main processor.

* `c0_cause` register - cause of the most recent exception
* `c0_status` register - current status of the CPU
* `c0_epc` register - address of the instruction that triggered an exception

Accessing CP0 is done through the two kernel mode instructions `mtc0` (move to c0), and `mfc0` (move from c0).

## Important Bits

### c0_status

![](Screenshot from 2020-03-24 19-28-19.png)

<!-- The last 16 LSBs:

* IM - 8 bits - Interrupt Mask (6 external, 2 software)
* _-- placeholder --_ - 2 bits - set to `00`
* Then for **o**ld, **p**revious, **c**urrent
  * KU - 1 bit - Kernel or User bit
  * IE - 1 bit - Interrupt enabler -->

### c0_cause

![](Screenshot from 2020-03-24 19-28-27.png)

* **Important Exception Codes**
  * `0` - Interrupt
  * `8` - Syscall

* General Exception Vector is at `0x8000 0800`

## Returning from an Exception

* Set the PC to the value of the EPC (using the `jr` instruction)
* Return from the exception (using the `rfe` instruction)

# OS/161 System Calls

Arguments are passed and returned via normal C function calling convention.

Register `v0` contains the system call number

* When a syscall returns successfully:
  * Register `a3 = 0` on success
* Register `a3` is non-zero if a failure has occurred
  * `v0` contains the error number
  * `v0` is then stored in `errno`
  * `v0` set to `-1`
  

// TODO: Slides