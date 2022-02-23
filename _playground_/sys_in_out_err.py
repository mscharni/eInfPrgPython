import sys
 
stdin_fileno = sys.stdin
stdout_fileno = sys.stdout
stderr_fileno = sys.stderr

# Redirect sys.stdout to the file
sys.stdout = open('Output.txt', 'w')

# Keeps reading from stdin and quits only if the word 'exit' is there
# This loop, by default does not terminate, since stdin is open
for line in stdin_fileno:
    # Remove trailing newline characters using strip()
    if 'exit' == line.strip():
        print('Found exit.')
        break
    else:
        print('Message from sys.stdin: ---> {} <---'.format(line))
        

 
sample_input = ['Hi', 'Hello from AskPython', 'Break']
 
for ip in sample_input:
    # Prints to stdout
    stdout_fileno.write(ip + '\n')
    
for ip in sample_input:
    # Prints to stdout
    stdout_fileno.write(ip + '\n')
    # Tries to add an Integer with string. Raises an exception
    try:
        ip = ip + 100
    # Catch all exceptions
    except:
        stderr_fileno.write('Exception Occurred!\n')
