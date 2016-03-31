from symbol_table import SymbolTable
import ckeywords as ck

import string

class TableManager:
  def __init__(self):
    super(TableManager, self).__init__()
    self.table = SymbolTable()

    self.line_counts = []
    self.line_count = 0

    self.scope_names = ['global']

  def parse_line(self, line):
    #ignore blank lines
    if not line.strip():
      return

    #handle open brace work
    if '{' in line:
      self.table.initialize_scope()
      self.line_counts.append(self.line_count)
      self.scope_names.append(str(self.table.scope_number))

    #determine if a function is defined and get parameters from functions
    is_function = False
    if '(' in line:
      line = line.replace('(', ' ( ').replace(')', ' ) ')
      if ';' not in line and line.split()[0] not in ck.flowkeys:
        #function definitions are lines that have an open parens
        # and don't have a semicolon
        # AND the first token is not a flow of control keyword
        line, params = line.split('(')
        is_function = True
        param_tokens = params.rstrip(' {)\n').split(',')

    #insert new labels into the table
    if is_function or line.split()[0] in ['void', 'int', 'char' 'for'] or line.split()[0] in ck.varmods:
      #handle pointer nonsense
      if '*' in line:
        line = line.replace('*', '')
        pointer = True
      else:
        pointer = False
      head, tail = line.split(maxsplit=1)

      #ignore any/all variable modifiers
      while head in ck.varmods:
        head, tail = tail.split(maxsplit=1)

      #first token of var type
      if head in ['void','int','char']:
        if is_function:
          #insert function name
          word = tail.strip()
          if not self.table.lookup((self.scope_names[-1], word)) and word not in ck.keywords:
            self.table.insert(( self.scope_names[-1], word), 'function', self.line_count)
            self.scope_names[-1] = word

          #insert function parameters
          for declare in param_tokens:
            if not declare:
              continue

            declare = ''.join(c for c in declare if c not in set(string.punctuation)).split()
            if not self.table.lookup((self.scope_names[-1], declare[1])) and declare[1] not in ck.keywords:
              self.table.insert((self.scope_names[-1], declare[1]), declare[0], self.line_count)
        else:
          words = tail.split(',');

          #insert the (possibly) comma-delimited set of declared variables
          for word in words:
            if not word:
              continue

            word = ''.join(c for c in word if c not in set(string.punctuation)).split()[0]
            if not self.table.lookup(( self.scope_names[-1], word)) and word not in ck.keywords:
              self.table.insert(( self.scope_names[-1], word.strip()), head, self.line_count)

    #handle close brace work
    if '}' in line:
      self.table.finalize_scope()
      self.line_count = self.line_counts.pop()
      self.scope_names.pop()

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
