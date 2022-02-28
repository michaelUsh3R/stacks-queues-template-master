# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 2: Stacks & Queues

from Stack import Stack

# Returns True if the braces match,
# & False otherwise

def matcher(expr):
  stack = []
  for c in expr:
    if c in '[({':
      stack.append(c)
    elif c in '])}':
      if len(stack) == 0:
        return False
      if '])}'.index(c) != '[({'.index(stack.pop()):
        return False
  return len(stack) == 0

def main():
    print("matcher: ", matcher("[ ]"))
    print("matcher: ", matcher("{ }"))
    print("matcher: ", matcher("hello"))
    print("matcher: ", matcher("(45 + 36) - 5"))
    print("matcher: ", matcher("[()]"))
    print("matcher: ", matcher("{[()]}"))
    print("matcher: ", matcher("{ () [ [] ( {} ) ] }"))
    print("matcher: ", matcher("{[()]} [ ] ( ) ([{}]) { () [ [] ( {} ) ] } ( {[()] [] } {} )"))



# Don't run main on import
if __name__ == "__main__":
    main()

