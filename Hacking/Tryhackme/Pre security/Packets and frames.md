 
### Packet

- Pieces of data ( from layer 3 of osi model ).
- Contains the payload and the ip address .

### Frame 

- Encapsulation of packets with mac address .
- At the 2nd layer of the osi model .


- **Encapsulation** is the process of wrapping information over data . 

- As data in small packets , the chances of bottle necking reduces .

## Protocols 
- Packets have different structures depending upon the type of packet it is . 
- Network has standards and protocols . Without proper standardisation the internet will break .
- These standards and protocols decide how packets are handled over a network 


### IP
- A packet using the internet protocol ( IP) will have a header and that contains which will also be sent along with the packet across the network . 

#### Some notable headers 
1. **Time to live** : Tells the expiry of a packet .( Helps in eradicating lost data packets so that they don't clog up the network ) .
2. **Checksum** : This field ensures integrity for protocols such as tcp/ip . If any data is changed then this value will come different from what was expected and therefore corrupt . 
3. **Source Address** : The ip address of the device from where the packet is being sent from so that data knows , where to return to . 
4. **Destination Address** : This filed contains the data of the ip of the device the packet is sent to so that it knows where it is going . 


# Tcp / ip 

- Transmission control protocol (TCP)
- 4 layers 

- Namely 
1. Application 
2. Transport 
3. Internet 
4. Network Interface 

- Information is added to each layer of tcp layer as the packet traverses it . 
-  As already mentioned this process is called encapsulation and its reverse is called de-capsulation . 
- Tcp is connection based , it must establish a connection between the client and the server (device ) before the data is sent . 
- Because of this , tcp guarantees that data sent will we received by the other side , this is called a 3 way hand shake . 


## Encapsulation 

- There is there is a lot of info that is present in the header of the packet, which is added during encapsulation . 

### Some of the few headers are : 
1. Soruce port 
2. Destination port 
3. Source IP 
4. Destination IP 
5. Sequence number (this is given when a connection is established )
6. Acknowledgement number 
7. Checksum ( used to check integrity of data )
8. Data 
9. Flag ( tells how data should be dealth with )

## Three - way handshake 

1. SYN 
2. SYN/ACK
3. ACK
4. DATA
5. FIN
6. RST

- The syn packet is sent by the client and is used to initiate connection and synchronise 2 devices. 
- Syn/ack packet is sent by the receiving device , which confirm that the device received a syn packet . 
- The ack packet can be used either by the client or the receiver to acknowledge that a series of message has been successfully received . 
- Data is basically the info intended to transfer which is transferred after a connection is established .
- Fin is a packet used to cleanly and properly close the connection after it is completed . 
- Rst is a packet used to abruptly end a connection and is used as a last resort , to indicate that there was some problem during the process . 


#### Sequence number 

- Any data sent is given a random number sequence and is reconstructed at the receiver device using this number sequence and by incrementing 1 to the sequence . 
- Both computers must agree on the same number sequence for data to be sent in correct order .
- This order is agreed upon in 3 steps :
	1. SYN - Client: Here's my Initial Sequence Number(ISN) to SYNchronise with (0)
	2. SYN/ACK - Server: Here's my Initial Sequence Number (ISN) to SYNchronise with (5,000), and I ACKnowledge your initial number sequence (0)
	3. ACK - Client: I ACKnowledge your Initial Sequence Number (ISN) of (5,000), here is some data that is my ISN+1 (0 + 1)
- As tcp reserves system resources for a connection , it is best practice to end a connection once the objective is reached . 
	- Eg of a tcp session closing packet 
		`Fin (client to receiving )-> Ack+Fin( receiving to client ) -> Ack ( client to receiving)


# UDP 

- User datagram protocol .
- Unlike tcp ,udp is a stateless protocol . Meaning it doesnt require a constant connection between 2 devices to sent data . 
- There is no 3 way handshake nor any synchronisation . 
- Udp is faster as there are lesser checks in it . 
- Sender does'nt verify that the packet is received or not . 
- Apps control sending rate and any reliability . 
- Flexibility for real time apps where `` working > perfect packet delievery .
- Use udp when low latency matter and some data loss is acceptable . 

## Some of the few headers are : 

1. TTL ( time to live )
2. Source address 
3. Destination address 
4. Source port 
5. Destination port 
6. Data

- **TTL ( time to live )** denotes the expiration time of the packet , which ensures that if the packet gets lost somewhere in transmission , it should not clog the network , so the packet expires after some time . 


# Ports 

- The computer has 0 - 65,535 port number range . 
- Port no range of 0 - 1024 is known as the common port range . 
- To prevent confusion some major ports have been standerdized .
- For example : 

#ports 
1. ftp - 21
2. ssh - 22
3. http - 80
4. https - 443
5. smb - 445 ( server message block)
6. rdp - 3389
