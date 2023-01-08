import scapy.all as scapy 
import threading, time, pyfiglet
"""
# Set the network range to scan
ip_range = "192.168.29.1/24"

# Set the interface to use for scanning
# To get a list of available interfaces, use the command: "ipconfig" (Windows) or "ifconfig" (Linux/Mac)
interface = "Wi-Fi"

# Create an ARP packet
arp = ARP(pdst=ip_range)

# Create an Ethernet packet
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# Combine the two packets
packet = ether/arp

# Send the packet and store the answer
result = srp(packet, iface=interface, timeout=3, verbose=0)[0]

# Print the list of devices that responded to the ARP request
print("List of devices in the network:")
for sent, received in result:
    print(received.psrc)
"""
banner = pyfiglet.figlet_format("LAN Scanner")
print(banner, end="")
print("|"+"_"*22 + "@Yashparwal1" + "_"*22+"|")
print("\n")

start_time = time.time()

def scanlan(ip_range, interface):
    # Create an ARP packet
    arp = scapy.ARP(pdst=ip_range)

    # Create an Ethernet packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # in any private network (LAN) data is transferred between 2 devices using MAC addrs, so that's why broadcast MAC is giver here not a broadcast IP 

    # Combine the two packets
    packet = broadcast/arp
    # Send the packet and store the answer
    result,noresult= scapy.srp(packet, iface=interface, timeout=10, verbose=0)

    # Print the list of devices that responded to the ARP request with their IP and MAC
    for element in result:
        print(f"{element[1].psrc} \t\t {element[1].hwsrc}")


# Set the network range to scan
ip = "192.168.29."
# Set the interface to use for scanning
# To get a list of available interfaces, use the command: "ipconfig" (Windows) or "ifconfig" (Linux/Mac)
interface = "Wi-Fi"
thread_list=[]
print("List of devices in the network:")
print("\n  IP Address \t\t    MAC Address")
for x in range(1,256):
    addr = ip+str(x)
    thread = threading.Thread(target=scanlan,args=(addr,interface))
    thread.start()
    thread_list.append(thread)

for item in thread_list:
    item.join()

end_time = time.time()
print("\nScan Completed in :", end_time - start_time  , "sec")