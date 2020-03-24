---
title: "Assignment 2 - Useful Things To Know"
date: 2020-03-24T14:15:27+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

<style>
details:not([open]) > summary::before {
content: "▸ ";
}

details[open] > summary::before {
  content: "▾ ";
}
</style>

# Scripts

Both scripts are to be placed in the parent directory, where `asst2-src` and `root` are subdirectories

## Build Script

```
#!/bin/bash

cd "$(dirname "$0")/asst2-src"

echo "Building User Files..."
bmake > /dev/null && bmake install > /dev/null

cd kern/compile/ASST2
echo "Building Kernel..."
bmake > /dev/null && bmake install > /dev/null
```

## Run Script

```
#!/bin/bash

cd "$(dirname "$0")/root"

sys161 kernel $@
```

# Syscall Table

<details>

<summary>Warning: There's alot.</summary>

|Function|ID|
|:-------|--:|
|`fork`|0|
|`vfork`|1|
|`execv`|2|
|`_exit`|3|
|`waitpid`|4|
|`getpid`|5|
|`getppid`|6|
|`sbrk`|7|
|`mmap`|8|
|`munmap`|9|
|`mprotect`|10|
|`umask`|17|
|`issetugid`|18|
|`getresuid`|19|
|`setresuid`|20|
|`getresgid`|21|
|`setresgid`|22|
|`getgroups`|23|
|`setgroups`|24|
|`__getlogin`|25|
|`__setlogin`|26|
|`kill`|27|
|`sigaction`|28|
|`sigpending`|29|
|`sigprocmask`|30|
|`sigsuspend`|31|
|`sigreturn`|32|
|`open`|45|
|`pipe`|46|
|`dup`|47|
|`dup2`|48|
|`close`|49|
|`read`|50|
|`pread`|51|
|`getdirentry`|54|
|`write`|55|
|`pwrite`|56|
|`lseek`|59|
|`flock`|60|
|`ftruncate`|61|
|`fsync`|62|
|`fcntl`|63|
|`ioctl`|64|
|`select`|65|
|`poll`|66|
|`link`|67|
|`remove`|68|
|`mkdir`|69|
|`rmdir`|70|
|`mkfifo`|71|
|`rename`|72|
|`access`|73|
|`chdir`|74|
|`fchdir`|75|
|`__getcwd`|76|
|`symlink`|77|
|`readlink`|78|
|`mount`|79|
|`unmount`|80|
|`stat`|81|
|`fstat`|82|
|`lstat`|83|
|`utimes`|84|
|`futimes`|85|
|`lutimes`|86|
|`chmod`|87|
|`chown`|88|
|`fchmod`|89|
|`fchown`|90|
|`lchmod`|91|
|`lchown`|92|
|`socket`|98|
|`bind`|99|
|`connect`|100|
|`listen`|101|
|`accept`|102|
|`shutdown`|104|
|`getsockname`|105|
|`getpeername`|106|
|`getsockopt`|107|
|`setsockopt`|108|
|`__time`|113|
|`__settime`|114|
|`nanosleep`|115|
|`sync`|118|
|`reboot`|119|

</details>

Found in `asst2-src/kern/include/kern/syscall.h`

# Error Numbers

<details>
<summary>Click to open</summary>

