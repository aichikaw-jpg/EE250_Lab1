"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

HOST = "10.189.147.211"
PORT = 12000

def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    # TODO: Get user input and send it to the server using your TCP socket
    # TODO: Receive a response from the server and close the TCP connection

    #create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"hello")
        data = s.recv(1024)

        #infinite loop to get message
        while(1):
        #get the message from user
            user_input = input("Please type a message: ")
            #encode the user input, turning it from string to bytes so that s can send it
            s.sendall(user_input.encode())

    print(f"Received {data!r}")
    
    
    

    pass


if __name__ == '__main__':
    main()