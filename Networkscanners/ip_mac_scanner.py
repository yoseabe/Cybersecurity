from scapy.all import ARP, Ether, srp

target_ip = input("Target IP>")
arp =ARP(pdst=target_ip)

ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether/arp
result = srp(packet,timeout=5)[0]
clients = []

for sent, received in result:
	clients.append({'ip': received.psrc, 'mac': received.hwsrc})
print("Available devices in the network:")
print("IP" + " " * 18 + "MAC")

for client in clients:
	print("{:16}    {}".format(client['ip'], client['mac']))