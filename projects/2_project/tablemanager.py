from symbol_table import SymbolTable

class TableManager:
  def __init__(self):
    super(TableManager, self).__init__()
    self.table = SymbolTable()
    self.line_count = 0

  def parse_line(self, line):
    #here
    if line.find('{')
      self.table.initialize_scope()

    words = line.split()
    if words[0] in ['void','int','char']:
      if not self.table.lookup(words[1]):
        self.table.insert(words[1])

    if line.find('='):
      assign_stmt, value = tuple(map(lambda x: x.trim(), line.split('=')))

    if line.find('}')
      self.finalize_scope()

if __name__ == '__main__':
