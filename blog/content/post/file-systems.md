---
title: "File Systems"
date: 2020-03-24T22:35:44+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

File-system abstractions give us many features and accessibility features

* Uniform namespace
* Hierarchical structure
* Arbitrarily-sized files
* Symlinks (Symbolic links)
* Contiguous address space inside a file
* Access control

But in reality, all of our files are stored as binary 1s and 0s on some medium.  
The data of a single is not necessarily all stored together on a disk.  
It might not even be all stored on the same disk!

> Bless the people who invented file system implementations

# File Access Patterns

* Sequential Access
  * Read from start to end in a linear fashion
  * Cannot reach a certain location without rewinding or forwarding to that spot
* Random Access
  * Bytes can be read in any order
  * Instant access to any location

# Typical File Operations

* Create
* Delete
* Open
* Close
* Read
* Write
* Append
* Seek
* Get Attributes
* Set Attributes
* Rename

# Directories

File directories provide a hierarchy in the organisation of files.  
They can be considered as files themselves.

## Typical Directory Operations

* Create
* Delete
* Opendir
* Closedir
* Readdir
* Rename
* Link
* Unlink

# File Sharing

## Access Rights

A consequence of having multiple users with access to the same files is controlling access to files.

* No access
* Knowledge - Know it exists
* Execute - Can run (but not read)
* Read - Can read
* Append - Add extra content
* Update - Add and delete content
* Change protection - Change access rights
* Delete - Delete the file
* Owner - Everything

## Simultaneous Access

i.e. `flock()`, `lockf()`

Files may need to be locked when it needs to be updated.
Otherwise at times, depending on the structure of the file; only individual portions of the file may need to be locked.

Raises mutex and deadlock issues

# The UNIX Storage Stack

* Application
* OS
  * FD Table - File descriptor table - keeps track of files opened by user-level processes; matches syscall interface to VFS interface
  * OF Table - Open file table - keeps track of files opened by user-level processes; matches syscall interface to VFS interface
  * VFS - [Virtual File System](../virtual-file-system.md) - Unified interface to multiple file systems
  * FS - Exposes directory hierarchy, symlink, random access files, protection (hides the physical location of data on disk)
  * Buffer cache - Keeps recently accessed disk blocks in memory
  * Disk scheduler - Schedule disk accesses from multiple processes
  * Device driver - Exposes a block-device interface (hides device-specific protocol)
* Disk controller - Exposes the disk as a linear sequence of blocks (hides the disk geometry, bad sectors)
* Disk

## File System Types

e.g. FAT16, FAT32, NTFS, ext2, ext3, ext4, ResierFS, XFS, ISO9660, HFS+, UFS2, ZFS, JFS, OCFS, BTRFS, JFFS2, exFAT, UBIFS.

There are many types of filesystems

* To cater for the different physical characteristics of storage devices
  * ext3 is optimised for magnetic disks, whilst JFFS2 is optimised for flash memory devices.  
* To cater for different storage capacities
  * FAT16 only works for drives under 2GB, whilst FAT32 is optimised for drives under 32GB.
  * ZFS are for large scalable drive arrays of multiple terrabytes.
* To cater for different CPU and memory requirements
  * FAT16 is good for embedded devices
  * ZFS takes a WHOLE LOT OF MEMORY
* Proprietary Standards
  * NTFS is closed source from Windows

## A look at magnetic disks

![](Screenshot from 2020-03-25 14-39-45.png)

* Has multiple platters
  * Which has multiple tracks
    * Which has multiple sectors
* Performance
  * Seek time - ~15ms max 
  * Rotational delay - for a 7200rpm drive, ~8ms max
* Keep related blocks close to each other!

## Inside a File System

The file system maps symbolic file names into a collection of block addresses.  
It keeps track of which blocks belong to each file, the order of blocks, and also which blocks are unused.

### Allocation Methods

> How does the filesytem store blocks?

#### Contiguous Allocation

* Easy to keep track of the file (at first)
  * Starting block, and length
* Good for sequential operations
* Hard to resize the file
* As files are deleted, free space becomes divided into many small chunks

#### Dynamic Allocation

* Disk is split into portions
* Fixed-size blocks are allocated
* Does not require pre-allocating disk space
* No external fragmentation
  * But then may have internal fragmentation
* File blocks will be scattered across the disk
  * Complex metadata management

i.e. instead of giving someone a single cookie, we give them the whole packet so they can have more cookies if they need

##### Linked List Allocation

Each block contains a pointer to the next block in the chain.  
Free blocks also have their own chain

* Single metadata entry per file
* Best for sequential files

* Poor random access
* Blocks become scattered across the disk

Leveraging physical storage medium capabilities with layout structure

##### File Allocation Table (FAT)

Keeps a map of the entire file system in a separate table.

* End-of-file blocks and empty blocks are marked with special values
* Table is stored on the disk, and is replicated in memory
* Random access is fast

* Requires a lot of memory
  * i.e. for a 200GB disk, there are 200 * 10^6 1K-blocks
    * 800 MB table
* Free block lookup is slow

###### Structure

![](Screenshot from 2020-03-25 15-07-30.png)

##### inode-based structure

Separate table (index-node / i-node) for each file.

* Only the table for the relevant file needs to be kept in memory
* Fast random access

* As i-nodes are dynamically allocated, we need to manage the free-space for i-nodes too now
  * Could use fixed-size i-nodes entries
  * last i-node points to an extension i-node (new space)

###### Managing free space with a linked list of free blocks

* Stored in the free blocks, until they are used.
  * Does require additional disk capacity
* Background jobs can re-order the list for better contiguity
* Only one block of pointers need to be kept in the main memory

###### Managing free space with bit tables

* Each bit represents a block.
* Have to search linearly to find free blocks
  * Easy to find contiguous space

###### Directories

Stored as normal files, and contained inside usual data blocks.  
Directory file is a list of entries which contain the file name, attributes, and the file's i-node number

### Block Size

* Disk Blocks (Sectors) - usually 512 bytes
* File system blocks - 512 * 2^N bytes

* Larger blocks
  * Less FS metadata
  * Fewer required IO operations (ie sequential access)
* Smaller blocks
  * Less internal fragmentation (less wasted disk space)
  * Less unrelated data loaded (ie random access)

### Fragmentation

Fragmentation occurs when data is split into fragments, and are not altogether.

#### External Fragmentation

* Space wasted external to the allocated memory regions
* i.e. There is enough memory space (in total), but is unusable as it is not contiguous.

#### Internal Fragmentation

* Space wasted internal to the allocated regions
* Allocated memory is larger than the requested memory