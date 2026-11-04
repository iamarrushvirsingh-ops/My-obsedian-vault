- Domain name system .

# TLD

- Top level domain . 
- There are 2 types of TLD :
	1. gTLD (Generic top level domain )
	2. ccTLD(Country code top level domain )
- gTLD is used to  denote domain names type like , `.com` and `.gov` to specify commerical and govt domains respectively . 
- And ccTLD were used for geographical purposes . For example `.ca` in canada and so on . 

# Second level domain 

- Like for example concider `tryhackme.com`
	- So the `.com` is the TLD . 
	- And the `tryhackme` is the second level domain .
- Rules for domain names
	- The second-level domain is limited to 63 characters + the TLD and can only use a-z 0-9 and hyphens (cannot start or end with hyphens or have consecutive hyphens).
- The rules to create a subdomain is same as for a main domian , you just have to seperate sub domains using `.` .
- And the character limits for a full domain name with multiple subdomains is 253 or less . 


# Record types 

## A record 
- These records resolve to IPv4 address.

## AAAA Record 
- These records resolve to IPv6 address . 

## CNAME Record 
- Its like a redirecting route .
- Lets just say that you want the user to be directed to your website , even if they aren't mentioning the exact domain word by word . 
- Like instead of `tryhackme.com` , a person searches for `www.tryhackme.com` . 
- So CNAME record ensures this only , that the person , is redirected to the right site event after typing a other know name of the domain .
- CNAME sends the orginally linked domain name to the user and then another DNS request is made for that domain name . 
- This makes sure that the provider doesn't has to bbuy every similar sounding domain name and set up a website at 6 different places with 6 different names . 

## MX Record
- These records holds the address of the server which handles the emails of the domain you are querying . 
- These records also holds a priority flag that tells the user in which order to try the server if the main server goes does and you want to send a mail . 

## TXT Record 
- These are free text fields where any text based data can be stored . 
- They have multiple uses . 
- The most common one is , the list of servers who have the authority to send emails , on behalf of the domain . 
- Can help in prevent spoofing and scams . 
- They can also be used to verify ownership of the domain name when singing up for third party services . 



# Workflow 
- What happens when a request is made ?
- When you first make a request the computer checks if you have recently made the request and if the domain name is in the computers dns cache . 
- If not then a request is made to your Recursive DNS server . 
- A recursive DNS server is usually provided by your isp provider but you can choose your own as well . 
- This server has its own cache , which is searched first if a request is recieved to the server , if there are no matches then the  internets Root DNS server is sent a request . 
- The internets root dns server redirects you to the correct TLD ( top level domain ) server for your request . 
- The TLD server holds records as to where to find the authoritative server to answer your request . 
- The authoritative server is also known as the nameserver of that domain . 
- You will often find multiple nameservers for a domain , in case one goes down . 
- An authoritative server is responsible for storing DNS records for a particular domain name and is where you update any changes in the DNS records .  
-  Every DNS record comes with a TTL (time to live ) which is measured in seconds . 
