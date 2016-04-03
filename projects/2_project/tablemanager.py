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

  #returns True is a record was successfully inserted into the symbol table
  def _insert_one(self, label_name, var_type, **adds):
    label_key = (self.scope_names[-1], label_name)
    if not self.table.lookup(label_key) and label_name not in ck.keywords:
      self.table.insert(label_key, var_type, self.line_count)
      return True

  def parse_line(self, line):
    #ignore blank lines
    if not line.strip():
      return

    #check if scope should be initialized or finalized, the line variable is going to be screwed with
    if '{' in line:
      self.table.initialize_scope()
      self.line_counts.append(self.line_count)
      self.scope_names.append(str(self.table.scope_number))

      should_initialize = True
    else:
      should_initialize = False

    if '}' in line:
      should_finalize = True
    else:
      should_finalize = False

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
        param_tokens = [ x.strip() for x in params.rstrip(' {)\n').split(',') if x ]

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

          #if a scope was initialized this line, we need to use the correct name
          if should_initialize:
            real_scope_name = self.scope_names[-2]
          else:
            real_scope_name = self.scope_names[-1]

          if not self.table.lookup(( real_scope_name, word)) and word not in ck.keywords:
            self.table.insert(( real_scope_name, word), 'function', self.line_count, num_parameters=len(param_tokens), parameter_name_and_type=param_tokens, return_type=head)
            self.scope_names[-1] = '{} - level {}'.format(word, self.scope_names[-1])

          #insert function parameters
          for declare in param_tokens:
            declare = ''.join(c for c in declare if c not in set(string.punctuation)).split()
            if self._insert_one(declare[1], declare[0]):
              pass
        else:
          words = [ x.strip() for x in tail.split(',') if x ];

          #insert the (possibly) comma-delimited set of declared variables
          for word in words:
            word = ''.join(c for c in word if c not in set(string.punctuation)).split()[0]
            if self._insert_one(word, head):
              pass

    #handle close brace work
    if should_finalize:
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
