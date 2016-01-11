# PP #1 Implement a Recursive Descent Parser -- Checking syntax  
#### Distributed: 11 January 2016
#### Due: 25 January 2016

### Background

The text *Programming Language Pragmatics*, written by Scott has a grammar for a calculator (see Figure 2.15) and recursive descent parser to implement that language (Figure 2.16). The code for that parser is given in pseudo-code.

The grammar is not left recursive, so it is a good possibility for a recursive descent parser.  
In the grammar, the symbol eps stands for the null string.

The entry point to the recursive descent program is "procedure program". The parser calls the tokenizer (match()) with the desired token; the tokenizer then reads in chars from the input stream. As chars are read in to form a token, the chars are consumed.

The procedure match(expected) gets the next token from the input char stream. If expected matches that new input_token, then match() returns successfully. If the match fails, then the program terminates in an error state.

The chars $$ mark the end of the input stream for the recursive descent parser.

By examining the grammar in with the interpreter, the parallels between the two are obvious.
Project spec

Implement the interpreter in the language of your choice. When the parser detects an error, it should immediate output the current line with an appropriate error message. The parser should be able to do the following:

    Validate a program with correct syntax
    Report tokenizer error, the desired token, the actual token,
    Report parser error, the name of the method where the error was triggered.

The input stream should be supplied as a text file or from the keyboard (I don't care). Do not hardcode the input stream.
Testing the parser
Your validator should given an appropriate error message for each of the parse_error function calls in the pseudo-code.

    Valid input stream:

        a := 3
        b := a + 2
        write b
        $$


    Invalid token

         a := 2
         3 := 3
         $$


    Invalid factor


        read a
        a := 3 + (2
        write a
        $$


    Invalid term_tail

         a:= 2
         b := a % 3
         write a
         $$


Turn in:

    Hard copy of source code
    Screen shot showing validator action on above tests
    UML diagram (use a drawing tool, e.g, http://yed.yworks.com/support/manual/uml.html)

Grade based on:

    Functionality
    Readability -- this is extremely important. Points will be subtracted for each bad use of white space, bad variable name, etc
    Elegance
