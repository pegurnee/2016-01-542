class SymbolTable:

  def __init__(self):
    self._table = {}

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
