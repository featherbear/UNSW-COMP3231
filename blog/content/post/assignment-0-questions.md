---
title: "Assignment 0 Questions"
date: 2020-02-19T23:08:53+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

**Question 1**: What is the vm system called that is configured for assignment 0?  
**Answer**: dumbvm (kern/arch/mips/conf.arch)

**Question 2. Which register number is used for the stack pointer (sp) in OS/161?**  
**Answer**: Register 29 (kern/arch/mips/include/kern/regdefs.h)

Additional::
* a0 contains the address of the switchframe pointer in the old thread.
* a1 contains the address of the switchframe pointer in the new thread.
* The switchframe pointer is really the stack pointer. 

**Question 3. What bus/busses does OS/161 support?**  
**Answer**: LAMEbus (kern/arch/sys161/include/bus.h)

**Question 4. Why do we use typedefs like uint32_t instead of simply saying "int"?**  
**Answer**: To enforce the size of their types, as lengths can be platform dependent. Also enforces the unsigned component (Larger positive number space)

**Question 5. What function is called when user-level code generates a fatal fault?**  
**Answer**: `static void kill_curthread(vaddr_t epc, unsigned code, vaddr_t vaddr)` (kern/arch/mips/locore/trap.c)

**Question 6. How frequently are hardclock interrupts generated?**  
**Answer**: 100 times a second (kern/include/clock.h)

**Question 7. How many characters are allowed in an SFS volume name? **  
**Answer**: 32, inc null terminator (kern/include/kern/sfs.h)


