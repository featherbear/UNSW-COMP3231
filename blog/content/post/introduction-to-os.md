---
title: "Introduction to OS"
date: 2020-02-17T13:09:51+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# What is an Operating System

## An abstract machine

* Extends the basic hardware, with added functionality
* Hides details of the hardware
* Provides a high-level abstraction of the system to the developer (common framework)

## A resource manager

* Allocates resources (CPU time, memory, etc) to users and processes (Depending on policy)
* Ensures no starvation occurs, and that progress is made

## The software running in privileged mode

On microprocessors with [levels of privileges](#microprocessor-privilege-levels) (user mode / kernel mode), the OS runs in the higher privileged mode.

# The Kernel

The kernel is the core part of the operating system.

* Kernel aka supervisor, nucleus, etc
* Fundamental functionality
  * Services
  * Security
* Applications should not be able to interefere with or bypass the operating system

Applications run on the OS.  
The OS runs on the kernel.  

# Microprocessor Privilege Levels

# User (application) mode

* Lesser access to the instruction set, memory
* Applications, system libraries (syscalls)


# Kernel (privileged/system) mode

* Full access to all instructions and resources
* OS, Devices, Registers, Memory

---

# Privilege-less Microprocessors and Operating Systems

Some embedded operating systems and architectures have no privileged components.  
Whilst they can implement OS functionality, they are unable to enforce restrictions and policies.  

They are good for small / single tasked operations.

# OS vs Application Software

In theory, the compiled code is effectively the same, but depending on the privilege level; certain machine instructions may not execute succesfully.

_Fun fact: Vendor graphics drivers install themselves in the OS_

# System Libraries

Some C library functions are just functions (we could implement it ourself), whilst others are system calls (require the OS and cannot be implemented ourselves).

> For example, we could implement `strcmp`, `memcpy`.  
> But we cannot implement `open`, or `close`.

