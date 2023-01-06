class Monkey:
    def __init__(self, name):
        self.name = name
        self.things = list()
        self.operation = ''
        self.testDivisor = int()
        self.true = int()
        self.false = int()
        self.inspect_count = 0
    
    def throw_next(self):
        self.inspect_count += 1
        if self.things:
            old = int(self.things.pop(0))
            new = eval(self.operation)
            worry = new // 3
#            worry = new
            if worry % self.testDivisor == 0:
                return [self.true, worry]
            else:
                return [self.false, worry]
        else: 
            return None

    def add_thing(self, thing):
        self.things.append(thing)

    def add_things(self, array):
        self.things = array

    def add_operation(self, input):
        self.operation = input

    def add_divisor(self, input):
        self.testDivisor = int(input)

    def add_true(self, input):
        self.true = int(input)

    def add_false(self, input):
        self.false = int(input)

    def add_name(self, input):
        self.name = input

    def __repr__(self) -> str:
        return "Monkey " + str(self.name) + " items: " + str(self.things) + '\n'
    
