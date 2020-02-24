---
title: "Deadlocks"
date: 2020-02-24T14:49:39+11:00

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