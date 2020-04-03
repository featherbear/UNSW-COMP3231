---
title: "Memory Management"
date: 2020-04-03T18:22:44+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

> Memory is a resource that needs to be managed.  
Ideally we would want LOTS of FAST memory; but this is very difficult; it's easier to get LOTS of SLOWER memory.  
&nbsp;  
The lower the degree of multiprogramming, the lower the CPU utilisation (lots of IO wait).  
The higher the degree of multiprogramming, the higher the CPU utilisation.

![](Snipaste_2020-04-03_18-11-11.png)

# Static Memory Management

## Simple Memory Management

In a simple memory system, the memory is split into equally sized partitions.  
Applications can then be assigned one of these partitions.

However, **internal fragmentation** occurs - as any unused space is wasted.  
Additionally, as all partitions are of the same size, they will each need to be large as the highest memory consuming application; consequently, the smallest memory-consuming application will have a tremendous amount of internal fragmentation.  

This is okay for highly predictable workloads, but is not efficient for common workloads.

## Queue Strategy - First Fit

The memory is split into partitions of different sizes, which each have a queue.  
Processes are appended to the queue for the memory partition that first fits them (smallest to largest).  

Most applications don't consume that much memory, so larger sized partitions may be idle; and also delay the execution of applications that consume little memory as they need to wait in the queue.

## Queue Strategy - Any Fit

Applications are added to the queue of any partition that fits.  
For example, a small job may be queued into a large memory partition.  

(This can done by maintaining an index of the last memory partition checked)

# Dynamic partitioning

Partitions are dynamically allocated and assigned to programs.  
This eliminates internal fragmentation issues, and with good algorithms - free memory can quickly be located.

However dynamic allocation brings new challenges, like minimising **external fragmentation**, memory overhead (from keeping track of partitions), and also efficiently merging free space together.

> Minimising overhead often involves using the unallocated memory as temporary storage for memory metadata.

## First Fit Algorithm

Scans the memory from the first entry.  
If the block of free space is sufficient, then split the free space into the allocated, and (possibly) outstanding free space. Then allocate the program to the reserved space.  

There is often **external fragmentation near the end**, due to released memory being re-re-re-re-revisited and reallocated.

## Next Fit Algorithm

Restarts the search at where it left off. There is often **external fragmentation near the start**.

## Best Fit Algorithm

The entire memory is scanned for the smallest region that will fit the requested memory.  
However, having need to search the entire memory region, it is very slow.  

The smallest memory region will be unusable until memory regions around it are released.

---

# Swapping

When the RAM is full, and more memory is needed, the computer can use space on secondary storage (i.e. from an SSD) as a RAM storage location. However, as secondary storage is logically further away from the CPU, it will be much slower.  

Regardless, it allows for the memory of inactive processes to be stored off-RAM, to create more space for new/active processes that request for memory.

# Memory Address Binds

## During Compile/Link time

The entrypoint location of the program needs to be known at compile-time. When this entrypoint changes, the program needs to be recompiled

## During Load/Object time

The compiler generates relocatable code

## Run time

Logical addresses are translated to physical addresses

# Compaction

Compaction is the process of reducing external fragmentation, by moving memory around so that there is a larger contiguous free space. This is **hard to perform** in software as processes will not know where the memory has been relocated to.

Software-wise, this is a large overhead (storage and time) as there needs to be a memory map.  
Often, hardware is implemented to do this.

# Base and Limit registers / Base and Bound machines

* Adds a memory region floor, and offset to requested memory addresses so that they point to their allocated space
* Entire memory has to be in RAM
* Sharing memory not possible

# Virtual Memory

What if the process is bigger than RAM?  
Well then, we click [here](../virtual-memory) to read the post about virtual memory!

# Paging

* No external fragmentation
* Only the last page will have internal fragmentation
* Memory can be shared by mapping memory to the save page
* Uses hardware: Memory Management Unit (MMU) 
  * aka Translation Lookaside Buffer (TLB)
