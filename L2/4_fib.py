class Fibonacci:
    def __init__(self, steps):
        self.steps = steps
        self.current_step = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_step >= self.steps:
            raise StopIteration
        current_value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.current_step += 1
        return current_value

fib = Fibonacci(10)
for number in fib:
    print(number)

