class Interpreter

  def __init__(self, codeString):
    self.values = []
    self.tokens = []
    lines = codeString.splitlines()
    for x in range(len(lines)):
      for token in lines[x].split():
        tokens[x].append(token)

  def match(self, expected, actual):
    if expected == actual:
      self.consume(actual)
    else:
      return parse_error

  def consume(self, correctToken):
    pass

  def program(self, arg):
    pass
