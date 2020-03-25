---
title: "Virtual File System"
date: 2020-03-25T15:22:41+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

The virtual filesystem provides a framework that separates file-system independent and file-system dependent code.  
It allows different file-systems to work together, and appear as if they were connected.

> for example, mounting a network drive into a folder on your computer

* They provide a single system call interface which will work for all file systems
* File-based interface to arbitrary device drivers (`/dev`)
* File-based interface to kernel data structures (`/proc`)
* Provides an indirection layer for system calls
  * Automatic setup of file operation tables
  * Forwards the call to the correct handler

# VFS

* Represents all file system types
* Contains pointers to functions to manipulate each file system as a whole (`mount`, `unmount`)

# Vnode

* Represents a file/inode in the underlying system.
* Points to the real inode
* Contains pointers to functions to manipulate the inodes (`open`, `close`, `read`, `write`, ...)

---

|VFS Structure|Vnode Structure|
|:-----------:|:-------------:|
|![](Screenshot from 2020-03-25 15-52-58.png)|![](Screenshot from 2020-03-25 15-52-51.png)|

# OS/161

![](Screenshot from 2020-03-25 16-02-02.png)
![](Screenshot from 2020-03-25 16-02-36.png)

![](Screenshot from 2020-03-25 16-02-42.png)
![](Screenshot from 2020-03-25 16-02-47.png)

![](Screenshot from 2020-03-25 16-05-27.png)

# File Descriptors

Each open file has a file descriptor, which we pass into file operations (`read`, `write`, `lseek`, etc).  

File descriptors also hold other state values

* File pointer
  * Where we currently are in the file
  * File mode (read only?)

# File Descriptor Table

The File Descriptor table is a map which translates a file descriptor (numerical number) into a vnode in the Open File table.  

# Open File Table

The Open File table stores the vnode that are currently in use

# Multiple Processes

![](Screenshot from 2020-03-25 16-08-45.png)
![](Screenshot from 2020-03-25 16-09-51.png)

Each process needs to have its own File Descriptor table, so that entry 1 of one process does not need to have the same value as entry 1 of a different process. The Open File table, however, is a global structure that all processes share.



