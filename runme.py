import subprocess
process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, err = process.communicate("g++ -fprofile-arcs -ftest-coverage -fPIC -O0" + sys.argv[1] + "-o exe")
out, err = process.communicate("/.exe < " + sys.argv[2])
out, err = process.communicate("gcovr -r .")
print out
out, err = process.communicate("gcovr -r . --branches")
print out