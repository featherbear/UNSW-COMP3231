---
title: "Deadlock"
date: 2020-02-27T12:12:37+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---


// req -> block until available -> release resource

* Preemptable resources
  * Can be taken away from a process without ill effects
* Nonpreemptable resources
  * Cause process failure if taken away

Deadlock occurs when two mutually exclusive resources are both occupied at the same time.  
ie devices, locks, tables, etc, ...

---

# Conditions for Deadlock

All four must be true for deadlock to occur

* Mutual Exclusion condition
* Hold and Wait condition
  * Holding a resource whilst waiting for another resource
* No Preemption condition
  * Previously granted resources cannot be forcibly taken away
* Circular Wait condition

---

TODO: Directed Graph

Arrow from resource to process -> Exclusive access
Arrow from process to recess -> Request

Circular flow = dead lock

# Dealing with Deadlock

* Ignore
  * Reasonable if deadlocks occur very rarely
* Prevention - Negate one of the four required conditions
  * Mutex - Not always feasible to implement a non-mutual exclusive resource system
  * Hold and Wait - Not all required resources may be known at program start
                  - Release all resources if one resource is unavailable; then try again
                    - Livelock -> Unblocked but no progress making - ie people walking opposite me
  * Preemption - Not feasible, might break something
  * Circular wait - Resource queue - Fetch resources in ascending order
* Detection and Recovery - Alllocation matrix; request matrix

Resources in existence -> Vector E_n -> n number of resources
Resources available -> Vector A_n


Each row is a process
Each column is a resource

Algorithm ::
Add things up. For process which can fulfil, remove process and try agin

-- slide43


recovery through preemption
recovery through fallback
recovery through process killing
;;


* Avoidance
-- allocating resources such that deadlock won't occur
-> only if enough informtion known in advanced 


^
\ >

Delay requested resource allocation

**Safe and Unsafe States**
A state is safe if the system isn't deadlocked, and a scheduling ordere exists where every process will be able to complete.

Banker's algorithm
-> Checking | Assume max, determine if the max can be satisfied. Then 'finish' / remove the process
-> Even if satisfiable, postpone it for later; else resource deadlock
-> Hard to use, unknown required resources in a dynamic systems
Unsafe ~= will deadlock -> but no gaurantee it won't deadlock

# Starvation

A process is ready to run, but never gets picked
