from parse_error    import ParseError
from token_error    import TokenError
from compiler_error import CompilerError
from tokenizer      import Tokenizer
from symbol_table   import SymbolTable

class Interpreter:

  def __init__(self, code_string=None):
    self._KEYWORDS = ['read', 'write']

    self._token = None
    self._line = 0

    self._tokenizer = Tokenizer(code_string, ['+','-','/','*','(',')',':='], ['\n',' '])
    self._symboltable = SymbolTable()

  def reset(self):
    self._line = 0
    self._token = None
    self._tokenizer.clear()

  def interpret(self, code_string=None):
    if code_string is not None:
      self._tokenizer.append(code_string)

    self._consume()
    self.program()

  def _consume(self, _nomable=None):
    if _nomable == '$$':
      self.reset()
      return True

    if _nomable == 'id':
      self._symboltable.add(self._token, self._line)
    # TODO: add current token to AST
    self._token = self._tokenizer.next()

  def _is_token_id(self, _id=None):
    if self._token is None:
      raise ParseError(self._line, 'unexpected EOF')

    if _id is None:
      _id = self._token

    if self._symboltable.has(_id):
      return True
    elif _id.isalpha() and _id not in self._KEYWORDS:
      return True
    else:
      return False

  def _is_token_num(self, _num=None):
    if self._token is None:
      raise ParseError(self._line, 'unexpected EOF')

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
      raise TokenError(self._line, self._token, expected)

  def _skip(self):
    pass

  def program(self):
    if self._token in ['read', 'write', '$$'] or self._is_token_id():
      self._stmt_list()
      self._match('$$')
    else:
      raise ParseError(self._line, 'program')

  def _stmt_list(self):
    if self._token == '$$':
      self._skip()
    elif self._token in ['read', 'write'] or self._is_token_id():
      self._line += 1
      self._stmt()
      self._stmt_list()
    else:
      raise ParseError(self._line, 'stmt_list')

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
      raise ParseError(self._line, 'stmt')

  def _expr(self):
    if self._token == '(' or self._is_token_id_or_num():
      self._term()
      self._term_tail()
    else:
      raise ParseError(self._line, 'expr')

  def _term_tail(self):
    if self._token in ['+', '-']:
      self._add_op()
      self._term()
      self._term_tail()
    elif self._token in [')', 'read', 'write', '$$'] or self._is_token_id():
      self._skip()
    else:
      raise ParseError(self._line, 'term_tail')

  def _term(self):
    if self._token == '(' or self._is_token_id_or_num():
      self._factor()
      self._factor_tail()
    else:
      raise ParseError(self._line, 'term')

  def _factor_tail(self):
    if self._token in ['*', '/']:
      self._mult_op()
      self._factor()
      self._factor_tail()
    elif self._token in ['+', '-', ')', 'read', 'write', '$$'] or self._is_token_id():
      self._skip()
    else:
      raise ParseError(self._line, 'factor_tail')

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
      raise ParseError(self._line, 'factor')

  def _add_op(self):
    if self._token == '+':
      self._match('+')
    elif self._token == '-':
      self._match('-')
    else:
      raise ParseError(self._line, 'add_op')

  def _mult_op(self):
    if self._token == '*':
      self._match('*')
    elif self._token == '/':
      self._match('/')
    else:
      raise ParseError(self._line, 'mult_op')

if __name__ == "__main__":
  test = Interpreter("read a\na := 3\nwrite (a + 3) - b * 4\n$$")
  #test = Interpreter("read a\na := 2\nb := ( 4\nwrite \n$$")
  #test = Interpreter("a := 2\n$$\n")
  import traceback
  try:
    print(test._tokenizer._tokens)
    test.interpret()
    print('success')
  except CompilerError as e:
    print('Invalid at %s because of %s at line %s' % (e.location(), test._token, test._line))
    traceback.print_exc()
