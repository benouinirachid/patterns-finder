from . import Pattern

# postal code

__us = "\\d{5}(?:-\\d{4})?"
__us_label = "US"
us = Pattern(__us, __us_label)

__canada = "[ABCEGHJ-NPRSTVXY]\\d[A-Z][ -]?\\d[A-Z]\\d"
__canada_label = "CANADA"
canada = Pattern(__canada, __canada_label)

__uk = "[a-zA-Z]{1,2}[0-9][0-9A-Za-z]{0,1}[ -]{0,1}[0-9][A-Za-z]{2}"
__uk_label = "UK"
uk = Pattern(__uk, __uk_label)

__france = "(?:0[1-9]|[1-8]\\d|9[0-8])\\d{3}"
__france_label = "FRANCE"
france = Pattern(__france, __france_label)

__spain = "(?:0[1-9]|[1-4]\\d|5[0-2])\\d{3}"
__spain_label = "SPAIN"
spain = Pattern(__spain, __spain_label)

__switzerland = "[1-9]\\d{3}"
__switzerland_label = "SWITZERLAND"
switzerland = Pattern(__switzerland, __switzerland_label)

__brazilian = "\\d{5}-\\d{3}"
__brazilian_label = "BRAZILIAN"
brazilian = Pattern(__brazilian, __brazilian_label)
