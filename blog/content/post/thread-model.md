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

TODO: diagram

Each thread has its own stack

- Local variables per thread
  - Allocated in their own stack frame
- Global variables are shared between all threads
  - Alocated in the data section
  - Concurrency control is an issue
- Dynamically allocated memory (`malloc`) can be global or local
  - Program defined (pointer can be global or local)

A thread uses less resources than a process.

## Example - Multithreaded Web Server

Consider two requests made to a single threaded server.  
If the first request takes a long time to fetch a resource, the second requests will never be attended to until the first request is done.

In a multi-threaded server, there is a dispatcher thread which delegates requests to the pool of worker threads.  
This creates a degree of parallelism.
