from symbol_table import SymbolTable
import ckeywords as ck

import string

class TableManager:
  def __init__(self):
    super(TableManager, self).__init__()
    self.table = SymbolTable()

    self.line_counts = []
    self.line_count = 0

  def parse_line(self, line):
    print(line)

    #ignore blank lines
    if not line.strip():
      return

    #handle open brace work
    if '{' in line:
      self.table.initialize_scope()
      self.line_counts.append(self.line_count)

    #determine if a function is defined and get parameters from functions
    is_function = False
    if '(' in line:
      line = line.replace('(', ' ( ').replace(')', ' ) ')
      if ';' not in line and line.split()[0] not in ck.flowkeys:
        #function definitions are lines that have an open parens and don't have a semicolon AND the first token is not a flow of control keyword
        line, params = line.split('(')
        is_function = True
        param_tokens = params.rstrip(' {)\n').split(',')

    #insert new labels into the table
    if is_function or line.split()[0] in ['void', 'int', 'char' 'for'] or line.split()[0] in ck.varmods:
      if '*' in line:
        line = line.replace('*', '')
        pointer = True
      else:
        pointer = False
      head, tail = line.split(maxsplit=1)

      while head in ck.varmods:
        head, tail = tail.split(maxsplit=1)
      if head in ['void','int','char']:
        for word in tail.split(','):
          word = ''.join(c for c in word if c not in set(string.punctuation)).split()[0]
          if not self.table.lookup(word) and word not in ck.keywords:
            self.table.insert(word.strip(), head if head != 'void' else 'function', self.line_count)

    if '=' in line and '==' not in line:
      assign_stmt, value = tuple(map(lambda x: x.strip(), line.split('=')))

    #handle close brace work
    if '}' in line:
      self.table.finalize_scope()
      self.line_count = self.line_counts.pop()

    self.line_count += 1

if __name__ == '__main__':
  test_files = ['p253.c', 'p257.c', 'p267.c', 'p324.c']
  for fname in test_files:
    man = TableManager()
    with open('test_cases/' + fname) as f:
      for line in f:
        man.parse_line(line)
    print(man.table)
    print('=' * 40)
