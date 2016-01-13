class Tokenizer:

  def __init__(self, code_string):
    self._tokens = []

    self._pointer = 0

    self._tokenize(code_string)

  def _tokenize(self, code_string):
    # Split code by lines, then split lines by white space into tokens
    lines = code_string.splitlines()
    for x in range(len(lines)):
      self._tokens.append([])
      for token in lines[x].split():
        self._tokens[x].append(token)

  def next(self):
    if not self._tokens[0]:
      self._tokens.pop(0)
      
    return self._tokens[0].pop(0)

  def is_empty(self):
    if not self._tokens:
      return True
    else:
      for tokenlist in self._tokens:
        if not tokenlist:
          return True
    return False

  def _consume(self, _nomable=None):
    if _nomable == '$$':
      return True
    if not self._tokens:
      return True
    elif not self._tokens[0]:
      self._tokens.pop(0)

    # TODO: add current token to AST
    self._token = self._tokens[0].pop(0)

  def append(self, code_string):
    pass
