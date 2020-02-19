---
title: "Assignment 0"
date: 2020-02-19T22:51:30+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

This assignment introduces us to the OS/161 environment: of how to compile the kernel, run the operating system, and to learn how to debug errors.

For setup instructions, look [here](../os161)

# Building the Kernel

[`./rebuild.sh`](../os161#installation)

# Running the OS

In `~/cs3231/root`...

* Start - `sys161 kernel`
* Wait for debugger before start - `sys161 -w kernel`

# Debugging

In `~/cs3231/root`...

* Execute `os161-gdb kernel`
* Use the [_connect_ command](../os161#installation)

* _where_ -> show current call frames
* _frame n_ -> Inspect frame `n`
* _list_ -> Show source code

---

From the _where_ command, we see get this result

```
(gdb) where
#0  membar_any_any () at includelinks/machine/membar.h:47
#1  membar_store_store () at includelinks/machine/membar.h:58
#2  lamebus_write_register (bus=<optimised out>, slot=<optimised out>, offset=offset@entry=16, val=val@entry=0) at ../../arch/sys161/dev/lamebus_machdep.c:184
#3  0x800052ec in ltrace_stop (code=code@entry=0) at ../../dev/lamebus/ltrace.c:87
#4  0x8000ad58 in panic (fmt=fmt@entry=0x80023bd8 "I can't handle this... I think I'll just die now...\n") at ../../lib/kprintf.c:184
#5  0x8001b2a8 in mips_trap (tf=0x80027f28) at ../../arch/mips/locore/trap.c:315
#6  <signal handler called>
#7  0x8000b504 in boot () at ../../main/main.c:140
#8  0x8000b5d4 in kmain (arguments=0x80026020 "") at ../../main/main.c:218
#9  0x8001d1ac in __start () at ../../arch/sys161/main/start.S:216
```

We can see that because of the signal handler being raised in #6, an exception was raised from #7.

## Method One - `frame 7`, `list`

```
(gdb) frame 7
#7  0x8000b504 in boot () at ../../main/main.c:140
140                     * foo = 'x';            /* attempt to access it */
(gdb) list
135             kheap_nextgeneration();
136
137             {
138                     /* remove this section of code to fix ASST0 */
139                     char *foo = NULL;       /* create a NULL pointer */
140                     * foo = 'x';            /* attempt to access it */
141             }
142
143             /*
144              * Make sure various things aren't screwed up.
(gdb)
```

## Method Two - `list *0x8000b504`

```
(gdb) list *0x8000b504
0x8000b504 is in boot (../../main/main.c:140).
135             kheap_nextgeneration();
136
137             {
138                     /* remove this section of code to fix ASST0 */
139                     char *foo = NULL;       /* create a NULL pointer */
140                     * foo = 'x';            /* attempt to access it */
141             }
142
143             /*
144              * Make sure various things aren't screwed up.
(gdb)
```

---

After finding this 'bug', we can remove it and [`./rebuild.sh`](#building-the-kernel) the kernel.  
_BTW it's located at `~/cs3231/asst0-src/kern/main/main.c`_
