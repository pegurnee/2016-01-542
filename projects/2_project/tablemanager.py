from symbol_table import SymbolTable

class TableManager:
  def __init__(self):
    super(TableManager, self).__init__()
    self.table = SymbolTable()

    self.line_counts = []
    self.line_count = 0

  def parse_line(self, line):
    #here
    print(line)
    #ignore blank lines
    if not line.strip():
      return

    if line.find('{'):
      self.table.initialize_scope()
      self.line_counts.append(self.line_count)

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
        self.table.insert(word, words[0] if words[0] != 'void' else 'function', self.line_count)

    if '=' in line:
      assign_stmt, value = tuple(map(lambda x: x.strip(), line.split('=')))

    if line.find('}'):
      self.table.finalize_scope()
      self.line_count = self.line_counts.pop()

    self.line_count += 1

if __name__ == '__main__':
  man = TableManager()
  with open('test_cases/p253.c') as f:
    for line in f:
      man.parse_line(line)
  print(man.table)
