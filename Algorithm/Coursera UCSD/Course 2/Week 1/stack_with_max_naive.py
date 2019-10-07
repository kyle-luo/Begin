#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.track_stack = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.track_stack) == 0:
            self.track_stack.append(a)
        else:
            if a >= self.track_stack[-1]:
                self.track_stack.append(a)
            else:
                self.track_stack.append(self.track_stack[-1])

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.track_stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.track_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()
    count_max = {}

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
