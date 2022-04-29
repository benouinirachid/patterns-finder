import regex

from . import Pattern

# Time and Date

__time = "((([0]?[1-9]|1[0-2])(:|-|\\.)[0-5][0-9]((:|-|\\.)[0-5][0-9])?( )?(AM|am|aM|Am|PM|pm|pM|Pm))|(([0]?[0-9]|1[0-9]|2[0-3])(:|-|\\.)[0-5][0-9]((:|-|\\.)[0-5][0-9])?))"
__time_label = "TIME"
time = Pattern(__time, __time_label)

__date = "(0?[1-9]|[12][0-9]|3[01])[-/.](0?[1-9]|1[012])[-/.](19|20)?\\d{2}"
__date_label = "DATE"
date = Pattern(__date, __date_label)

__year = "(19|20)\\d{2}"
__year_label = "YEAR"
year = Pattern(__year, __year_label)
