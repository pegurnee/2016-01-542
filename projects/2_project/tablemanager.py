from symbol_table import SymbolTable
import ckeywords as ck

import string
'''
Symbol Table Manager for a subset of the C language.

@author eddie gurnee
'''
class TableManager:
  def __init__(self, filename=None):
    super(TableManager, self).__init__()
    self.table = SymbolTable()

    self.line_counts = [0]
    self.scope_names = ['global']

    self.numscopes = {}

    if filename:
      self.load_file(filename)

  def __str__(self):
    artsy = '*' * 10
    return '{} Symbol Table for {} {}\n{}'.format(artsy, self.filename, artsy, self.table)

  def load_file(self, filename):
    self.filename = filename

    with open(filename) as f:
      for line in f:
        self.parse_line(line)

    return True

  #returns True is a record was successfully inserted into the symbol table
  def _insert_one(self, label_name, var_type, adds=None):
    label_key = (self.scope_names[-1], label_name)
    _data = {
      'var_type': var_type,
      'line_count': self.line_counts[-1]
    }
    if adds:
      _data.update(adds)
    if not self.table.lookup(label_key) and label_name not in ck.keywords:
      self.table.insert(label_key, **_data)
      return True

  def parse_line(self, line):
    #ignore blank lines
    if not line.strip():
      return

    #check if scope should be initialized or finalized, the line variable is going to be screwed with
    if '{' in line:
      self.table.initialize_scope()
      curr_scope = self.table.scope_number
      self.line_counts.append(0)

      if curr_scope in self.numscopes:
        self.numscopes[curr_scope] += 1
      else:
        self.numscopes[curr_scope] = 0
      self.scope_names.append('{}.{}'.format(curr_scope, self.numscopes[curr_scope]))

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
    if is_function or line.split()[0] in ['void', 'int', 'char', 'for'] or line.split()[0] in ck.varmods:
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
            real_scope = -2
          else:
            real_scope = -1

          if not self.table.lookup(( self.scope_names[real_scope], word)) and word not in ck.keywords:
            self.table.insert(( self.scope_names[real_scope], word), 'function', self.line_counts[real_scope], num_parameters=len(param_tokens), parameter_name_and_type=param_tokens, return_type=head)
            self.scope_names[-1] = '{} - level {}'.format(word, self.table.scope_number)

          #insert function parameters
          for declare in param_tokens:
            pointer = '*' in declare

            var_type, label_name = ''.join(c for c in declare if c not in set(string.punctuation)).split()
            if pointer:
              var_type += '*'

            if self._insert_one(label_name, var_type):
              pass
        else:
          words = [ x.strip() for x in tail.split(',') if x ];

          #become a pointer to the var
          if pointer:
            head += '*'

          #insert the (possibly) comma-delimited set of declared variables
          for word in words:

            extra_data = None
            #handle the array of it all
            if '[' in word and ']' in word:
              dimension_bounds = []
              head = '[' + head + ']'
              word, _, tail = word.partition('[')

              while True:
                dimension, _, tail = tail.partition(']')
                dimension_bounds.append(dimension)

                if not tail:
                  break
                else:
                  tail = tail[1:]

              extra_data = {
                'number_of_dimensions': len(dimension_bounds),
                'upper_bounds_of_dimensions' : dimension_bounds
              }

            word = ''.join(c for c in word if c not in set(string.punctuation)).split()[0]
            if self._insert_one(word, head, extra_data):
              pass

    #handle close brace work
    if should_finalize:
      self.table.finalize_scope()
      self.line_counts.pop()
      self.scope_names.pop()

    for i,c in enumerate(self.line_counts):
      self.line_counts[i] += 1

if __name__ == '__main__':
  print('This is a tool to use, not a tool to run')
