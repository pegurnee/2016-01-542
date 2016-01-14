from parse_error  import ParseError
from tokenizer    import Tokenizer
from symbol_table import SymbolTable

class Interpreter:

  def __init__(self, code_string):
    self._KEYWORDS = ['read', 'write']

    self._token = None

    self._tokenizer = Tokenizer(code_string, ['+','-','/','*','(',')',':='], ['\n',' '])
    self._symboltable = SymbolTable()

  def interpret(self, code_string=None):
    if code_string is None:
      code_string = 'totally unneeded'
    self._consume()
    self.program()

  def _consume(self, _nomable=None):
    if _nomable == '$$':
      return True

    if _nomable == 'id':
      self._symboltable.add(self._token, 'theoretically a line number')
    # TODO: add current token to AST
    self._token = self._tokenizer.next()

  def _is_token_id(self, _id=None):
    if _id is None:
      _id = self._token

    if self._symboltable.has(_id):
      return True
    elif _id.isalpha() and _id not in self._KEYWORDS:
      return True
    else:
      return False

  def _is_token_num(self, _num=None):
    if _num is None:
      _num = self._token
    if _num.isdigit():
      return True
    else:
      return False

  def _is_token_id_or_num(self, _token=None):
    if _token is None:
      _token = self._token
    if self._is_token_id(_token) or self._is_token_num(_token):
      return True
    else:
      return False

  def _match(self, expected):
    # TODO: might conflict with id's named 'id' or 'number'
    if expected == self._token or expected in ['id', 'number']:
      self._consume(self._token)
    else:
      raise ParseError('token')

  def _skip(self):
    pass

  def program(self):
    if self._token in ['read', 'write', '$$'] or self._is_token_id():
      self._stmt_list()
      self._match('$$')
    else:
      raise ParseError('program')

  def _stmt_list(self):
    if self._token == '$$':
      self._skip()
    elif self._token in ['read', 'write'] or self._is_token_id():
      self._stmt()
      self._stmt_list()
    else:
      raise ParseError('stmt_list')

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
      raise ParseError('stmt')

  def _expr(self):
    if self._token == '(' or self._is_token_id_or_num():
      self._term()
      self._term_tail()
    else:
      raise ParseError('expr')

  def _term_tail(self):
    if self._token in ['+', '-']:
      self._add_op()
      self._term()
      self._term_tail()
    elif self._token in [')', 'read', 'write', '$$'] or self._is_token_id():
      self._skip()
    else:
      raise ParseError('term_tail')

  def _term(self):
    if self._token == '(' or self._is_token_id_or_num():
      self._factor()
      self._factor_tail()
    else:
      raise ParseError('term')

  def _factor_tail(self):
    if self._token in ['*', '/']:
      self._mult_op()
      self._factor()
      self._factor_tail()
    elif self._token in ['+', '-', ')', 'read', 'write', '$$'] or self._is_token_id():
      self._skip()
    else:
      raise ParseError('factor_tail')

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
      raise ParseError('factor')

  def _add_op(self):
    if self._token == '+':
      self._match('+')
    elif self._token == '-':
      self._match('-')
    else:
      raise ParseError('add_op')

  def _mult_op(self):
    if self._token == '*':
      self._match('*')
    elif self._token == '/':
      self._match('/')
    else:
      raise ParseError('mult_op')

if __name__ == "__main__":
  test = Interpreter("read a\na := 3\nwrite (a + 3) - b * 4\n$$")
  #test = Interpreter("read a\na := 2\nb := ( 4\nwrite \n$$")
  #test = Interpreter("a := 2\n$$\n")
  import traceback
  try:
    print(test._tokenizer._tokens)
    test.interpret()
    print('success')
  except ParseError as e:
    print('Invalid at %s because of %s' % (e.location(), test._token))
    traceback.print_exc()
