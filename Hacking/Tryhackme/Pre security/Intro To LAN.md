
- There are many network design , these design are called topologies 
1. Star topology
2. Bus topology
3. Ring topology

## Star topology 

 -  Devices are individually connected via a central networking device such as a switch or hub .
 - Its costly due to the excessive wiring
 - But its easily scaleable . 

## Bus topology

-  This type of connection relies upon a single connection which is known as the backbone cable . 
- It is prone to bottle neck and multiple requests can be a problem 
- If the main backbone cable is damaged , the whole operation fails .

## Ring topology 

- It forms a network of devices in a circle .
- For any request , the packets need to travel in the circle-circuit until it reaches the intended device . 
- Its cons is that the packet direction is unidirectional and if at any point the cable is damaged , the whole operation stops .

## Sub-netting (intro)

- Sub-netting is the term given to splitting up a network into smaller, miniature networks within itself.
- Sub-netting is achieved by splitting up the number of hosts that can fit within the network, represented by a number called a subnet mask.
- An IP address is made up of four sections called octets. 
- The same goes for a subnet mask which is also represented as a number of four bytes (32 bits), ranging from 0 to 255 (0-255).
- Subnets use IP addresses in three different ways:
    - Identify the network address.
    - Identify the host address.
    - Identify the default gateway.

- Network address : Used to identify networks existence .
- Host address : An ip add used to identify a device on the subnet.
- Default Gateway : The default gateway address is a special address assigned to a device on the network that is capable of sending information to another network.

## ARP 

- The **A**ddress **R**esolution **P**rotocol or **ARP** for short, is the technology that is responsible for allowing devices to identify themselves on a network.
- Simply, ARP allows a device to associate its MAC address with an IP address on the network
-  Each device on a network will keep a log of the MAC addresses associated with other devices.
- When a device wants to communicate on a network , it can send a broadcast , asking for the mac of a deivce associated with a specefic ip .
- This is done using ARP . 
- After this is done , the mac is saved and associated ip in the machines logs so it does'nt always has to send a broadcast msg .
  
  - Each device within a network has a ledger to store information on, which is called a cache.
  - In the context of ARP, this cache stores the identifiers of other devices on the network.

- In order to map these two identifiers together (IP address and MAC address), ARP sends two types of messages:

1. **ARP Request**
2. **ARP Reply**

- In a arp request , the mac of the device associated with a specefic ip is asked .
- The device whose ip it is , responds with a arp reply where he sends his mac addr . 
-  The requesting device can now remember this mapping and store it in its **ARP cache** for future use.

## DHCP

- `DHCP discovery `, in this the device sends a request to see if there are any dhcp servers on the network.
- `DHCP offer` is basically a offer ip , for the device to use . 
- `DHCP request` , is sent to confirm that the device wants/would like to use the offered ip .
- `DHCP ack `, is used to acknowledge that the whole thing has been done and now you can use your ip . 
- 