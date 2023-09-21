readelf -h match
```
[root@ip-10-0-0-230 day1]# readelf -h match
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              EXEC (Executable file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x46dc60
  Start of program headers:          64 (bytes into file)
  Start of section headers:          624 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         10
  Size of section headers:           64 (bytes)
  Number of section headers:         36
  Section header string table index: 9
```

nohup ./match & && netstat -lntp
```
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:2024            0.0.0.0:*               LISTEN      3056/sshd
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      1802/rpcbind
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      2223/master
tcp        0      0 127.0.0.1:33601         0.0.0.0:*               LISTEN      2555/containerd
tcp6       0      0 :::2024                 :::*                    LISTEN      3056/sshd
tcp6       0      0 :::111                  :::*                    LISTEN      1802/rpcbind
tcp6       0      0 :::8080                 :::*                    LISTEN      6490/./match
```