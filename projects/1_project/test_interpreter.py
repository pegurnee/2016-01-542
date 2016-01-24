from interpreter  import Interpreter
from parse_error  import ParseError

from os           import walk


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
    print('interpret: \n%s' % _test)
    try:
      interpreter.interpret(_test)
      print('success')
    except:
      print('oopsies')

if __name__ == '__main__':
  main()
