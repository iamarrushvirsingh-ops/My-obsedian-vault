
# Port forwarding

- Routers are used to configure port forwarding .
	- Port forwarding opens specific ports . 
- Without port forwarding , devices such as web servers are only available to devices within the same direct network . 
- Requests from other networks can be entertained , the other network sends a request through a public ip on the designated port , if the port is correct the response is sent back . 
- In simple words port forwarding is directing incoming network traffic on a specific port of a server or device on the receivers network . 
- The router has a list that you configure which contains ports and their related private ip . This way any packet that comes with a destination port X , will be routed to the private ip related to the specific port in the table provided in the router by you. 

# FireWalls 

- A firewall is a device on the network that decides which traffic is allowed to enter or exit . 
-  A firewall is reponsible for permiting or denying entry / exit to traffic based on : 
1. Where it is coming from ?
2. Where it is going ?
3. What port is it for ?
4. What protocol is it using ?

- Firewalls perform packet inspection to answer these questions . 
- Firewall comes in many shapes and sizes , big and small , etc . 
- They can be majorly divided into 2 categories : 
1. Stateful
2. Stateless

## Stateful 

- This firewall monitors the entire connection , rather than inspecting individual packets . 
- This firewall determines the behaviour of the device based on the entire connection .
- This type of firewall consumes more resources than stateless firewall as the decision making is dynamic .
- If a connection from a host is bad , it will block the entire device .
## Stateless 

- This type of firewall uses a static set of rules to determine whether or not the individual packet is acceptable or not . 
- This firewall uses much less resources but are more dumber . 
- However these firewalls are useful when receiving a large amount of traffic from a set of hosts ( ddos attack ) .

# VPNs

- Virtual private network 
- Using this 2 devices on different networks can  commuicate using a dedicated path between each other over the internet ( tunnel ).
- Vpns are not just proxy servers connections with a tunnel . 
- They are something that run on the OS level and proxy servers only run on application level , this way proxy servers tunnel traffic only for a application , but vpns tunnel traffic for the whole system . 
- It helps networks from different physical and geographical locations to be connected . 
- It also helps in privacy as data transfered through a vpn is encrypted . 
- It helps you hide your data from your isp .

## VPN technologies 

### **PPP  
- This technology is used by PPTP .
- It is used for authentication and encryption of data .
- VPNs works by using a private key and public certificate  .
- This technology is non-routable . (cannot leave the network itself )

### PPTP 
- The Point to Point Tunneling Protocol .
- This is the technology that allows the data from PPP to travel and leave a network . 
- PPTP is easy to set up and is supported by most devices . 
- But it is weakly encrypted in comparision to alternatives . 

### IPSec 
- Internet protocol security encrypts data using existing IP framework .
- Ipsec is difficult to set up in comparision to alternatives
- However once set-uped , it offers very strong encryption and is supported by many devices . 


# LAN networks 

- A router is a device used to connect networks and pass data between them . 
- Routing operates at the layer 3 of the OSI model . 
- 