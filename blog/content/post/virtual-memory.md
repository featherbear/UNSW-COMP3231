---
title: "Virtual Memory"
date: 2020-04-09T18:13:39+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# The Memory Management Unit

Hardware device that translates virtual addresses into physical addresses.  
Translation isn't that fast, as the structure of the MMU may be complex (hash table)

Translation Look-aside Buffer - The TLB is a cache of the most recently accessed pages

## Usage

Given a virtual address, the address (as bits) is split into MSB and LSB nibbles

The MSB is passed into the MMU, which gives the correct frame.  
The LSB is used as an index in the frame.

The more bits MSB are used, the more the number of frames increase, by powers of two

## Two Level Page Table

> ie `0x01003007`  
`0000000100 0000000011 000000000111`

Split the MSB into two sections of MSB.

The first table points to a different table

## Inverted Page Table

The PID and Virtual Page Number is stored as entries in the IPT.  
The returned frame location is the address of the entry that matches the details.

A **hash anchor table** is often used to reduce the size of possible virtual addresses

## Hashed Page Table

HPT contains the Process ID, Virtual Page Number and Physical Frame Number


# Calculating average memory accesses with the TLB

Accesses if hit x Chance of hit + Accesses if miss x Chance of miss

> For a 95% hit ratio  
`1 * 0.95 + 3 * 0.05 = 1.1`

# Page Faults

* Illegal accesses - dereferencing null pointers etc
* Mapping not in the TLB
* Writing to a read only page (ie writing to the code segment of application memory)

# MIPS R3000

* EntryLo (12bits) - Offset
* EntryHi - contains the current ASID

* VPN - the 20 MSB in a virtual number
* ASID (6 bits) - Address Space Identifier

* ASID must be equal to EntryHi
* EntryLo contains the PFN

* Dirty bit 1 - Read and write
* Dirty bit 0 - Read only

* Global bit 1 - Ignore even if ASID different

* Valid bit 1 - valid mapping

## How-To

1) Ignore the LSB (last 12 bits / last 3 hex characters)
2) Compare the MSB to the VPN
3) Check if valid
4) Check if ASID matches, or if the global flag is set
5) Replace the MSB with PFN
6) Replace back the LSB
7) Check dirty bits, etc

---

# Locality

## Temporal Locality

Recently accessed items are likely to be accessed again

i.e. in a loop, the counter is continually accessed

## Spacial Locality

High chance of accessing nearby items soon

