---
title: "Multiprocessor Systems"
date: 2020-04-30T22:11:31+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams:
  enable: false
  options: ""
---

> The faster you go, the harder it is to accelerate (without heaps of effort)

A single CPU can only go so fast (because physics).  
So instead, we can employ multiple CPUs to do the same task!

# Amdahl's Law

Given a portion `P` of a program that can be made parallel, and the remaining serial portion `1 - P`, then using `n` processors will give an increase of `1 / ([1-P] + P/N)`

i.e. If (hypothetically) 100% of the program was parallel, then for 2 CPUs there is a speed up of (1 / 1/2 ) = 2 times

# Types of Multiprocessors

- UMA - Uniform Memory Access
  - All memory accesses occur at the same speed
- NUMA - Non-Uniform Memory Access
  - Access to some parts of the memory is faster for some processors than for other parts of memory

# Bus Based UMA Multi Processors

Multiple processors share the same bus (data communication channel).

## Caching

Each processor also has their own cache, so less memory accesses are required.  
However whilst each processor has its own cache, eventually the bus' bandwidth will become a bottleneck.

In addition, cache consistency between processors must be addressed.  
Often cache updates propagate to other caches; but this also consumes bandwidth - as well as syncing/timing issues.

## Multi-Core Processors

Multiple cores within the same CPU chip; each has their own cache, which goes to a central cache within the chip.

# Designing a good OS for multiprocessing

- Building scalable multiprocessor kernels is hard.
- Lock contention can limit overall system performance.

## Isolated OS

- Each CPU has their own OS
- Memory is statically assigned to each CPU
- Each processor has its own scheduling queue - some may be idle whilst one is very busy
- Each processor has its own memory partition - some may be empty, whilst one is occupied
- Hard to move data between CPUs

## Symmetric Multiprocessors (SMP)

- OS Kernel runs on all processors
- Load and resources are balanced between processors
- Requires synchronisation between processors

### Single Mutex Lock (Single critical section)

Only one CPU can be in kernel-mode at a time.  
Good - until you want to load balance kernel-mode operations

### Selective Lock (Multiple critical sections)

Identify critical sections and turn them into separate critical regions.

## Achieving Multiprocessor Locking

Additional hardware is required to block other CPUs from accessing the bus during Test-Set-Lock operations.  
However, will cause a spinlock - which will lead to lock contention and bus contention (From continually checking for free state)

**_Solution: Read before TST_**

Locks can be shared in read-only mode until it is released.  
No race conditions!

![](Screenshot from 2020-04-30 23-14-35.png)

Read-before-TST operations is better, however there is still significant lock contention due to all processors having to read, then acquire a free lock simultaneously. Entering (and locking) critical sections also competes with other processors testing.

## Blocking Locks vs Spin Locks

Blocking Locks cause the process to sleep/suspend for a period of time, and to wake up after an amount of time.

For uniprocessor models - Blocking Locks are preferred...  
![](Screenshot from 2020-04-30 23-19-39.png)

However for multiprocessors, it can depend...  
![](Screenshot from 2020-04-30 23-23-29.png) ![](Screenshot from 2020-04-30 23-23-34.png)

## Spinning vs Switching

Switching (blocking) to another process requires time to switch context, clear caches, and update the TLB.  
However, it is more efficient if the lock is held for short amount of times - shorter than the time taken to context switch

**_Takeaway_** - Spinlock only for short critical sections, otherwise blocking locs are better.  
Do not wait for IO during spinlocks, and do not nest locks in spinlocks.
