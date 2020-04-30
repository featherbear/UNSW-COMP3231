---
title: "Tutorial Week 10"
date: 2020-04-27T21:35:33+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams:
  enable: false
  options: ""
---

# Queueing thread activity

## Global Queue

If a single lock is shared between all CPUs.  
Lock contention

## Per-CPU Queue

Poor load balancing

# Priority

Priority = CPU_usage + nice + base.

The closer the priority is to -inf, the higher the priority.  
The higher the priority is to +inf, the lower the priority.

- e.g. IO bound applications (that waits for IO) have low CPU usage, and therefore higher priority
- Nice - Custom value
- Base - Kernel level has a lower base, User level has a higher base

# Program IO / Polling

# Deadlock

P1 acquires a resource X  
P2 wants that resource X  
P1 needs more space in its stack, but P2 is blocking it

Solution - P2 allocates a new stack space and moves itself over to that spot.  
P1 is then able to expand its stack.

# Thrashing

Working set size - the pages that are most commonly accessed (ie main code blocks)

As the working set size increases, the CPU utilisation goes up.

- Sample the number of page faults
