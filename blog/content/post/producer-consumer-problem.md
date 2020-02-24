---
title: "Producer Consumer Problem"
date: 2020-02-24T13:12:18+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---


Producer produces data items and store the items in a buffer.  
Consumer takes the items out of the buffer and consumes them.

A test condition and the result action needs to occur as an **atomic instruction** (considered as one instruction)

# Semaphores

Blocks a thread until unblocked by an external signal.  
Unblock is **external**, rather than an internal check condition.  

Each primitive is atomic, and is usually implemented by disabling interrupts.

* aka wait-signal
* aka down-up
* aka P-V

A semaphore has a `count` - number of times a thread can call `wait` before they start blocking.  

* `count = 0` - first thread will block
* `count = 1` - the first thread will execute, the second will block

```
// wait
flag->count--; // Always subtracts one, but will sleep the thread, so it can't decrement again

// signal
flag->count++;
// allow ONE blocked thread to continue // This is fine as each process which `wait`s, also `signal`s
```

---

```
#define N = 4

semaphore mutex = 1;

// Empty slots
semaphore empty = N;

// Full slots
semaphore full = 0;

/* Separate semaphore for empty and full, to cater for multiple producers and/or multiple consumers
```

- Must `signal` for every `wait`
  - Easy to make mistakes, hard to detect

# Monitors

* High-level synchronisation primitive
* "Class" wrapper over a function which guarantees execution mutex
* Any requested thread/function is placed into a queue, so only one can executate at a given time

```
condition x, y;
x.wait() 
x.signal() -> allows another thread to execute, pausing itself
```

# Dining Philosophers

* Philosophers eat / think.
* Eating needs 2 forks
* Pick up one fork at a time
* How to prevent deadlock

5 forks, 5 philosophers.  
If all 5 take their left fork, there are 0 forks remaining.  
They will all deadlock, as they cannot take a fork on their right.  

Philosopher wakes other philosophers up when they finish eating


# Readers and Writers Problem

* Access to a database
* Can have many **READERS**
* **WRITERS** must have exclusive access

READERS and WRITERS are mutually exclusive

