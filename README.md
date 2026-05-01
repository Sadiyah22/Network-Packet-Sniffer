# Network Packet Sniffer

## Overview
This is a network monitoring tool developed in **Python** using the **Scapy** library. It captures live data packets as they travel across a network interface, allowing for real-time analysis of source and destination traffic. This project demonstrates my understanding of the **TCP/IP stack** and the **OSI model**.

## Technical Goals
The objective of this sniffer is to:
* **Capture Live Traffic:** Intercept IP packets to analyze network communication patterns.
* **Protocol Identification:** Distinguish between different protocols such as TCP, UDP, and ICMP.
* **Header Analysis:** Extract and display critical header information, including Source and Destination IP addresses.

## How it Works
1. **Promiscuous Mode:** The script utilizes the Scapy library to listen to the network interface.
2. **Packet Callback:** Every captured packet is passed to a processing function that checks for the presence of an IP layer.
3. **Data Extraction:** The tool prints a summary of each packet, showing how data is routed between devices.

## Features
- **Real-time Monitoring:** Displays network activity as it happens.
- **Filtered Capture:** Can be modified to target specific ports (e.g., port 80 for HTTP).
- **Lightweight Design:** Uses non-persistent storage to minimize memory usage during capture.

## How to Run
1. Install Scapy:
   ```bash
   pip install scapy
