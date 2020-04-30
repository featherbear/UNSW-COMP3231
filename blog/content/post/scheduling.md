---
title: "Scheduling"
date: 2020-04-30T23:33:02+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams:
  enable: false
  options: ""
---

> Which process runs next? Which user is served next? Which job executes next?

Scheduling is important when there are many things that a system needs to do.

> **Foor for Thought - Perceived Performance**  
> Small progress visible in the window, or to see the program lock up (but is busy in the background)

# Bound Processes

## CPU Bound Processes

Spends most of its time in computation.  
Completion largely affected by allocated CPU time

## IO Bound Process

Spends most of its time waiting for IO.  
Completion largely affected by IO request time

## Considerations

- Executing an IO bound process hardly affects the execution of a CPU bound process.
- Executing a CPU bound process **greatly** affects the execution of an IO bound process
  - IO is blocked

Aim to favour IO bound processes over CPU-bound processes

# Scheduling Execution

Scheduling occurs during many phases of a system's and program's lifecycle.

- Spawning a new process
- Exiting a process
- Process waiting for IO
- Encountering a lock
- IO Interrupt
- Time interrupt

## Non-Preemptive

A thread running in `running` state, will continue tor un until it completes, blocks IO, or yields.

## Preemptive Scheduling

The OS interrupts the current running thread, and moves it to the `ready` state.  
This is caused by an internal timer elapse, or other higher priority process that has become ready.

# Scheduling Algorithms

Scheduling algorithms provide fairness, enforcement of policy and resource balance

## Interactive Algorithms

- Minimise response time from user input
- Provide response proportionality (short jobs will return faster than long jobs)

### Round Robin Scheduling

Each process is given a time slice to execute in.  
When the time slice expires, the next process runs on.

- Ready queue with interrupt

Time slice too short - Time wasted from context switching  
Time slice too long - System not responsive

### Priority Queue (with optional Round Robin)

Processes with a higher priority are allocated more time to execute.

However, if there are many high priority processes - low priority processes will starve (as they are not allocated [enough] resources)

## Real-time Algorithm

- Meet strict time deadlines
- Provide predictability

## The UNIX Scheduler

The UNIX scheduler is a two level scheduler.

On the high-level - Processes are scheduled for memory and disk operations  
On a lower level - Processes are scheduled for CPU run time

Tasks are calculated for a priority number - the lower the number the higher the priority.  
These priority numbers are calculated every second

> Refer to [[Tutorial 10](../tut-10#priority)]

**Priority = CPU Usage + Nice + Base**

- CPU Usage - Number of clock ticks used (This value decays over time to ensure fairness)
- Nice - User managed offset
- Base - System managed offset (IO priority, swapper, etc)

# Distributing Tasks Between CPUs

## Single Shared

> All CPUs share a single queue.

Simple, and load balancing occurs.

However, there is lock contention - only one CPU can access the queue at a time.

**Affinity Scheduling** - Resources related to a process will only exist on the CPU is ran on.  
To mitigate the time for resources to be loaded on a new CPU, processes should be resumed on the same CPU.

## Multiple Queue

Each CPU has its own queue.  
Deals with affinity scheduling, as processes stay within a CPU.

If a CPU has finished its tasks, it can 'work steal' from another computer
