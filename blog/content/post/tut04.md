---
title: "Tutorial Week 4"
date: 2020-03-09T16:08:56+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# What does the branch delay slot do?

Allows the processor to execute a command while the branch jump instruction is armed to execute.  

# What register is the return result usually placed in?

`v0`

# Conventions for function arguments

The first 4 arguments are `a0`, `a1`, `a2`, `a3`.  
For additional arguments, we need to use the values on the stack.  

For example:
```asm
addu a0, a0, a1
addu a2, a0, a2
addu a3, a2, a3
lw v0, 16(sp)   ; Load the 2-byte word at sp+16
nop
```

# Stacks

Stacks start at the MAX memory (0xFFFFFFFF), and grow by reaching memory addresses closer to 0x00000000.

Therefore to 'grow' the stack, we would subtract values from the stack pointer.

# Save registers

`s*` registers are, by convention, required to be preserved even if another function is called.  

# Kernel Programming

Recursion and large arrays of local variables are generally discouraged in kernel programming as to minimise data corruption from the same memory region being used for several purposes.

# Threads

## Co-operative vs Pre-emptive Multithreading

>  In cooperative models, once a thread is given control it continues to run until it explicitly yields control or it blocks. In a preemptive model, the virtual machine is allowed to step in and hand control from one thread to another at any time. Both models have their advantages and disadvantages.  
Java threads are generally preemptive between priorities. A higher priority thread takes precedence over a lower priority thread. If a higher priority thread goes to sleep or blocks, then a lower priority thread can run (assuming one is available and ready to run). However, as soon as the higher priority thread wakes up or unblocks, it will interrupt the lower priority thread and run until it finishes, blocks again, or is preempted by an even higher priority thread.  
The Java Language Specification allows VMs to occasionally run a lower priority thread instead of a runnable higher priority thread, but in practice this is unusual.  
However, nothing in the Java Language Specification specifies what is supposed to happen with equal priority threads. On some systems these threads will be time-sliced, and the runtime will allot a certain amount of time to a thread. When that time is up, the runtime preempts the running thread and switches to the next thread with the same priority. On other systems, a running thread will not be preempted in favor of a thread with the same priority. It will continue to run until it blocks, explicitly yields control, or is preempted by a higher priority thread.

* Co-operative multithreading - takes control until it `yield`s itself.
* Pre-emptive multithreading - Interrupted

Co-operative multithreading trusts that other programs will be `yield`ing at several times - we can't trust this.  

## User-level vs Kernel-levels thread

_aka User-level management of threads vs kernel-level management of threads_  

* User-level
  * Normally co-operative
  + Decide how the scheduler operates (ordering the importance of threads)
  + Lots of threads
  - Kernel only sees one thread (as it is all user-managed)
  - Kernel might only allocate one thread to the program, cannot utilise multithreading
  - Cannot use the clock to interrupt
* Kernel-level
  * ???

# Assume a multi-processing system with single-threaded applications. The OS manages the concurrent application requests by having a single thread of control within the kernel for each process. Such an OS would have an in-kernel stack associated with each process. Switching between each process (in-kernel thread) is performed by the function `switch_thread(cur_tcb,dst_tcb)`. What does this function do?

* Saves all registers inc status register, program counter, PID, etc
* Process put to sleep, and put to READY
* _Determine which thread is next to execute_
* Other thread has its registers restored, etc
* Wake up process

# Why do we have to be careful when writing kernel-level code?

* Kernel-level code has access to anything
  * Need to ensure that nothing will be corrupted
* An error in kernel-level is fatal - will crash the system without any exception/error handling.


# Do syscall function names need to have the same name as the library function?

Nope! It's up to the library developer!