|Name|ID|Description|
|:--:|:--:|:--:|
|`ENOSYS`|1|Function not implemented|
|`-`|2|_unused_|
|`ENOMEM`|3|Out of memory|
|`EAGAIN`|4|Operation would block|
|`EINTR`|5|Interrupted system call|
|`EFAULT`|6|Bad memory reference|
|`ENAMETOOLONG`|7|String too long|
|`EINVAL`|8|Invalid argument|
|`EPERM`|9|Operation not permitted|
|`EACCES`|10|Permission denied|
|`EMPROC`|11|Too many processes|
|`ENPROC`|12|Too many processes in system|
|`ENOEXEC`|13|File is not executable|
|`E2BIG`|14|Argument list too long|
|`ESRCH`|15|No such process|
|`ECHILD`|16|No child processes|
|`ENOTDIR`|17|Not a directory|
|`EISDIR`|18|Is a directory|
|`ENOENT`|19|No such file or directory|
|`ELOOP`|20|Too many levels of symbolic links|
|`ENOTEMPTY`|21|Directory not empty|
|`EEXIST`|22|File or object exists|
|`EMLINK`|23|Too many hard links|
|`EXDEV`|24|Cross-device link|
|`ENODEV`|25|No such device|
|`ENXIO`|26|Device not available|
|`EBUSY`|27|Device or resource busy|
|`EMFILE`|28|Too many open files|
|`ENFILE`|29|Too many open files in system|
|`EBADF`|30|Bad file number|
|`EIOCTL`|31|Invalid or inappropriate ioctl|
|`EIO`|32|Input/output error|
|`ESPIPE`|33|Illegal seek|
|`EPIPE`|34|Broken pipe|
|`EROFS`|35|Read-only file system|
|`ENOSPC`|36|No space left on device|
|`EDQUOT`|37|Disc quota exceeded|
|`EFBIG`|38|File too large|
|`EFTYPE`|39|Invalid file type or format|
|`EDOM`|40|Argument out of range|
|`ERANGE`|41|Result out of range|
|`EILSEQ`|42|Invalid multibyte character sequence|
|`ENOTSOCK`|43|Not a socket|
|`EISSOCK`|44|Is a socket|
|`EISCONN`|45|Socket is already connected|
|`ENOTCONN`|46|Socket is not connected|
|`ESHUTDOWN`|47|Socket has been shut down|
|`EPFNOSUPPORT`|48|Protocol family not supported|
|`ESOCKTNOSUPPORT`|49|Socket type not supported|
|`EPROTONOSUPPORT`|50|Protocol not supported|
|`EPROTOTYPE`|51|Protocol wrong type for socket|
|`EAFNOSUPPORT`|52|Address family not supported by protocol family|
|`ENOPROTOOPT`|53|Protocol option not available|
|`EADDRINUSE`|54|Address already in use|
|`EADDRNOTAVAIL`|55|Cannot assign requested address|
|`ENETDOWN`|56|Network is down|
|`ENETUNREACH`|57|Network is unreachable|
|`EHOSTDOWN`|58|Host is down|
|`EHOSTUNREACH`|59|Host is unreachable|
|`ECONNREFUSED`|60|Connection refused|
|`ETIMEDOUT`|61|Connection timed out|
|`ECONNRESET`|62|Connection reset by peer|
|`EMSGSIZE`|63|Message too large|
|`ENOTSUP`|64|Threads operation not supported|

</details>

Found in `asst2-src/kern/include/kern/errno.h`

# MIPS Exception Codes

<details>
<summary>Click to open</summary>

|Name|ID|Description|
|:--:|:--:|:--:|
|`EX_IRQ`|0|Interrupt|
|`EX_MOD`|1|TLB Modify (write to read-only page)|
|`EX_TLBL`|2|TLB miss on load|
|`EX_TLBS`|3|TLB miss on store|
|`EX_ADEL`|4|Address error on load|
|`EX_ADES`|5|Address error on store|
|`EX_IBE`|6|Bus error on instruction fetch|
|`EX_DBE`|7|Bus error on data load *or* store|
|`EX_SYS`|8|Syscall|
|`EX_BP`|9|Breakpoint|
|`EX_RI`|10|Reserved (illegal) instruction|
|`EX_CPU`|11|Coprocessor unusable|
|`EX_OVF`|12|Arithmetic overflow|

</details>

Found in `asst2-src/kern/arch/mips/include/trapframe.h`

# Design Questions / Considerations


## What is the difference between UIO_USERISPACE and UIO_USERSPACE?

* `UIO_USERISPACE` - User Code
* `UIO_USERSPACE` - User Data

## When should one use UIO_SYSSPACE instead?

Kernel related stuff. Doesn't require validity checks - as the kernel is trusted to be safe.




---

## Conventions

* In-kernel system call names should be prefixed with `sys_`

## What data structures are private to each process? Which ones are shared (also think of concurrency issues)?

Refer to [Structures](#structures)

## What primitive operations exist to support the transfer of data to and from kernel space? Do you want to implement more on top of these?

## How you will keep track of open files? For which system calls is this useful?



# Implementation Details

## Structures

### File descriptor map

### Process information map

* pid
* cwd
* time
* pointers, registers
* arguments


## open


## read

## write

## lseek

## close

## dup2
