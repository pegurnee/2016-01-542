class ParseError(Exception):
  def __init__(self, error_loc):
    self._error_loc = error_loc

  def location(self):
    return self._error_loc
