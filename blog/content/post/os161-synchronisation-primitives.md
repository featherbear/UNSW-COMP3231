---
title: "OS/161 Synchronisation Primitives"
date: 2020-02-24T13:55:39+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Locks

* `struct lock *lock_create(const char *name);`
  * Name parameter for debug purposes!
  * Return `NULL` if out of memory -> Then `panic`
* `void lock_destroy(struct lock *);`
  * Destroy the lock
* `void lock_acquire(struct lock *);`
  * Enter the critical region
* `void lock_release(struct lock *);`
  * Exit the critical region

# Semaphores

* `struct semaphore *sem_create(const char *name, int initial_count);`

* `void sem_destroy(struct semaphore *);`

* `void P(struct semaphore *);`
  * Wait

* `void V(struct semaphore *);`
  * Signal

# Locks vs Semaphores

* Locks are binary || Semaphores are not.
* Semantic - intrinsic documentation -> Locks used for locks...

# Condition Variables

* `struct cv *cv_create(const char *name);`
* `void cv_destroy(struct cv *);`
* `void cv_wait(struct cv *cv, struct lock *lock);`
  * Sleep and wakeup on an event
  * Sleeps thread and releases the lock
    * On wakeup, reacquires the lock
* `void cv_signal(struct cv *cv, struct lock *lock);`
  * Wake up one
* `void cv_broadcast(struct cv *cv, struct lock *lock);`
  * Wake up all

-> 

<!-- * We can combine locks and condition variables to create our own monitors. -->

