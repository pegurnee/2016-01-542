from parse_error import ParseError

class TokenError(ParseError):
  def __init__(self, actual, expected):
    super().__init__('token')
    self._actual_token = actual
    self._expected_token = expected

  def token_issue(self):
    return self._actual_token, self._expected_token
