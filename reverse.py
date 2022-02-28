# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 2: Stacks & Queues
import reverse_test
from Queue import Queue
from Stack import Stack

# Return a new queue in reverse order
# Hint: can use a stack to help

def reverse(q_orig):
    q_new = Queue()
    new_stack = Stack()
    print("original queue", q_orig)
    while (not q_orig.is_empty()):
        new_stack.push(q_orig.deq())
    while (not new_stack.is_empty()):
        q_new.enq(new_stack.pop())
    return q_new

def main():
    reverse(Queue([l for l in "Professor Hill"])).print()
    reverse(Queue([l for l in "hello"])).print()
    reverse(Queue(list(range(1, 5)))).print()
    reverse(Queue([])).print()
    reverse(Queue([0])).print()
    reverse(Queue(list(range(0, 101, 5)))).print()
    reverse(Queue(list(range(1, -10, -1)))).print()
    reverse(Queue([int(i) for i in "23762304"])).print()
    reverse(Queue(["a"])).print()
    reverse(Queue([-5])).print()
    reverse(Queue(list(range(-5, 6)))).print()

# Don't run main on import
if __name__ == "__main__":
    main()