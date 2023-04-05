import socket

HOST = '127.0.0.1'
PORT = 65432

n = input('Enter the value of n: ')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(n.encode())
    data = s.recv(1024)

print('The', n + 'th Fibonacci number is', data.decode())
