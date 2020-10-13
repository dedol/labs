# Strategy pattern example

class Uppercase:
    def do_it(self, string):
        return string.upper()


class Lowercase:
    def do_it(self, string):
        return string.lower()


class Printer:
    def set_strategy(self, strategy):
        self.strategy = strategy
        
    def do_it(self, string):
        print(self.strategy.do_it(string))

        
pr = Printer()

pr.set_strategy(Uppercase())
pr.do_it("TEST STRING test string")

pr.set_strategy(Lowercase())
pr.do_it("TEST STRING test string")
