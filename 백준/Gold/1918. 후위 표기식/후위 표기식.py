class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else:
            print("stack overflow")

    def pop(self):
        if not self.isEmpty():
            item = self.array[self.top]
            self.top -= 1
            return item
        else:
            print("stack underflow")

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print("stack underflow")

    def __str__(self):
        return str(self.array[0:self.top + 1])

def precedence(op):
    if (op == '(' or op == ')'):
        return 0
    elif (op == '+' or op == '-'):
        return 1
    elif (op == '*' or op == '/'):
        return 2
    else:
        return -1


def Infix2Postfix(expr):
    s = ArrayStack(100)
    output = []

    for term in expr:
        if term == '(':
            s.push(term)

        elif term == ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)

        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if (precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)
        else:
            output.append(term)
    while not s.isEmpty():
        output.append(s.pop())
    return output
a = list(input())
postfix1 = Infix2Postfix(a)
for i in postfix1:
    print(i,end="")