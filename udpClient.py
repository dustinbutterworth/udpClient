import socket
# From Black Hat Python: Python Programming for Hackers and Pentesters 1st Edition by Justin Seitz

target_host = "127.0.0.1"
target_port = 80
payload = "AAABBBCCC"

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto(payload.encode(),(target_host,target_port))

# receive some data
data, addr = client.recvfrom(4096)

print(data)