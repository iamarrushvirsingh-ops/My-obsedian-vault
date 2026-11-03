	- Install docker
- pull and run images / use simple command to to download and start containers.
- map container ports to your host ports so that you can access web applications in your web browser . 
- check which container are running 





## Containerisation 

- Containerisation is the process of packaging an application and the necessary resources (such as libraries and packages) required into one package named a container.
- The process of packaging applications together makes applications considerably portable and hassle-free to run.
- So lets say a developer wants to fix or understand why and how a bug is occuring in a system , then the not only need the bugs info , they also need the info of the environment in which the bug occured .
- This is where containerisation helps , it captures the environment , so that the developer can replicate the environment and pinpoint if it was the application that had a problem or was it the environment .
- Docker lets you run many containers in isolation , so lets say one of your containers get compromised that wont affect the host operating system or other containers . 
- Containerisation platforms make use of the “namespace” feature of the kernel, which is a feature used so that processes can access resources of the operating system without being able to interact with other processes.
- The Docker Engine is essentially an API that runs on the host operating system, which communicates between the operating system and containers to access the system’s hardware (such as CPU, RAM, networking and disk)
- What docker engine can do : 
	- Tranfer of files between containers and os .
	- Export and import applications (images)
	- Connecting containers together . 

## Basic benefits of docker 

- Docker is free .
- Docker is compatible .
- Docker is efficient and minimal .
- Docker is easy to get started with ( good documentation)
- Docker is minimal ( with reduce in installation of unnecessary tools and applications in a env like text editor , etc.) This also helps in reducing the attack surface and acts as a add on to security .

## How containerisation works 

- Namespaces segregates system resources like files , memory , storage and other name spaces .
- Every process runnning will be assigned 2 things 
	- Namespace 
	- (PID) process identifier 
- Processes can only see processes that are in the same name-space .

#howasystemstarts #pid 
- When a system starts by a boot-loader a process is started , which is named PID 0 , this process starts the kernel and creates the first user space PID 1 and then it goes idle .
- PID 1 it takes over the system and starts all necessary processes and also is responsible for scrapping zombie processes .
- In containerisation a new name space is used for the container , in that namespace the first prcoess is named PID 1 for that name space . 
- It so happens that sometimes these isolated namespace interact with the host os / namespace , causing the isolation to be a little .... less secure . 
- `ps aux` is the command in linux/ docker to get a snapshot of running processes in the system.



