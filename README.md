# Lab 2

## Team Members
- Alan Ichikawa -Chang 

## Lab Question Answers

Answer for Question A.1: 
The reliability of the UDP was a lot worse when the 50% was added. This occured because it doesn't have the same assurance as the TCP to get all the messages across in order and accurately. 

Answer for Question A.2:
The reliability of the TCP seemed to be similar if not the same with the speed being the only change. It took slightly longer when the 50% was added. It might be taking longer because of the 50% and it's requirement to send all the messages accurately and in order. 

Answer for Question C.1:
Argc is the argument count which contains the amount of commands there are. Argv[] is the argument vector which is an array of all the commands.
 
Answer for Question C.2:
A UNIX file descriptor is a number label that represents something in a file. The UNIX file descriptor table is the table that contains the files that each number label corresponds to.

Answer for Question C.3:
A struct is a custom variable that you can create that stores data. The structure of sockaddr_in is sin_family, sin_port, sin_addr, and sin_zero. Sin_family is the address. Sin_port is the port number. Sin_addr is another structure that stores the IPv4 address. Sin_zero is used for compatibility and is usually left as 0. 

Answer for Question C.4:
The inputs of socket() are AF_INET, SOCK_STREAM, and 0. The first input AF_INET is used to determine the domain like whether to use IPv4 or IPv6. SOCK_STREAM is used to determine what type of socket is used. The 0 is the function that is chosen to operate. The return value of socket() should be a file descriptor value or -1 if there was an error. 

Answer for Question C.5:
The first parameter of bind() is sockfd, or the file descriptor. The second parameter is sockaddr which contains data about what ip address to use and what port to use. The third parameter is addrlen, which is the size of the sockaddr structure in bytes. The first parameter of listen() is sockfd, or the file descriptor. The second parameter is the backlog which is the number of connections that are allowed.

Answer for Question C.6:
The infinite while loop is used in order to accept a connection at any time. If there are multiple simultaneous connections, it will only be able to accept 1 connection at a time.

Answer for Question C.7:
Fork() creates another process that copies another process allowing multiple of the processes to run. You can use fork() to accept multiple connection requests by having it copy the socket accept. 

Answer for Question C.8:
A system call is a function that is taken and used from the kernel. Bind() and listen() are examples of some of these functions that are from the kernel.  
