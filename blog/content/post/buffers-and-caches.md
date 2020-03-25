---
title: "Buffers and Caches"
date: 2020-03-25T16:14:53+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Buffers

A buffer is a temporary storage used when transferring data between two entities.  
They are used to mitigate issues caused from differences in performance rates, or when a piece of data cannot be simply transferred to another device.

For example, when writing to a file on a disk; The computer does not need to wait for the file to be written to the disk, which may take a long time, and freeze intermediary user operations.  
Instead, the data is placed into the kernel buffer; and the write from the buffer to the actual disk can be scheduled at a later time.

Buffers can also be used to speed up (sequential) reading.  
Under the premise that reading a given block will probably then require the reading of the subsequent block; the subsequent block can be loaded into the buffer at the same as the first block - making possible read operations faster

# Caches

Caches are fast storage devices that temporarily hold data that is accessed repeatedly.  
This way, if a block on a disk is requested, but it is already stored in the cache; the disk does not need to be accessed!

The cache is built to use unused kernel memory space.  
_So, the more memory you need, the less cache space you have!_

# Saturated Buffers

If the buffer is full, we choose an existing entry to replace

Generally, the replacement policy is by the criticality of the disk block to file system consistency.  

For example, if a directory block or inode block is lost, it could corrupt the entire filesystem.  
A lost data block only corrupts the file they are associated with.

# Write-Through Caches

* All modified blocks are written immediately to disk
  * Including temporary files... which we might not want
    * Generates more disk traffic
    * Not optimised (better to write blocks at a time)