---
title: "Concurrency and Synchronisation"
date: 2020-02-20T12:39:56+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# The Issue

Race conditions: Depending on the scheduling and timing of the function execution.  
We cannot guarantee the order of execution, and hence the final state of a shared value being manipulated by simultaneous threads

Even in a single threaded processor, there is still concurrency built.

# Critical Region / Section

* Avoid race conditions of shared resources!  
* Blocks of lines need to execute sequentially without control being handed over to another task.  
* Critical sections should be as short as possible

# Mutex - Mutual Exclusion

* No two process simultaneously in critical region
* Platform Independence - Independent of the speed and number of CPUs
* Progress - No process running outside its critical region may block another process
* Bounded - No process waits forever to enter its critical region

## Mutex by Turns -> Each thread has its own turn ID

* Although requires threads to be aware of other turns

+ Strict Alternation
- Busy waiting
- Process must wait its turn even while the other process is doing something else

## Mutex by Disabling Interrupts

* Before entering a critical region, disable interrupts
* After leaving the critical region, enable interrupts

+ Simple
- Only available in the kernel
- Blocks everybody else, even with no contention
  - Slows interrupt response time
  - Includes ALL interrupts - keyboard, mouse, network
- Does not work on a multiprocessor -> UNIPROCESSOR ONLY

## Hardware Mutex

Test and Set Instruction

* Checks the lock
* Sets the lock
* Returns a lock

... In an atomic behaviour (all guaranteed to occur in succession)

+ Simple 
+ Available at user-level
  + Multiprocessor compatible
  + Can implement multiple lock variables
- [Busy waits](#busy-wait) (aka Spin lock)
  - Consumes CPU
  - Starvation possible, many processes waiting for one lock


# Busy wait

Issue: Wastes CPU

When a process is waiting, call sleep -> change process into blocked.  
When the process in critical section exits its critical component, call wakeup

# Producer Consumer // Bounded Buffer

Producer produces data items and store the items in a buffer.  
Consumer takes the items out of the buffer and consumes them.

[Read more](../producer-consumer-problem)
