---
title: "Context Switching"
date: 2020-03-24T18:46:22+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

A **context switch** is the event which happens when the CPU changes from one thread/process to another thread/process. When a context switch occurs, the state of a thread/process is saved, and the next thread's/process' state is restored - Such as the following [state items](../processes-and-threads#related-metadata).  

The threads and processes themselves are oblivious to their execution being interrupted by context switches, and when restored - they continue as if nothing has happened.

They can be called on demand (ie a blocking syscall, or an exit() function), but also automatically (through exceptions and interrupts). They can occur between any two CPU instructions (Note: This is not the same as a program instruction, which might be composed of several CPU cycles)