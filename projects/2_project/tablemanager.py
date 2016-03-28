from symbol_table import SymbolTable

class TableManager:
  """docstring for TableManager"""
  def __init__(self, arg):
    super(TableManager, self).__init__()
    self.arg = arg

def parse_line(line):
  #here
  if line.find('='):
    assign_stmt, value = tuple(map(lambda x: x.trim(), line.split('=')))

#initialize_scope
#insert
#lookup
#finalize_scope

if __name__ == '__main__':
