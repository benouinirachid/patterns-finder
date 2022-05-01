from . import Pattern
# Web

__email = "(?<=\\s|^)\\w+([-+.']\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*(?=\\s|$|\\.)"
__email_label = "EMAIL"
email = Pattern(__email, __email_label)

__url = "((ftp|https?):\\/\\/(?:www\\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\\.[^\\s]{2,}|www\\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\\.[^\\s]{2,}|https?:\\/\\/(?:www\\.|(?!www))[a-zA-Z0-9]+\\.[^\\s]{2,}|www\\.[a-zA-Z0-9]+\\.[^\\s]{2,})"
__url_label = "URL"
url = Pattern(__url, __url_label)

__uri = "\\w+:(\\/?\\/?)[^\\s]+"
__uri_label = "URI"
uri = Pattern(__uri, __uri_label)

__mailto = "mailto:\\w+([-+.']\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*"
__mailto_label = "MAILTO"
mailto = Pattern(__mailto, __mailto_label)

__html_link = "<\\s*a[^>]*>(.*?)<\\s*\\/\\s*a>"
__html_link_label = "HTML_LINK"
html_link = Pattern(__html_link, __html_link_label)

__sql = "(?i)(?s)\\b(select)\\b(.*?)\\b(from)\\b|\\b(insert)\\b(.*?)\\b(into)\\b|\\b(update)\\b(.*?)\\b(set)\\b|\\b(delete)(.*?)\\b(from)\\b"
__sql_label = "SQL"
sql = Pattern(__sql, __sql_label)

__color_hex = "#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})"
__color_hex_label = "COLOR_HEX"
color_hex = Pattern(__color_hex, __color_hex_label)

__copyright = "(?:©|\\(c\\)|copyright\\b|(?-i:&copy;|&COPY;)|&#x0{0,3}a9;|&#169;)\\s*(\\d{4})"
__copyright_label = "COPYRIGHT"
copyright = Pattern(__copyright, __copyright_label)

__alphanumeric = "([-A-Za-z0-9_]*?([-A-Za-z_][0-9]|[0-9][-A-Za-z_])[-A-Za-z0-9_]*)"
__alphanumeric_label = "ALPHANUMERIC"
alphanumeric = Pattern(__alphanumeric, __alphanumeric_label)

__emoji = "[\\U0001F40C-\\U0001F43C]|\\U0001F98A|[\\U0001F601-\\U0001F64F]|[-\\U0001F680-\\U0001F6C0]|[\\uD800-\\uDBFF]|[\\u2702-\\u27B0]|[\\uF680-\\uF6C0]|[\\u24C2-\\uF251]"
__emoji_label = "EMOJI"
emoji = Pattern(__emoji, __emoji_label)

__username = "[a-zA-Z][a-zA-Z0-9_-]{6,20}"
__username_label = "USERNAME"
username = Pattern(__username, __username_label)

__quotation = "([\"“‘\'])(?:\\\\.|[^\\\\])*?([\"”‘’\'])"
__quotation_label = "QUOTATION"
quotation = Pattern(__quotation, __quotation_label)

__ipv4 = "(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
__ipv4_label = "IPV4"
ipv4 = Pattern(__ipv4, __ipv4_label)

__ipv6 = "(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"
__ipv6_label = "IPV6"
ipv6 = Pattern(__ipv6, __ipv6_label)
