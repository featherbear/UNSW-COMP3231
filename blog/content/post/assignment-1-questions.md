---
title: "Assignment 1 Questions"
date: 2020-03-03T12:39:31+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Thread Questions

## What happens to a thread when it exits (i.e., calls thread_exit())? What about when it sleeps?

* Releases its allocated resources (ie memory)
* Destroys its stack
* Yields control back to the scheduler.

When a thread sleeps it goes into a sleep state, and stays asleep until a wakeup is called on it

## What function(s) handle(s) a context switch?

* `thread_switch` - machine-independent code - `thread.c`
* `switchframe_switch` - machine-dependent code - `switch.S`

## How many thread states are there? What are they?

There are four thread states.  

* `S_RUN`
* `S_READY`
* `S_SLEEP`
* `S_ZOMB` - Threads that have exited but still need to have thread_destroy called on them.

Source: `thread.h`

## What does it mean to turn interrupts off? How is this accomplished? Why is it important to turn off interrupts in the thread subsystem code?

Turning off interrupts disables external signals from being handled by the machine. These signals could include an alarm (timer), or GPIO events.  

They can be turned off with the `splhigh`, and turned back on with `spl0`.

For more fine-grained control, there are also the following functions:

* `splx`
* `spllower`
* `splraise`

Source: `spl.h`

Turning off interrupts is important to allow critical regions of code to execute entirely without context switching occuring.

## What happens when a thread wakes up another thread? How does a sleeping thread get to run again?

The sleeping thread is removed from the sleep queue, and its state is set to ready (?), and appended to the run queue.

# Scheduler Questions

## What function is responsible for choosing the next thread to run?

`schedule` from `thread.c`.  

## How does that function pick the next thread?

Threads run in a round-robin fashion.  
(Unless implemented otherwise)

## What role does the hardware timer play in scheduling? What hardware independent function is called on a timer interrupt?

The hardware timer signals the processor to reevaluate the current schedule. The hardware timer calls `hardclock`.

A `thread_yield` call is made at the end of every `hardclock`, forcing a context switch.

_So, `schedule()` is called every SCHEDULE_HARDCLOCKS number of hardclocks...????_


```c
void hardclock(void) {
	/*
	 * Collect statistics here as desired.
	 */

	curcpu->c_hardclocks++;
	if ((curcpu->c_hardclocks % MIGRATE_HARDCLOCKS) == 0) {
		thread_consider_migration();
	}
	if ((curcpu->c_hardclocks % SCHEDULE_HARDCLOCKS) == 0) {
		schedule();
	}
	thread_yield();
}
```

Source: `clock.c`


# Synchronisation Questions

## What is a wait channel? Describe how wchan_sleep() and wchan_wakeone() are used to implement semaphores.

A wait channel is a queue of threads which are waiting for the same signal.

`wchan_sleep` puts a thread to sleep, into a given wait channel.

`wchan_wakeone` wakes the head of the queue of a given wait channel.

This can be used to implement semaphores, by sleeping threads until signalled by `wchan_wakeone`, mitigating busy waits.

## Why does the lock API in OS/161 provide lock_do_i_hold(), but not lock_get_holder()?

Security? Other processes do not need to know who has an occupied lock, just the fact that the lock is unavailble.
