class Interpreter

  def __init__(self, code_string):
    self._token = None
    self._tokens = []

    # Split code by lines, then split lines by white space into tokens
    lines = code_string.splitlines()
    for x in range(len(lines)):
      for token in lines[x].split():
        self._tokens[x].append(token)

  def _match(self, expected):
    if expected == self._token:
      self.consume(self._token)
    else:
      return parse_error

  def consume(self, arg):
    if not self._tokens:
      return True
    elif not self._tokens[0]:
      self._tokens.pop(0)

    # TODO: add current token to AST
    self._token = self._tokens[0].pop(0)

  def _skip(self):
    pass

  def program(self):
    if self._token in ['read', 'write', '$$']:
      self._stmt_list()
      self._match('$$')
    elif:  # TODO: is an id
      self._stmt_list()
      self._match('$$')
      pass
    else:
      return parse_error

  def _stmt_list(self):
    if self._token == '$$':
      self._skip()
    elif self._token in ['read', 'write']:
      self._stmt()
      self._stmt_list()
    elif:  # TODO: is an id
      self._stmt()
      self._stmt_list()
      pass
    else:
      return parse_error

  def _stmt(self):
    if self._token == 'read':
      self._match('read')
      self._match('id')
    elif self._token == 'write':
      self._match('write')
      self._expr()
    elif:  # TODO: is an id
      self._match('id')
      self._match(':=')
      self._expr()
    else:
      return parse_error

  def _expr(self):
    if self._token == '(':
      self._term()
      self._term_tail()
    elif:  # TODO: is an id
      self._term()
      self._term_tail()
    elif:  # TODO: is a number
      self._term()
      self._term_tail()
    else:
      return parse_error

  def _term_tail(self):
    if self._token in ['+', '-']:
      self._add_op()
      self._term()
      self._term_tail()
    elif self._token in [')', 'read', 'write', '$$']:
      self._skip()
    elif:  # TODO: is an id
      self._skip()
    else:
      return parse_error

  def _term(self):
    if self._token == '(':
      self._factor()
      self._factor_tail()
    elif:  # TODO: is an id
      self._factor()
      self._factor_tail()
    elif:  # TODO: is a number
      self._factor()
      self._factor_tail()
    else:
      return parse_error

  def _factor_tail(self):
    if self._token in ['*', '/']:
      self._mult_op()
      self._factor()
      self._factor_tail()
    elif self._token in ['+', '-', ')', 'read','write','$$']:
      self._skip()
    elif:  # TODO: is an id
      self._skip()
    else:
      return parse_error
  def _factor(self):
    if self._token == '(':
      self._match('(')
      self._expr()
      self._match(')')
    elif:  # TODO: is an id
      self._match('id')
    elif:  # TODO: is a number
      self._match('number')
    else:
      return parse_error

  def _add_op(self):
    if self._token == '+':
      self._match('+')
    elif self._token == '-':
      self._match('-')
    else:
      return parse_error

  def _mult_op(self):
    if self._token == '*':
      self._match('*')
    elif self._token == '/':
      self._match('/')
    else:
      return parse_error
