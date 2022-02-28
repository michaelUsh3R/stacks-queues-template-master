# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue
def dec_to_bin(x):
    binary = ""
    while x != 0:
        remain = x % 2
        x = x // 2
        binary = str(remain) + binary
    return binary

def generate_binary_numbers(N):
    binaryQueue = Queue()
    if (N>=1):
        for i in range(1,N+1):
            binaryQueue.enq(dec_to_bin(i))
    return binaryQueue

def main():
    generate_binary_numbers(8).print()

# Don't run main on import
if __name__ == "__main__":
    main()

