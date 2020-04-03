---
title: "Approaching assignment 2"
date: 2020-04-03T18:19:39+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

> Check out this page for useful stuff and references: [Assignment 2 - Useful Things To Know](../assignment-2-useful)

# Multiprogramming Nature

Assume that multiple programs can be running - which means that synchronisation access of shared resources must be implemented.

# Syscalls

In-kernel system call names should be prefixed with `sys_`

# VFS and VOP functions

In this assignment, our scope was the code to only interface system calls to the VFS layer.  
No low-level assembly code, disk controller code, file system code [[example]](https://github.com/featherbear/myLittleFUSE), etcetera was needed.

# Reading and Writing

This means that our read and write functions do not need to do any low level reading, but simply to pass the instructions to the virtual file system functions.

In the assignment, these instructions are passed through the `iovec` and `uio` structs, so we could use the below code to initialise them

```c
static void uio_init (
        struct iovec *iov, 
        struct uio *uio, 
        userptr_t buf, 
        size_t len, 
        off_t offset, 
        enum uio_rw rw
    ) {
    
    *iov = (struct iovec) {
        .iov_ubase = buf,
        .iov_len = len
    };

    *uio = (struct uio) {
            .uio_iov = iov,
            .uio_iovcnt = 1,
            .uio_offset = offset,
            .uio_resid = len,
            .uio_segflg = UIO_USERSPACE,
            .uio_rw = rw,
            .uio_space = proc_getas()
    };
}
```

---

# File Descriptor Table

The file descriptor table is a process-specific map of file descriptor numbers to open file entries.  
Our assignment implemented a maximum of `OPEN_MAX` (`128`) file descriptors per process.  

When a program performs a fork, the file descriptor table is duplicated (shallow copy) and assigned to the fork.

When it comes to synchronous programming, it was advised to have **only one** lock for the entire table

# Open File Table

The open file table is a global table of open file entries, which hold reference to files that are opened in the system. They contain metadata, such as the mode and flags of the file.  

They also store a reference count of how many process are dependent on the open file entry.  
Each call to `open` creates a new open file entry though, so this count will usually only be 1, unless a `fork` or `dup2` is executed.

When a file descriptor is closed, the reference count should be decremented.  
Only when the reference count is zero, will the open file entry be removed.  

Our open file table was implemented as a doubly linked list.

![](Screenshot from 2020-03-26 15-43-48.png)

# Spinlocks

Spinlocks cause the processor to BUSY-WAIT.  
As opposed to usual locks, spinlocks will prevent a thread from sleeping.  

Only one spinlock can be acquired at a time!
