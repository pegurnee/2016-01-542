class SymbolTable:

  def __init__(self):
    self.scope_number = 0
    self._table = {}

  def initialize_scope(self):
    self.scope_number += 1

  def finalize_scope(self):
    self.scope_number -= 1

  def lookup(self, name):
    if name in self._table.keys():
      return self._table[name]
    return False

  def insert(self, name, type, name_and_level_of_parent, line_count, num_parameters=0, parameter_name_and_type=[], return_type=None, number_of_dimensions=0, upper_bounds_of_dimensions=[] ):
    pass

  def add(self, label, address):
    if label in self._table.keys():
      return False
    self._table[label] = address
    return True

  def get_label_kv(self, address):
    for key in self._table.keys():
      if self._table[key] == address:
        return key, self._table[key]
    return False

  def get_address_kv(self, label):
    for key in self._table.keys():
      if key == label:
        return key, self._table[key]
    return False

  def get_label(self, address):
    for key in self._table.keys():
      if self._table[key] == address:
        return key
    return False

  def get_address(self, label):
    for key in self._table.keys():
      if key == label:
        return self._table[key]
    return False

  def has(self, label):
    if label in self._table.keys():
      return True
    else:
      return False
