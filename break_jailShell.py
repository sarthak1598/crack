
# type of command line python code that is to be supplied with single line ---> as shown below '
# the main aim of this single line code is to spawn a TTL shell from a limited reverse shell , it breaks the jailed shell 
# so , that directory can be traversed .... 

# two types of shells are tried to poped up ... 

python -c 'import pty; pty.spawn("/bin/sh")'
python -c 'import pty; pty.spawn("/bin/bash")'

echo os.system('/bin/bash')  # This command will spawn the system bash shell with breaking the jailed shell ..
