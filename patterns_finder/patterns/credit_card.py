from . import Pattern

# Credit Cards

__generic = "\\d{4}(| |-)(?:\\d{4}\\1){2}\\d{4}"
__generic_label = "GENERIC"
generic = Pattern(__generic, __generic_label)

__visa = "4\\d{3}(| |-)(?:\\d{4}\\1){2}\\d{4}"
__visa_label = "VISA"
visa = Pattern(__visa, __visa_label)

__mastercard = "5[1-5]\\d{2}(| |-)(?:\\d{4}\\1){2}\\d{4}"
__mastercard_label = "MASTERCARD"
mastercard = Pattern(__mastercard, __mastercard_label)

__discover = "6(?:011|5\\d\\d)(| |-)(?:\\d{4}\\1){2}\\d{4}"
__discover_label = "DISCOVER"
discover = Pattern(__discover, __discover_label)

__american_express = "3[47]\\d{1,2}(| |-)\\d{6}\\1\\d{6}"
__american_express_label = "AMERICAN_EXPRESS"
american_express = Pattern(__american_express, __american_express_label)
