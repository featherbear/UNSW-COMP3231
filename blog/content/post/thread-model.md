---
title: "Thread Model"
date: 2020-02-20T12:19:08+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams:
  enable: false
  options: ""
---

Asynchronous Model - Keep track of requests waiting to be fulfilled.

# Thread Model

![](Screenshot from 2020-03-24 18-33-39.png)

Each thread has its own stack

- Local variables per thread
  - Allocated in their own stack frame
- Global variables are shared between all threads
  - Allocated in the data section
  - Concurrency control is an issue
- Dynamically allocated memory (`malloc`) can be global or local
  - Program defined (pointer can be global or local)

A thread uses less resources than a process.

## Related Metadata

* Program Counter
* Registers
* Stack
* State

## Example - Multithreaded Web Server

Consider two requests made to a single threaded server.  
If the first request takes a long time to fetch a resource, the second requests will never be attended to until the first request is done.

In a multi-threaded server, there is a dispatcher thread which delegates requests to the pool of worker threads.  
This creates a degree of parallelism.

# Kernel-Level Threads

* TCB stored in the kernel

* **Pros**
  * Preemptive Multithreading
    * Can pause the state of a thread
  * Parallelism
    * Can perform other tasks whilst one thread is blocked from an outstanding syscall
    * Multiprocessor usage
    
* **Cons**
  * Operations are more expensive than with user-level threads
    * Thread operations (creation, destruction, blocking, unblocking) require the processor to enter kernel mode
      * Kernel entry and kernel exit delay

# User-Level Threads

* User-level **Thread Control Block** (TCB)
* User-level ready queue
* User-level blocked queue
* User-level dispatcher

A developer can implement a scheduler into their own program.  
The kernel will only see this program as a single process.

> Consider `yield` in Python

* **Pros**
  * Don't need to wait for traps to and from the kernel
  * Fine tuned dispatching algorithm
  * OS independent
* **Cons**
  * You probably will screw up writing it
  * Does not utilise multiple CPUs, as the program was only allocated one CPU
    * _Consider a virtual machine which has been assigned only one CPU on a device with 8 cores_
  * A blocking syscall will block the process, and hence all the threads