
#windows #cli #basics 

## Where am i ?

- You can use the `cd`command to see where you are in the command prompt 

## Whats is around me ?
-  You can use the `dir` command to list the files and folders present in the current directory .
#hiddenfiles
- To see hidden file use : `dir /a` .
#locatefile
- To locate a file use : `dir /s filename.txt` .
- The `/s` flag tells Windows to search **all subfolders** starting from your current directory and show you the full path if the file exists.

## Print file output
- Now read the contents of the file using: `type task_brief.txt`. This will print the contents of the file directly in the command prompt .

## Who am i ?
- You can use the `whoami` cmd to check what user you are logged in as.
- Every windows machine has a name , to see the computers name run:  `hostname` .

## For the os details 
-  Use : `systeminfo` to get the info about the os . 

## How is the machine connected to the net 
-  Use `ipconfig` to see details about network connection of the system .
