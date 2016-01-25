from interpreter    import Interpreter
from compiler_error import CompilerError
from token_error    import TokenError
from parse_error    import ParseError

from os             import walk


def main():
  _tests  = []
  _fnames = []
  for (_, _, filenames) in walk('test_cases'):
    _fnames.extend(filenames)
    break

  for filename in _fnames:
    with open('test_cases/' + filename) as f:
      _tests.append(f.read())

  interpreter = Interpreter()
  for _test in _tests:
    print('<-\ninterpret:\n%s' % _test)
    try:
      interpreter.interpret(_test)
      _ret = 'Valid'
    except TokenError as e:
      _ret = 'Invalid token at line %s:\n  actual: %s\n  expected: %s' %  e.token_issue()
    except ParseError as e:
      _ret = 'Invalid at line %s:\n  method: %s' % e.location()
    print('->%s\n\n' % _ret)
    interpreter.reset()

if __name__ == '__main__':
  main()
