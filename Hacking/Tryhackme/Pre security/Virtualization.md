
#Virtualization 
- Virtualization helped in using a single physical server for multiple services .
- A virtualization layer, called a **hypervisor**, was introduced to act as a referee between lab machines and allow each virtual computer to behave independently, like a physical computer.

#Container 
- A **container** is a lightweight, isolated environment that runs a single application and all the necessary components to support it.
- Containers behave like small, self-contained spaces because:

- They package the application and its dependencies (libraries, tools, versions).
- They share the host’s operating system, so they start almost instantly.
- They remain isolated from each other, so a misbehaving container doesn’t affect the others.
- They can run consistently on any machine, making them perfect for development, testing, and scalable deployments.

- The easiest way to deploy containers in a VM is using Docker.  
- Docker is an open-source software platform that simplifies the process of building, deploying, and running applications using containerization.


- Hypervisors have two main types of implementation, each of which is used for specific scenarios, from home labs to large data centers:

- **Type 1** hypervisors run directly on the physical hardware, making them fast, efficient, and ideal for servers and professional environments.
- **Type 2** hypervisors run within an existing operating system, making them easier to install and ideal for learning, testing, or small setups.


- **Virtualization:** Enables a single physical computer to act like multiple separate computers.
- **Hypervisor:** The “manager” software that makes and runs the virtual computers.
- **Lab Machine (VM):** A whole virtual computer inside the real one, with its own system.
- **Container:** A small, isolated box for one app that shares the same system as the host.
- **Container Images:** A pre-packed recipe/template used to create containers.
- **Network Ports:** Special numbered entry points that apps use to talk over the network.

