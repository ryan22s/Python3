class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def __repr__(self):
        if self.value == 1 or self.value > 10:
            self.value == str(self.value)
        return f"{self.suite}", self.value


testit = Card('boner', 3433)
print(testit)

