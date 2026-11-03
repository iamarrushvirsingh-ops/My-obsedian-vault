
 (**O**pen **S**ystems **I**nterconnection Model)
 
- It provides a framework that decides how all network devices sends / receives and interprets data .  
- It helps communicate between different devices meant for different functions . 

- The layers of OSI model are :

1. Physical 
2. Data link layer
3. Network
4. Transport 
5. Session
6. Presentation
7. Application


- The process of adding information to data (packets) is called encapsulation .
- This happens at every layer of the osi model , as needed .

## Physical layer

-  Devices use electrical signals to transfer data between each other in a binary numbering system (1's and 0's).
- Ex: ethernet cables connecting different devices over the internet .


## Data link layer 

- The data link layer focuses on the physical addressing of the transmission.
- It receives a packet from the network layer (including the IP address for the remote computer) and adds in the physical **MAC** (Media Access Control) address of the receiving endpoint.
- Inside every network-enabled computer is a **N**etwork **I**nterface Card (**NIC**) which comes with a unique MAC address to identify it.


## Network layer

- Routing simply determines the most optimal path in which these chunks of data should be sent.
- Some protocols at this layer determine the most optimal path that data should take to reach a device . 
-  These protocols include **OSPF** (**O**pen **S**hortest **P**ath **F**irst) and **RIP** (**R**outing **I**nformation **P**rotocol).
- They concider : 
1. The shortest path 
2. The most reliable path
3. The fastest physical connection . 
- At this layer , everything is dealt with a IP address .
- Devices capable of delivering packets using IP address are know as **level 3** devices . 

## Transport 

- This layer uses tcp /udp and all . 
- Transmission control protocol ( error checking / slow / continious constant session)
- User datagram protocol ( no error checking / fast . can break sessions)
- Udp is used for things like video playing or gaming , where a loss of few pixels ( data packets )  will not be such a problem .
- Tcp is used for tasks that need accuracy and assurance , like sending emaills , and transfiring files .

## Session 

- This layer is responsible for connecting and maintaining a session with other computers for which the data is destined . 
- The session layer is also responsible for closing the session , if the task is done or the session hasnt been used in a while .
- As long the connection is established the session also remains . 
- A data cannot travel in 2 different sessions , if the same file has to be sent to 2 different endpoints ,then 2 different sessions will be made and the data will be sent to the 2 sessions independent of each other . 


## Presentation layer 

- This layer is responsible for translating different types of data in a generalised format , that is used for it t be sent over the internet / network .
- Security features like https encryption also happen at this layer 
- This layer deals with everything related to the presentation of data . 


## Application layer 

- The application layer consists of the protocols and rules specifying how users should interact with the application  .
- The gui comes under this layer  .

