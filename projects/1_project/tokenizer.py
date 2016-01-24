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
      multiple, token, string_content = self._get_token(string_content)
      if token:
        if multiple:
          for the_token in token:
            if the_token:
              self._tokens.append(the_token)
        else:
          self._tokens.append(token)

  def _has_token(self, code_string):
    if not code_string:
      return False
    else:
      return True

  def _get_token(self, code_string):
    token_loc = 0
    while token_loc < len(code_string):
      if code_string[token_loc] in self._NOSAVE:
        break
      else:
        curr_string = code_string[:token_loc + 1]
        for saver in self._SAVERS:
          if curr_string[-len(saver):] == saver:
            return True, [curr_string[:-len(saver)], curr_string[-len(saver):]], code_string[token_loc + 1:]
        else:
          token_loc += 1
    return False, code_string[:token_loc], code_string[token_loc + 1:]

  def append(self, code_string):
    self._tokenize(code_string)

  def next(self):
    if not self._tokens:
      return None
    if not self._tokens[0]:
      self._tokens.pop(0)

    return self._tokens.pop(0)

  def is_empty(self):
    if not self._tokens:
      return True
    return False
