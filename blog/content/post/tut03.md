---
title: "Tutorial Week 3"
date: 2020-03-05T15:12:49+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---
# A particular abstraction only allows a maximum of 10 threads to enter the "room" at any point in time. Further threads attempting to enter the room have to wait at the door for another thread to exit the room. How could one implement a synchronisation approach to enforce the above restriction? 

Use semaphores, initialise the semaphore to a value of ten.  
Each thread will start with `P(sem)`.  
When they finish their task, `V(sem)`

# Multiple threads are waiting for the same thing to happen (e.g. a disk block to arrive from disk). Write pseudo-code for a synchronising and waking the multiple threads waiting for the same event. 

```
wait_block() {
  lock_acquire(lock);
  while (status != READY) cv_wait(cv, lock);
  lock_release(lock)
}
```

```
make_block_ready() {
  lock_acquire(lock);
  status = READY;
  cv_broadcast(cv, lock);
  lock_release(lock);
}

# Give a sequence of execution and context switches in which these two threads can deadlock. Then propose a change to one or both of them that makes deadlock impossible. What general principle do the original threads violate that causes them to deadlock?

```c
semaphore *mutex, *data;
 
void me() {
	P(mutex);
	/* do something */
	
	P(data);
	/* do something else */
	
	V(mutex);
	
	/* clean up */
	V(data);
}
 
void you() {
	P(data)
	P(mutex);
	
	/* do something */
	
	V(data);
	V(mutex);
}
```

Dead lock as they each hold a resource, and acquire the other.
Fix by changing the order of one of the acquire blocks.

----


**Always acquire resources and locks in a top-down fashion.**

---

# Synchronised Lists

Lock for the entire list?  
Or a lock for each node?