
#Components 
- Motherboard : The skeleton and nerves .
- RAM: Short term memory .
- GPU: Visual cortex .
- CPU: The brain .
- PSU: Heart and lungs .
- HDD + SSD : Long term memory .

#Motherboard 
 - The motherboard connects and holds all different components in place and connects them .

#CPU
- A cpu does mathematical operations , and logical operations .
- Modern CPUs have multiple cores that handle instructions in parallel. 
- The CPU connects to the motherboard via the CPU socket.

#RAM
- Ram holds data that the CPU needs quick access to.
- RAM is volatile: when power is lost, all contents are gone.
-  Modern RAM modules use technologies like DDR5 or DDR6 for increased speed and performance.


#STORAGE #SSD #HDD
- HDDs use older technology with moving parts, limiting performance. 
- SSDs have no moving parts and use memory chips, allowing much faster speeds.
- HDDs remain popular for their large capacity at low cost.
- Storage connects via SATA cables or PCI Express slots

#Networkadapter
-  A network adapter lets computers communicate with other systems.
- Network adapters come in wireless and wired variants. 
- Often they're embedded in the motherboard, but they can also be added as expansion cards. 
- Network cards typically connect via PCI Express ports.

#PSU
- A PSU supplies energy to all system components.
- The PSU takes power from an outlet and distributes it via various connectors like the main motherboard connector and Molex connectors.
- If components need more power than the PSU can provide, the system will fail.

#Graphicscard
- The graphics card receives information from the operating system and programs, then outputs processed visual data to a monitor.
- Graphics cards connect to PCI Express slots on the motherboard.

#howdoesacomputerstart


**Step 1: Press the Power Button**  
When we press the power button on our computer system, a signal is sent to the PSU to allow power to flow. Imagine our body being powered off when we sleep. Once we wake up and receive oxygen, our body starts pumping blood and boots up.


**Step 2: Firmware starts**  #UEFI #BIOS
Continuing our analogy from step 1, once the body has started up, our core components are up and running, but our brain is not yet conscious. Like our bodies, a computer system contains firmware that allows all its components to start up. The central system that manages this is called the Unified Extensible Firmware Interface (UEFI).

**Note: We will often see the term BIOS mentioned instead of UEFI. BIOS does the same as UEFI, but has mainly been replaced by UEFI**

**Step 3: Power-On Self Test**   #POST
Now that our body is up and running, it is time to test if everything is functioning as it should. If something isn't, there will be some alarm signals. One of the routines that the UEFI loads is the Power-On Self Test, which tests if every required component is present, configured correctly, and functioning.

**Step 4: Select Boot Device**  
Once our body is up and running, configured correctly and fully functional, our system searches for the location of our bootup routine to start our consciousness. In our computer system the UEFI holds an ordered list which prioritizes on which device to look first for the boot up routine for the Operating System.

**Step 5: Initiate Bootloader**  
Now that our system knows the part of our brain where our consciousness is located, it initiates the "load routine" to start it. Our computer systems follow a similar process: On the selected boot device, the bootloader is initiated. This bootloader transfers the Operating System from the selected boot device to the Random Access Memory. Once the OS is transferred, the UEFI gives control over the different components to the OS.


