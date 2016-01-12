class Interpreter

  def __init__(self, code_string):
    self._KEYWORDS = ['read', 'write']

    self._token = None
    self._tokens = []

    # Split code by lines, then split lines by white space into tokens
    lines = code_string.splitlines()
    for x in range(len(lines)):
      for token in lines[x].split():
        self._tokens[x].append(token)

  def _is_token_id(self, _id=self._token):
    if _id.isalpha() and _id not in self._KEYWORDS:
      return True
    else:
      return False

  def _is_token_num(self, _num=self._token):
    if _num.isdigit():
      return True
    else:
      return False

  def _is_token_id_or_num(self, _token=self._token):
    if self._is_token_id(_token) or self._is_token_num(_token):
      return True
    else:
      return False

  def _match(self, expected):
    #TODO: might conflict with id's named 'id' or 'number'
    if expected == self._token or expected in ['id', 'number']:
      self.consume(self._token)
    else:
      return parse_error

  def consume(self, _nomable):
    if not self._tokens:
      return True
    elif not self._tokens[0]:
      self._tokens.pop(0)

    # TODO: add current token to AST
    self._token = self._tokens[0].pop(0)

  def _skip(self):
    pass

  def program(self):
    if self._token in ['read', 'write', '$$'] or self._is_token_id():
      self._stmt_list()
      self._match('$$')
    else:
      return parse_error

  def _stmt_list(self):
    if self._token == '$$':
      self._skip()
    elif self._token in ['read', 'write'] or self._is_token_id():
      self._stmt()
      self._stmt_list()
    else:
      return parse_error

  def _stmt(self):
    if self._token == 'read':
      self._match('read')
      self._match('id')
    elif self._token == 'write':
      self._match('write')
      self._expr()
    elif self._is_token_id():
      self._match('id')
      self._match(':=')
      self._expr()
    else:
      return parse_error

  def _expr(self):
    if self._token == '(' or self._is_token_id_or_num():
      self._term()
      self._term_tail()
    else:
      return parse_error

  def _term_tail(self):
    if self._token in ['+', '-']:
      self._add_op()
      self._term()
      self._term_tail()
    elif self._token in [')', 'read', 'write', '$$'] or self._is_token_id():
      self._skip()
    else:
      return parse_error

  def _term(self):
    if self._token == '(' or self._is_token_id_or_num():
      self._factor()
      self._factor_tail()
    else:
      return parse_error

  def _factor_tail(self):
    if self._token in ['*', '/']:
      self._mult_op()
      self._factor()
      self._factor_tail()
    elif self._token in ['+', '-', ')', 'read', 'write', '$$'] or self._is_token_id():
      self._skip()
    else:
      return parse_error

  def _factor(self):
    if self._token == '(':
      self._match('(')
      self._expr()
      self._match(')')
    elif self._is_token_id():
      self._match('id')
    elif self._is_token_num():
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
