from . import Pattern

# Currency

__monetary = "[\\p{Sc}][\\s]?[0-9.,]+[KMBTkmbt]?"
__monetary_label = "MONETARY"
monetary = Pattern(__monetary, __monetary_label)

__symbol = "[\\p{Sc}]"
__symbol_label = "SYMBOL"
symbol = Pattern(__symbol, __symbol_label)

__code = "GBP|EUR|USD|JPY|CNY|CHF|RUB"
__code_label = "CODE"
code = Pattern(__code, __code_label)

__name = "Dirham|Peso|Dollar|Mark|Ruble|Real|Franc|Euro|Koruna|Krone|Dinar|Pound|Sterling|Rial|Won|Rupee|Shilling|Lira|Yuan|Yen"
__name_label = "NAME"
name = Pattern(__name, __name_label)
