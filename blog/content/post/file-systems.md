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

