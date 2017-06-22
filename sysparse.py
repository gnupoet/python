import subprocess

mem_tmp = subprocess.check_output(["cat", "/proc/meminfo"]).split("\n"); # Split every line into dict entry                                          
del mem_tmp[-1]
print mem_tmp

i=0
while i<len(mem_tmp):                    # loop                                                                                                      
    mem_tmp[i]=mem_tmp[i].split(":");    # split dict into 2d.                                                                                       
    mem_tmp[i][1]=mem_tmp[i][1].strip(); # strip white spaces from proc file.                                                                        
    print "idx:",i,"keys:", len(mem_tmp[i]), mem_tmp[i];
    i=i+1


print dict(mem_tmp)
