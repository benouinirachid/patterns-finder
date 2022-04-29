from . import Pattern

# Phone

__generic = "(\\+\\d{1,3}\\s?)?((\\(\\d{3}\\)\\s?)|(\\d{3})(\\s|-?))(\\d{3}(\\s|-?))(\\d{4})(\\s?(([E|e]xt[:|.|]?)|x|X)(\\s?\\d+))?"
__generic_label = "GENERIC"
generic = Pattern(__generic, __generic_label)

__uk = "(((\\+44\\s?\\d{4}|\\(?0\\d{4}\\)?)\\s?\\d{3}\\s?\\d{3})|((\\+44\\s?\\d{3}|\\(?0\\d{3}\\)?)\\s?\\d{3}\\s?\\d{4})|((\\+44\\s?\\d{2}|\\(?0\\d{2}\\)?)\\s?\\d{4}\\s?\\d{4}))(\\s?\\#(\\d{4}|\\d{3}))?"
__uk_label = "UK"
uk = Pattern(__uk, __uk_label)

__us = "(?:\\+?1\\s)?(\\([0-9]{3}\\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}"
__us_label = "US"
us = Pattern(__us, __us_label)
