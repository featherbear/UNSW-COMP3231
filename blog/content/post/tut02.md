---
title: "Tutorial 2"
date: 2020-02-24T16:09:20+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# The Role of the Operating System

## Abstracts Hardware

Provides a high level of access to the devices in the system

## Manages Resources

Fairly (tries to) assigns resources to each task

# Privileged/Kernel vs User Mode

* Programs run in user mode
* OS runs in kernel mode

* Programs in user mode can't do all instructions; goes through the kernel to request access
  * Disabling interrupts
  * Low level hardware access

# Kernel-only Access

* Disabling interrupts
* Setting time of day clock (..ehhhh.)
* Change the memory map (Allocated RAM to the process and other processes)
* Hard-disk controller register

---

User can perform `reading the time of day clock`, `fsync`

---

# File Descriptors

0 - stdin
1 - stdout
2 - stderr

# Threads vs Process

Threads are like forks, except that they share their global memory.  
Local memory is however independent.  

