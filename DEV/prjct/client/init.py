from socket import *
import sys
import uuid


def get_mac():
  mac_num = hex(uuid.getnode()).replace('0x', '').upper()
  mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
  return mac

host = '11.xiver.keenetic.pro'
port = 48555
addr = (host, port)

udp_socket = socket(AF_INET, SOCK_DGRAM)

  
#encode - перекодирует введенные данные в байты, decode - обратно
data = str.encode(f"I\r{get_mac()}\r0.1b\r1234567890")
udp_socket.sendto(data, addr)
# data = bytes.decode(data)
# data = udp_socket.recvfrom(1024)
print(data)


udp_socket.close()
