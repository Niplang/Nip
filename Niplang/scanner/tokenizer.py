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
    "class",
    "abs",  # Abstract keyword
    "new",
    "interface"  # Can delete it later
    "inherits",
    "implements",
    "return",
)

access_specifiers = (
    "priv",  # Private access specifier
    "pub",  # Public access specifier
    "protected",
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

logical_operator_keywords = (
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
    "pow",  # Exponents
)

assignment_operators = (
    "=",
    "+=",
    "-=",
    "*=",
    "/=",
    "%=",
    "pow=",
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
def token():
    # TODO
    pass
