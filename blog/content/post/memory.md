---
title: "Memory"
date: 2020-03-24T19:51:05+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

**Principle of Locality** - Things closer to each other are faster.

Registers can be accessed in a nanosecond.  
Caches can be accessed in two nanoseconds.  
Main memory can be accessed in about 10 nanoseconds.  
Magnetic disks can be accessed in around 10 milliseconds.  
Magnetic tape, takes, forever.

# Effective Access Time

The effective access time of the memory subsystem depends on the hit rate in the first level

`T = H*T1 + (1-H)*T2`

* `T` - Effective access time
* `T1`- Access time of Memory 1
* `T2`- Access time of Memory 2
* `H` - Hit Rate in Memory 1

_That is, if the first memory device does not hit / accept the request, it is passed onto the second (slower) memory device_

## Example

> The cache memory access time is 1ns, with a hit rate of 95%.  
The main memory access time is 10ns.

`T_eff = 0.95 * 10^-9 + (1-0.95) * (10^-9 + 10 * 10^-9)`  
`T_eff = 1.5 * 10^-9`