# Multi-Threading programming - run functions simultaneously
# So we can design our application such that the functions independent of each other can run on threads in parallel

# Process: An instance of computer program that is being executed

# Thread
#     - The smallest unit of Processing
#     - An entity within a process that can scheduled for execution
#     - Sequence of instructions within a program that can be executed independently
#     - A subset of a Process
#     - Multiple threads can exist within a Process
#     - Each thread has its own Register Set and Local Variables (stored in Stack)
#     - All threads of a Process share global variables (stored in Heap) and the Program Code

# Context Switching :
#     - In a single core CPU, frequent switching betweens threads is taken place
#     - They are switched so frequently that they appear to be running simultaneously
#     - Thus Multi Tasking is achieved

# Multi-Threading in Python
#     - The 'threading' Module offers a very simple and intuitive API for spawning multiple threads in a program
#     - The main thread will be the program itself. Others are its child
#     - The main thread should wait for the child threads to execute completely
#     - When the main execution completes before child, they become orphan threads, gets removed from System by OS

import threading
import time


def get_squared(pNum):
    for n in range(pNum):
        time.sleep(1)
        print("{0} - {1} : {2}".format(get_squared.__name__, n, pow(n, 2)))


def get_cubed(pNum):
    for n in range(pNum):
        time.sleep(3)
        print("{0} - {1} : {2}".format(get_cubed.__name__, n, pow(n, 3)))


def main_thread():
    # Create two threads
    thread1 = threading.Thread(target=get_squared, args=(12,))
    thread2 = threading.Thread(target=get_cubed, args=(5,))

    # Start running them
    thread1.start()
    thread2.start()

    # Wait until the threads are completely executed
    thread1.join()
    thread2.join()

    print("Main Thread completed its execution")


main_thread()

