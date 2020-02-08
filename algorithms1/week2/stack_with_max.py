"""
Stack with max. Create a data structure that efficiently supports the stack operations (push and pop) and also a return-the-maximum operation.
Assume the elements are reals numbers so that you can compare them.
"""


class StackWithMax:
    def __init__(self, size=10):
        self.storage = []
        self.maxes = []
        self.MAX_SIZE = size
        self.max = None

    def get_max(self):
        return self.max

    def push(self, val):
        if len(self.storage) == self.MAX_SIZE:
            raise Exception(f"Stack FULL. Max size is: {self.MAX_SIZE}")
        self.storage.append(val)

        if self.max is None:
            self.maxes.append(val)
            self.max = val
        else:
            max_val = max(val, self.max)
            if max_val > self.max:
                self.maxes.append(max_val)
                self.max = max_val

    def pop(self):
        return_val = self.storage.pop()
        if return_val == self.max:
            # get rid of old max
            self.maxes.pop()

            if len(self.storage) >= 1:
                # 2nd max becomes new max
                self.max = self.maxes.pop()
            else:
                # empty list
                self.max = None
        return return_val



s = StackWithMax()
for i in range(10):
    s.push(i)

print(s.max)
print(s.pop())
print(s.max)
