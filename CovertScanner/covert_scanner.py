from ipaddress import IPv4Network
from scapy.all import *
from scapy.layers.inet import sr1, IP, ICMP, TCP, Ether


# Globals
ports = (21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080)


def covert_scanner():
    scanned_addr = 0
    hosts_up = 0

    # Reading IPv4 and Subnet mask
    cidr = net_reading()

    # Calculating all IPs in network with ipaddress module
    net_addr_list = IPv4Network(cidr, False)
    print(f"Calculated addresses for the {cidr} network.\n")

    # Begin scanning with Host discovery
    print("~~~~~~ Covert Network Scanning has began ~~~~~~")
    for ip in net_addr_list:
        ip = str(ip)

        # Router check
        if ip.endswith("1.1"):
            continue

        # Check if Host is up
        if host_discovery(ip):
            hosts_up += 1

        scanned_addr += 1

    print("~~~~~~ Covert Network Scanning has ended ~~~~~~")
    print(f"There were a total of {hosts_up} hosts up out of the {scanned_addr} addresses that were scanned.")


def net_reading():
    ipv4 = []

    # Reading IPv4 address, with input handling
    print("~~~~~ IPv4 input ~~~~~")
    for i in range(4):
        while True:
            ip_oct = input(f"Please enter IPv4 octet n.{i + 1}: ")

            if ip_oct.isnumeric():
                ip_oct = int(ip_oct)

                if 0 <= ip_oct <= 255:
                    break
                else:
                    print("Please enter a valid number (0-255).")
            else:
                print("Input contained characters.")

        ipv4.append(ip_oct)

    print()

    # Reading subnet mask, with input handling
    print("~~~~~ Subnet Mask input ~~~~~")
    while True:
        sub_mask = input(f"Please enter the network's subnet mask: ")

        if sub_mask.isnumeric():
            sub_mask = int(sub_mask)

            if 1 <= sub_mask <= 31:
                break
            else:
                print("Please enter a valid subnet mask (1-31).")
        else:
            print("Input contained characters.")

    # Merging IP and mask
    cidr = str(ipv4[0]) + "." + str(ipv4[1]) + "." + str(ipv4[2]) + "." + str(ipv4[3]) + "/" + str(sub_mask)

    print(f"You entered: {cidr}")

    return cidr


def host_discovery(ip):
    # Packet creation
    icmp_pkt = IP(dst=ip) / ICMP()
    # print("ICMP echo-request packet constructed.")

    # Sending packet
    # print(f"Sending ICMP echo-request packet at {ip}.")
    icmp_ans = sr1(icmp_pkt, timeout=2, verbose=0)

    # Printing packet information
    # print("ICMP echo-request packet information:")
    # icmp_pkt.show()

    if icmp_ans is not None:
        print(f"Host at {ip} is up.")

        # Printing packet information
        # print("ICMP echo-reply packet information:")
        # icmp_ans.show()

        # Continue with Port scanning
        port_scanning(ip)
        return True
    else:
        print(f"Host at {ip} is down.")
        return False


def port_scanning(ip):
    print(f"~~~ Port scanning for {ip} has begun ~~~")

    # Scanning well known ports
    for port in ports:
        # Packet creation
        # print(f"TCP packet for port {port} constructed.")
        tcp_pkt = IP(dst=ip, ttl=128) / TCP(dport=port)

        # Printing packet information
        # print("TCP packet to send information:")
        # tcp_pkt.show()

        # Sending packet
        # print(f"Sending TCP packet at {ip}:{port}")
        tcp_ans = sr1(tcp_pkt, verbose=0)

        # Printing packet information
        # print("TCP packet received information:")
        # tcp_ans.show()

        # Checking TCP answer
        if tcp_ans.haslayer(TCP):
            if tcp_ans.getlayer(TCP).flags == "SA":
                print(f"Port {port} is open.")
            # elif tcp_ans.getlayer(TCP).flags == "RA":
            #     print(f"Port {port} is closed.")
        else:
            print(f"Did not get answer from port {port}.")

    print(f"~~~ Port scanning for {ip} has ended ~~~")


def main():
    print("This is a Covert Network Scanning tool.")
    print("You have to enter a valid IPv4 address with it's network's subnet mask and the scanner will")
    print("begin Host discovery and then continue with Port scanning for the hosts that are up.")
    print()

    covert_scanner()


main()
