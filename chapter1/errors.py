class IllegalCarError(Exception):

    def __init__(self, name, diff):
        self.name = name
        self.diff = diff

    def __str__(self):
        if self.diff > 0:
            return f'{self.name} norm exceeded by {self.diff}'
        else:
            return f'{self.name} norm found too small by {abs(self.diff)}'
