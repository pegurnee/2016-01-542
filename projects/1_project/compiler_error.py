class CompilerError(Exception):
  def __init__(self, line, error_loc):
    self._line = line
    self._error_loc = error_loc

  def location(self):
    return self._line, self._error_loc
