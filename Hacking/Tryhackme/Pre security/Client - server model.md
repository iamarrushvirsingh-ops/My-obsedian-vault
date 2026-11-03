- Basics about networking .



#Service #Clinet #Server 

- Service is the provision offering that you are trying to avail .
- Client is the browser making the request ( request of service ) .
- Server is the thing which we make a request to for the service .


#Request and #Response 

- A clients sends a request asking for data/service.
-  A server sends a response replying to the request . 

#Protocol 
 - A protocol defines how a client can communicate with a server. This definition includes:

- Which commands do the client and server understand. (GET)
- How a request is structured.
- E.g., first the command and then the order.
- What syntax is used.
- What response should be given to which type of request.

#Port

- A port is used to identify a specific service running on a system. 
- When a client wants to access a service on a server, it must connect using the correct port.\

 #httpcommands
- In the main specifications that define HTTP (also called Request for Comments, or RFC documents), there are 9 core commands. 
- In HTTP lingo, we use the term method instead of command. Below you can see an overview of these methods:
- GET
- POST
- PUT
- DELETE
- PATCH
- HEAD
- OPTIONS
- CONNECT
- TRACE

#Inspect 
- We can see more information about our GET request. We won't go into much detail, but let's have a look at some of these fields.
-  **Scheme**: Tells us which protocol was used: HTTP or HTTPS.
- **Host**: Tells us the name of the host we request resources from.
- **Filename**: Indicates which file we requested from the host. In our request, this is "/", which actually translates to "index.html".
- **Address**: Displays the IP address where the website is hosted. In our example, we are hosting the website on the same device. That's why the address 127.0.0.1 is shown.
- **Status**: This field indicates whether the request was successful. In our example, we received a "200 OK" status, which means that the request was successful.
  
  #Response 
- When a request is sent, we will get a response from the server. 
- The response is divided into two parts: the response header and the response body. 
- The response header contains metadata about the response, while the response body contains the requested content. ( #metadata)


