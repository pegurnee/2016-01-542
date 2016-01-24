from interpreter import Interpreter
from parse_error import ParseError

def main():
  tests = ["""
    a := 3
    b := a + 2
    write b
    $$
    """
  , """
    a := 2
    3 := 3
    $$
    """
  , """
    read a
    a := 3 + (2
    write a
    $$
    """
  , """
    a:= 2
    b := a % 3
    write a
    $$
    """
    ]

  interpreter = Interpreter()
  for _test in tests:
    print('interpret: %s' % _test)
    try:
      interpreter.interpret(_test)
      print('success')
    except:
      print('oopsies')

if __name__ == '__main__':
  main()
