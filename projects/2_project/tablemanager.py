from symbol_table import SymbolTable

class TableManager:
  def __init__(self):
    super(TableManager, self).__init__()
    self.table = SymbolTable()
    self.line_count = 0

  def parse_line(self, line):
    #here
    print(line)
    if line.find('{'):
      self.table.initialize_scope()

    words = line.split()
    if words[0] in ['void','int','char']:
      word = words[1]

      pointer = False
      more = False
      if '*' in word:
        word = word.replace('*', '')
        pointer = True
      if ',' in word:
        word = word.replace(',', '')
        more = True

      if not self.table.lookup(word):
        self.table.insert(word, words[0] if words[0] != 'void' else 'function')

    if '=' in line:
      assign_stmt, value = tuple(map(lambda x: x.strip(), line.split('=')))

    if line.find('}'):
      self.finalize_scope()

if __name__ == '__main__':
  man = TableManager()
  with open('test_cases/p257.c') as f:
    for line in f:
      man.parse_line(line)
