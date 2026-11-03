
#terminal #commands 

1. `pwd` : prints the path of the working/current directory . 

2.  `ls` : lists the components of the current directory .
    - `ls -al` : prints all the components (including the hidden ones )
    - hidden files start with a dot (.)

3. `find` : This command helps in locating files in the file system through the cli .
     - `find <starting_point> -name <filename`.
     - If the file exists, Linux will print the `full path` to it.
4. `uname` :
   -  use with (-a) flag to print **ALL** system info in structured layout . 
   
3. `df` : disk free , it is a command that is used to know the amount of  free and used disk storage in the computer . 
    -  `df -h` : this is used to make the usage human readable instead of long byte numbers 
    - `tmpfs` entries are temporary file systems stored in **RAM**, not on the physical disk.
    - `/run/user/114` is similar temporary storage for another system user,
4. EXTRA INFO 
-  Linux stores configuration and informational files in the `/etc` directory.
- " `os-release` "file provides details about the Linux distribution that are often clearer than those provided by the `uname` command.

3. SSH
#su #ssh
-  To connect to `ssh` use the syntax :
    `ssh username@target_machine_ip 

- Use `su` command to switch users 
- This also works out of ssh on normal bash for os . 
- Use the syntax :
    `su - username`  