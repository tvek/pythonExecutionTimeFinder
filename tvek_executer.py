import sys,time,os

prgm_name = sys.argv[1]
start_time = time.time()
print("\nTVEK Execution Time Finder\n\nProgram Name:"+prgm_name+"\n-------------------------------\nOutput:\n")
os.system("python "+prgm_name)
end_time = time.time()
exec_time = end_time-start_time
print("\n-------------------------------\nExecution Time : "+str(exec_time)+"\n'"+prgm_name+"' has executed successfully.");
