from multiprocessing import Process
import os
#go to activity moniotr to seee processes

def square_numbers():
    for i in range(1000):
        result = i * i



processes = []
num_processes = os.cpu_count()

# create processes and asign a function for each process
for i in range(num_processes):
    process = Process(target=square_numbers)
    processes.append(process)

# start all processes
for process in processes:
    process.start()


# wait for all processes to finish
# block the main thread until these processes are finished
for process in processes:
    process.join()

for process in processes:
    process.close()

   
        
    
