class Fibonacci:
    def F(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            print("call")
            return self.F(n - 1) + self.F(n - 2)

    def fact(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return self.fact(n - 1) * n
