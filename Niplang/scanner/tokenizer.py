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
    "do",
    "while",
    "break",
    "continue",
)

structure_keywords = (
    "struct",
    "func",
    "class",
    "abs",
    "new",
    "interface"
    "inherits",
    "implements",
    "return",
)

access_specifiers = (
    "priv",
    "pub",
    "protected",
)

import_keywords = (
    "import",
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
    "const",
    "var",
)

variable_types = (
    "bool",
    "int",
    "long",
    "float",
    "double",
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
    "pow",
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


def token():
    pass
