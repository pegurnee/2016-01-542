class Tokenizer:

  def __init__(self, code_string,
    stored_delimiters=['+','-','/','*','(',')'],
    unstored_delimiters=['\n',' ']):
    self._SAVERS = stored_delimiters
    self._NOSAVE = unstored_delimiters

    self._tokens = []

    self._tokenize(code_string)

  def __iter__(self):
    return self

  def __next__(self):
    return self.next()

  def _tokenize(self, code_string):
    string_content = code_string

    while self._has_token(string_content):
      token, string_content = self._get_token(string_content)
      self._tokens.append(token)
    '''
    # Split code by lines, then split lines by white space into tokens
    lines = code_string.splitlines()
    for x in range(len(lines)):
      self._tokens.append([])
      for token in lines[x].split():
        self._tokens[x].append(token)
    '''

  def _has_token(self, code_string):
    if not code_string:
      return False
    else:
      return True

  def _get_token(self, code_string):
    a = code_string.find(' ')
    b = code_string.find('\n')
    if a < 0:
      a = b
    if b < 0:
      b = a
    index = a if a < b else b
    if index < 0:
      index = len(code_string)

    return code_string[:index], code_string[index + 1:]

  def append(self, code_string):
    self._tokenize(code_string)

  def next(self):
    if not self._tokens[0]:
      self._tokens.pop(0)

    return self._tokens.pop(0)

  def is_empty(self):
    if not self._tokens:
      return True
    return False
