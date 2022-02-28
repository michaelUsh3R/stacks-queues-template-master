# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

def count_longest(queue):
    maxCount = 0
    currentCount = 1

    while(not queue.is_empty()):
        nextElement = queue.deq()
        currentElement = queue.front()

        if nextElement == currentElement:
            currentCount += 1
        elif nextElement != currentElement:
            currentCount = 1
        if currentCount > maxCount:
            maxCount = currentCount
    return maxCount

def main():
    print(count_longest(Queue([l for l in "oooohhhhhaaeeeeee"])))
    print(count_longest(Queue([l for l in "hello"])))
    print(count_longest(Queue([l for l in "m" * 5])))
    print(count_longest(Queue([l for l in "hooop"])))
    print(count_longest(Queue([l for l in "oooohh"])))
    print(count_longest(Queue([l for l in "oooohheeee"])))
    print(count_longest(Queue([l for l in "oooohheeeee"])))
    print(count_longest(Queue([ ])))
    print(count_longest(Queue([l for l in "m"])))
    print(count_longest(Queue([l for l in "+__--___----__--_+"])))


if __name__ == "__main__":
    main()