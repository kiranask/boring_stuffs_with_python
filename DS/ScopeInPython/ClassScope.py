class Test:
    def print_a(self):
        self.a = 100

    def print_b(self):
        print(self.a)
t = Test()
t.print_a()
t.print_b()