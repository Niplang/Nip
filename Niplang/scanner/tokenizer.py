# Author: Pavan D Umesh
# https://github.com/Pavan2027

value_keywords = (
    "true",
    "false",
    "NULL",
)

control_flow_keywords = (
    "if",
    "else",
    "switch",
    "case"
)

iteration_keywords = (
    "for",
    "do",  # do-while loop
    "while",
    "break",
    "continue",
)

structure_keywords = (
    "struct",
    "func",  # Function
    "main",  # Warning: For the main function, might delete later
    "class",
    "abs",  # Abstract keyword
    "new",
    "interface"  # Can delete it later. Might merge abstract
    "inherits",
    "implements",
    "return",
)

access_specifiers = (
    "priv",  # Private access specifier
    "pub",  # Public access specifier
    "prot", # Protected access specifier
)

import_keywords = (
    "import",
    # Need to implement other importing keywords / Namespaces
)

exception_keywords = (
    "try",
    "throw",
    "except",
    "catch",
    "finally",
)

variable_specifiers = (
    "static",
    "final",
    "const",  # Constant keyword
    "var",  # Variable keyword
    "unsigned",
)

variable_types = (
    "bool",
    "int",
    "long",
    "float",
    "double",
    "complex",  # For complex numbers
    "char",
    "str",
    "void",
)

logical_operators = (
    "&&",
    "||",
    "!",
    "->",  # Equivalent to 'in' keyword in python
)

arithmetic_operators = (
    "+",
    "-",
    "*",
    "/",
    "%",
)

string_operators = (
    "\"\"",
    "\'\'",
    "\'\'\'",
)

assignment_operators = (
    "=",
    "+=",
    "-=",
    "*=",
    "/=",
    "%=",
    "&=",
    "|=",
    "^=",
    ">>=",
    "<<=",
)

comparison_operators = (
    "==",
    "!=",
    ">",
    "<",
    ">=",
    "<=",
)

bitwise_operators = (
    "&",
    "|",
    "^",
    "~",
    "<<",
    ">>",
)

whitespace = ' '


# Function to return the lexeme
def lexeme():
    # TODO
    pass