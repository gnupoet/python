import subprocess

mem_tmp = subprocess.check_output(["cat", "/proc/meminfo"]).split("\n"); # Split every line into dict entry
del mem_tmp[-1] # Remove the last entry which is faulty for some reason

i=0
while i<len(mem_tmp):                    # loop
    mem_tmp[i]=mem_tmp[i].split(":");    # split dict into 2d.
    mem_tmp[i][1]=mem_tmp[i][1].strip(); # strip white spaces from proc file.
    print "idx:",i,mem_tmp[i][0],"=>",mem_tmp[i][1];
    i=i+1


print dict(mem_tmp)
