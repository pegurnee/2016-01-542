class Interpreter

  def __init__(self, code_string):
    self._token = None
    self._tokens = []

    #Split code by lines, then split lines by white space into tokens
    lines = code_string.splitlines()
    for x in range(len(lines)):
      for token in lines[x].split():
        self._tokens[x].append(token)

  def match(self, expected):
    if expected == self._token:
      self.consume(self._token)
    else:
      return parse_error

  def consume(self, correctToken):
    pass

  def program(self, arg):
    pass

"""
procedure match ( expected )
	if input_token = expected then consume input_token
	else parse_error

-- this is the start routine:
procedure program
	case input_token of
		id, read, write, $$:
			stmt_list
			match ( $$ )
		otherwise parse_error

procedure stmt_list
	case input_token of
		id, read, write : stmt; stmt_list
		$$ : skip		                          -- epsilon production
		otherwise parse_error

procedure stmt
	case input_token of
		id : match( id );   match( := ); expr
		read : match( read );   match( id )
		write : match( write );   expr
		otherwise parse_error

procedure expr
	case input_token of
		id, number, ( : term; term_tail
		otherwise parse_error

procedure term_tail
	case input_token of
		+, - : add_op; term; term_tail
		), id, read, write, $$ : skip		      -- epsilon production
	otherwise parse_error

procedure term
	case input_token of
		id, number, ( : factor; factor_tail
		otherwise parse_error

procedure factor_tail
	case input_token of
		*, / : mult_op; factor; factor_tail
		+, -, ), id, read, write, $$ : skip		-- epsilon production
		otherwise parse_error

procedure factor
	case input_token of
		id : match( id )
		number : match( number )
		( : match( ( ); expr; match( ) )
		otherwise parse_error

procedure add_op
	case input_token of
		+ : match( + )
		- : match( - )
		otherwise parse_error

procedure mult_op
	case input_token of
		* : match( * )
		/ : match( / )
		otherwise parse_error
"""
