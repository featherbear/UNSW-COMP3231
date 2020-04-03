---
title: "A look at the ext2 filesystem"
date: 2020-03-25T16:31:39+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# inode structure

* Mode
  * Type - file or directory
  * Access Mode - rwxrwxrwx
* UID - User ID
* GID - Group ID
* atime - last access time
* ctime - creation time
* mtime - last modified time
* size - offset of the highest byte written
* block count - number of blocks used / allocated