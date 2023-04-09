class ExtendedStack(list):
    def sum(self):
        if len(self) < 2:
            return
        x = self.pop() + self.pop()
        self.append(x)
    def sub(self):
        if len(self) < 2:
            return
        x = self.pop() - self.pop()
        self.append(x)
    def mul(self):
        if len(self) < 2:
            return
        x = self.pop() * self.pop()
        self.append(x)
    def div(self):
        if len(self) < 2 or self[-2] == 0:
            return
        x = self.pop() // self.pop()
        self.append(x)