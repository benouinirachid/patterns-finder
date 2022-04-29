from . import Pattern

# Numbers

__integer = "(\\-|\\+|±)?\\d+"
__integer_label = "INTEGER"
integer = Pattern(__integer, __integer_label)

__float = "[\\-\\+±]?\\d+\\.\\d*"
__float_label = "FLOAT"
float = Pattern(__float, __float_label)

__scientific = "[+-]?\\d(\\.\\d+)?[Ee][+-]?\\d+"
__scientific_label = "SCIENTIFIC"
scientific = Pattern(__scientific, __scientific_label)

__hexadecimal = "0[xX][0-9a-fA-F]+"
__hexadecimal_label = "HEXADECIMAL"
hexadecimal = Pattern(__hexadecimal, __hexadecimal_label)

__percent = "([±+-]?\\d{1,4}([,.]\\d{0,2})? ?%)"
__percent_label = "PERCENT"
percent = Pattern(__percent, __percent_label)

__roman = "(?=[MDCLXVI])(M*)(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})"
__roman_label = "ROMAN"
roman = Pattern(__roman, __roman_label)
