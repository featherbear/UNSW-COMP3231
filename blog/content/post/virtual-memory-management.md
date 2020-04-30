s---
title: "Virtual Memory Management"
date: 2020-04-30T21:01:15+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
enable: false
options: ""

sequenceDiagrams:
enable: false
options: ""

---

# Segmentation / On-Demand Paging

Only crucial parts of a program (i.e the program's code) need to reside in the memory during execution.  
Other resources that are rarely used the process can be transferred off the memory and onto a secondary storage - to free up the memory.

If these non-resident pages are requested, the process is blocked (waiting for the IO request) and another process is allowed to run. When the IO request is complete (loading the page back into memory) the original process is again allowed to execute.

If a page to be transferred off from the RAM is clean (aka the dirty bit is _not_ set) - it can simply be discarded; as there will be no difference to retrieving the location again.

# Working Set

The pages required by an application over a period of time is call its **memory working set**.  
It can be used as an approximation for the measure of a program's locality.

This working set is roughly the amount of pages that a system should keep in its memory at minimum.

## Trashing

![](Screenshot from 2020-04-30 20-58-26.png)

Trashing is the occurrence where processes are unable to run due to a lack of available resources

- CPU utilisation often as more processes are run.
- The more processes there are running, the less memory there is available for each process.
- If processes are not able to get their minimum working set size - there will be lots of page faults
  - Guaranteed to be at least one page fault for every cycle of the program - BAD!
- Processes will have insufficient resources, and will be unable to run

CPU utilisation will therefore go down, and the system becomes IO limited

### Recovery

- Suspend some processes
- Move pages of suspended process to secondary storage ([segmentation](#segmentation))

This way there will be more available memory for each process, and hopefully processes will be able to resume

# Factors affecting VM system performance

- [Page Table structure](../virtual-memory#page-tables)
- [Page Size](#page-size)
- [Fetch Policy](#fetch-policy)
- [Replacement Policy](#replacement-policy)
- [Resident Set Size](#resident-set-size)
- [Page Cleaning Policy](#cleaning-policy)

## Page Size

### A larger page size...

- Decreased the number of pages (smaller page table)
- Increases TLB coverage (less TLB misses)
- Higher swapping IO throughput (less IO delay)
- (Increases internal fragmentation - Less flexible for processes that require little resource)
- (Increases page fault latency - More data to read from disk)

### Flexible Page Sizes

Multiple page sizes would allow the system to be more efficient, as memory can be distributed more equitably.

i.e. Larger page sizes for code, smaller page sizes for stacks

## Fetch Policy

> When should a page be loaded?

- On-Demand
  - Fetch when requested
  - A lot of page faults as the program starts
- Pre-paging
  - Read more / related pages
  - Fetch when idle
  - Hard to get right in practice

## Replacement Policy

> Which occupied page to remove for the new page

Optimally, discard the page that is least likely to be used soon.

Some frames may be locked, due to them being essential to system operation. For example, kernel code, kernel data, IO buffers, amd/or critical user pages.

### Types of Algorithms (in order of best to worst)

- <s>Hypothetical optimal - Discard the page that won't be used for the longest time (Impossible)</s>
- Least Recently Used - LRU - Discard the page with the smallest counter (Counter incremented on every reference)
- Clock Page Replacement - Check for pages that have been used within a given time, discard the first unused one
- First In, First Out - FIFO - Discard earliest page

## Resident Set Size

> How many frames should each process have?

### Fixed

- Assign all frames at run-time
- Some frames may not be utilised (wasted)

## Variable Allocation

- Check application type and requirements as to how many frames to allocate

### On-Demand Allocation

- Allocate a new frame when requested

## Cleaning Policy

- Observation - Read-only / Clean pages are cheaper and easier to replace than dirty pages
- On Demand - Clean when selected - Takes time for selection and for actual cleaning to happen
- Pre-cleaning - Pages are written out in batches (pagedaemon)
