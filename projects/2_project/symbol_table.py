class SymbolTable:
  """
  This symbol table class was first seen in COSC 341. Nothing has been removed, only things have been added
  """
  def __init__(self):
    self.scope_number = 0
    self._table = {}

  def initialize_scope(self):
    self.scope_number += 1

  def finalize_scope(self):
    self.scope_number -= 1

  def lookup(self, location_and_name):
    if location_and_name in self._table.keys():
      return self._table[location_and_name]
    return False

  def insert(self, location_and_name, var_type, line_count, num_parameters=0, parameter_name_and_type=[], return_type=None, number_of_dimensions=0, upper_bounds_of_dimensions=[] ):
    _data = [var_type, self.scope_number, line_count]
    if '[' in var_type:
      _data.extend([number_of_dimensions, upper_bounds_of_dimensions])
    elif var_type == 'function':
      _data.extend([num_parameters, parameter_name_and_type, return_type])

    self._table[location_and_name] = tuple(_data)

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

  def __str__(self):
    return '\n'.join(['{}: {}'.format(k,v) for k,v in sorted(self._table.items())])
