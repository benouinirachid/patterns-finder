# pattern-finder library

Simple, Fast, Powerful and Easily extensible library for extracting patterns from text, with over than 60 predefined Regular Expressions.
This library offers the capabilities:
* A set of predefined patterns with the most useful regex.
* Extend the patterns, by adding user defined regex.
* Find and extarct patterns from text
* Pandas' Dataframe support.
* Sort the results of extraction.
* Summarize the results of extraction.
* Display extractions by visualy rich text annotation.
* Build complex extraction rules based on regex (in future release).

# Installation

To install the last version of patterns-finder library, use pip:

```bash
pip install patterns-finder
```

# Usage

## Find a pattern in the text

Just import patterns, like `emoji` from `patterns_finder.patterns.web`, then you can use them to find pattern in text:

```python
from patterns_finder.patterns.web import emoji, url, email 

emoji.find("the quick #A52A2A 🦊 jumped 3 times over the lazy 🐶 ")
# Output:
# [(18, 19, 'EMOJI', '🦊'), (49, 50, 'EMOJI', '🐶')]

url.find("The lazy 🐶 has a website https://lazy.dog.com ")
# Output:
# [(25, 45, 'URL', 'https://lazy.dog.com')]

email.find("quick.brown@fox.com is the email of 🦊 ")
# Output:
# [(0, 19, 'EMAIL', 'quick.brown@fox.com')]

```

The results provided the method find for each pattern are in the form:
    
    [(0, 19, 'EMAIL', 'quick.brown@fox.com')]
      ^  ^       ^          ^ 
      |  |       |          |
     Offset      |          └ Text matching the pattern
      |  |       └ Label of the pattern
      |  └ End index
      └ Start index in the text

## Find multiple patterns in the text

To search for different patterns in the text we can use the method `finder.patterns_in_text(text, patterns)` as follows:

```python
from patterns_finder import finder
from patterns_finder.patterns.web import emoji, url, color_hex
from patterns_finder.patterns.number import integer

patterns = [emoji, color_hex, integer]
text = "the quick #A52A2A 🦊 jumped 3 times over the lazy 🐶 "
finder.patterns_in_text(text, patterns)
# Output:
# [(18, 19, 'EMOJI', '🦊'),
#  (49, 50, 'EMOJI', '🐶'),
#  (10, 17, 'COLOR_HEX', '#A52A2A'),
#  (12, 14, 'INTEGER', '52'),
#  (15, 16, 'INTEGER', '2'),
#  (27, 28, 'INTEGER', '3')]
```


## Find user defined patterns in the text

To define new pattern you can use any regex pattern that are supported by the `regex` and `re` packages of python. User defined patterns can be writen in the form of string `regex pattern` or tuple of string `('regex pattern', 'label')`.

```python
patterns = [web.emoji, "quick|lazy", ("\\b[a-zA-Z]+\\b", "WORD") ]
text = "the quick #A52A2A 🦊 jumped 3 times over the lazy 🐶 "
finder.patterns_in_text(text, patterns)
# Output: 
# [(18, 19, 'EMOJI', '🦊'),
#  (49, 50, 'EMOJI', '🐶'),
#  (4, 9, 'quick|lazy', 'quick'),
#  (44, 48, 'quick|lazy', 'lazy'),
#  (0, 3, 'WORD', 'the'),
#  (4, 9, 'WORD', 'quick'),
#  (20, 26, 'WORD', 'jumped'),
#  (29, 34, 'WORD', 'times'),
#  (35, 39, 'WORD', 'over'),
#  (40, 43, 'WORD', 'the'),
#  (44, 48, 'WORD', 'lazy')]
```

## Sort extraxted patterns 

By using the argument `sort_by` of the method `finder.patterns_in_text` we can sort the extraction accoring to different options:
- `sort_by=finder.START` sorts the results by the start index in the text

```python
patterns = [web.emoji, color_hex, ('\\b[a-zA-Z]+\\b', 'WORD') ]
finder.patterns_in_text(text, patterns, sort_by=finder.START)
# Output:
# [(0, 3, 'WORD', 'the'),
#  (4, 9, 'WORD', 'quick'),
#  (10, 17, 'COLOR_HEX', '#A52A2A'),
#  (18, 19, 'EMOJI', '🦊'),
#  (20, 26, 'WORD', 'jumped'),
#  (29, 34, 'WORD', 'times'),
#  (35, 39, 'WORD', 'over'),
#  (40, 43, 'WORD', 'the'),
#  (44, 48, 'WORD', 'lazy'),
#  (49, 50, 'EMOJI', '🐶')]
```

- `sort_by=finder.END` sorts the results by the end index in the text
```python
finder.patterns_in_text(text, patterns, sort_by=finder.END)
# Output:
# [(0, 3, 'WORD', 'the'),
#  (4, 9, 'WORD', 'quick'),
#  (10, 17, 'COLOR_HEX', '#A52A2A'),
#  (18, 19, 'EMOJI', '🦊'),
#  (20, 26, 'WORD', 'jumped'),
#  (29, 34, 'WORD', 'times'),
#  (35, 39, 'WORD', 'over'),
#  (40, 43, 'WORD', 'the'),
#  (44, 48, 'WORD', 'lazy'),
#  (49, 50, 'EMOJI', '🐶')]
```

- `sort_by=finder.LABEL` sorts the results by pattern's label
```python
finder.patterns_in_text(text, patterns, sort_by=finder.LABEL)
# Output:
# [(10, 17, 'COLOR_HEX', '#A52A2A'),
#  (18, 19, 'EMOJI', '🦊'),
#  (49, 50, 'EMOJI', '🐶'),
#  (0, 3, 'WORD', 'the'),
#  (4, 9, 'WORD', 'quick'),
#  (20, 26, 'WORD', 'jumped'),
#  (29, 34, 'WORD', 'times'),
#  (35, 39, 'WORD', 'over'),
#  (40, 43, 'WORD', 'the'),
#  (44, 48, 'WORD', 'lazy')]
```

- `sort_by=finder.TEXT` sorts the results by the extracted text
```python
finder.patterns_in_text(text, patterns, sort_by=finder.TEXT)
# Output:
# [(10, 17, 'COLOR_HEX', '#A52A2A'),
#  (20, 26, 'WORD', 'jumped'),
#  (44, 48, 'WORD', 'lazy'),
#  (35, 39, 'WORD', 'over'),
#  (4, 9, 'WORD', 'quick'),
#  (0, 3, 'WORD', 'the'),
#  (40, 43, 'WORD', 'the'),
#  (29, 34, 'WORD', 'times'),
#  (49, 50, 'EMOJI', '🐶'),
#  (18, 19, 'EMOJI', '🦊')]
```

## Summarize results of extraction

By using the argument `summary_type`, one can choose the desired form of output results.
- `summary_type=finder.NONE` sorts the results by the start index in the text

```python
finder.patterns_in_text(text, patterns, summary_type=finder.NONE)
# Output:
# {
#  'COLOR_HEX': [[10, 17, '#A52A2A']],
#  'WORD': [[0, 3, 'the'], [4, 9, 'quick'], [20, 26, 'jumped'], [29, 34, 'times'], [35, 39, 'over'], [40, 43, 'the'], [44, 48, 'lazy']],
#  'EMOJI': [[18, 19, '🦊'], [49, 50, '🐶']]
# }
```

- `summary_type=finder.START` sorts the results by the start index in the text

```python
finder.patterns_in_text(text, patterns, summary_type=finder.LABEL_TEXT_OFFSET)
# Output:
# {
#  'COLOR_HEX': [[10, 17, '#A52A2A']],
#  'WORD': [[0, 3, 'the'], [4, 9, 'quick'], [20, 26, 'jumped'], [29, 34, 'times'], [35, 39, 'over'], [40, 43, 'the'], [44, 48, 'lazy']],
#  'EMOJI': [[18, 19, '🦊'], [49, 50, '🐶']]
# }
```

## Extract patterns from Pandas DataFrame



# List of patterns

# Web


## email
Description:

Regex:

    (?<=\\s|^)\\w+([-+.']\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*(?=\\s|$|\\.)
Label: **EMAIL**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## url
Description:

Regex:

    ((ftp|https?):\\/\\/(?:www\\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\\.[^\\s]{2,}|www\\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\\.[^\\s]{2,}|https?:\\/\\/(?:www\\.|(?!www))[a-zA-Z0-9]+\\.[^\\s]{2,}|www\\.[a-zA-Z0-9]+\\.[^\\s]{2,})
Label: **URL**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## uri
Description:

Regex:

    \\w+:(\\/?\\/?)[^\\s]+
Label: **URI**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## mailto
Description:

Regex:

    mailto:\\w+([-+.']\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*
Label: **MAILTO**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## html_link
Description:

Regex:

    <\\s*a[^>]*>(.*?)<\\s*\\/\\s*a>
Label: **HTML_LINK**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## sql
Description:

Regex:

    (?i)(?s)\\b(select)\\b(.*?)\\b(from)\\b|\\b(insert)\\b(.*?)\\b(into)\\b|\\b(update)\\b(.*?)\\b(set)\\b|\\b(delete)(.*?)\\b(from)\\b
Label: **SQL**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## color_hex
Description:

Regex:

    #?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})
Label: **COLOR_HEX**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## copyright
Description:

Regex:

    (?:©|\\(c\\)|copyright\\b|(?-i:&copy;|&COPY;)|&#x0{0,3}a9;|&#169;)\\s*(\\d{4})
Label: **COPYRIGHT**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## alphanumeric
Description:

Regex:

    ([-A-Za-z0-9_]*?([-A-Za-z_][0-9]|[0-9][-A-Za-z_])[-A-Za-z0-9_]*)
Label: **ALPHANUMERIC**

Matches:

    matches
Non-Matches:)

    non-matches
Sources:

    sources
## emoji
Description:

Regex:

    [\\U0001F601-\\U0001F64F]|[-\\U0001F680-\\U0001F6C0]|[\\uD800-\\uDBFF]|[\\u2702-\\u27B0]|[\\uF680-\\uF6C0]|[\\u24C2-\\uF251]
Label: **EMOJI**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## username
Description:

Regex:

    [a-zA-Z][a-zA-Z0-9_-]{6,20}
Label: **USERNAME**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## quotation
Description:

Regex:

    ([\"“‘\'])(?:\\\\.|[^\\\\])*?([\"”‘’\'])
Label: **QUOTATION**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## ipv4
Description:

Regex:

    (?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)
Label: **IPV4**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## ipv6
Description:

Regex:

    (([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))
Label: **IPV6**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources


# Phone

## generic
Description:

Regex:

    (\\+\\d{1,3}\\s?)?((\\(\\d{3}\\)\\s?)|(\\d{3})(\\s|-?))(\\d{3}(\\s|-?))(\\d{4})(\\s?(([E|e]xt[:|.|]?)|x|X)(\\s?\\d+))?
Label: **GENERIC**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## uk
Description:

Regex:

    (((\\+44\\s?\\d{4}|\\(?0\\d{4}\\)?)\\s?\\d{3}\\s?\\d{3})|((\\+44\\s?\\d{3}|\\(?0\\d{3}\\)?)\\s?\\d{3}\\s?\\d{4})|((\\+44\\s?\\d{2}|\\(?0\\d{2}\\)?)\\s?\\d{4}\\s?\\d{4}))(\\s?\\#(\\d{4}|\\d{3}))?
Label: **UK**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## us
Description:

Regex:

    (?:\\+?1\\s)?(\\([0-9]{3}\\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}
Label: **US**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources



# Credit Cards

## generic
Description:

Regex:

    \\d{4}(| |-)(?:\\d{4}\\1){2}\\d{4}
Label: **GENERIC**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## visa
Description:

Regex:

    4\\d{3}(| |-)(?:\\d{4}\\1){2}\\d{4}
Label: **VISA**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## mastercard
Description:

Regex:

    5[1-5]\\d{2}(| |-)(?:\\d{4}\\1){2}\\d{4}
Label: **MASTERCARD**

Matches:

    matches
Non-Matches:)

    non-matches
Sources:

    sources
## discover
Description:

Regex:

    6(?:011|5\\d\\d)(| |-)(?:\\d{4}\\1){2}\\d{4}
Label: **DISCOVER**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## american_express
Description:

Regex:

    3[47]\\d{1,2}(| |-)\\d{6}\\1\\d{6}
Label: **AMERICAN_EXPRESS**

Matches:

    matches
Non-Matches:)

    non-matches
Sources:

    sources
import regex





# Numbers

## integer
Description:

Regex:

    (\\-|\\+|±)?\\d+
Label: **INTEGER**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## float
Description:

Regex:

    [\\-\\+±]?\\d+\\.\\d*
Label: **FLOAT**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## scientific
Description:

Regex:

    [+-]?\\d(\\.\\d+)?[Ee][+-]?\\d+
Label: **SCIENTIFIC**

Matches:

    matches
Non-Matches:)

    non-matches
Sources:

    sources
## hexadecimal
Description:

Regex:

    0[xX][0-9a-fA-F]+
Label: **HEXADECIMAL**

Matches:

    matches
Non-Matches:)

    non-matches
Sources:

    sources
## percent
Description:

Regex:

    ([±+-]?\\d{1,4}([,.]\\d{0,2})? ?%)
Label: **PERCENT**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## roman
Description:

Regex:

    (?=[MDCLXVI])(M*)(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})
Label: **ROMAN**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources




# Currency

## monetary
Description:

Regex:

    [\\p{Sc}][\\s]?[0-9.,]+[KMBTkmbt]?
Label: **MONETARY**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## symbol
Description:

Regex:

    [\\p{Sc}]
Label: **SYMBOL**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## code
Description:

Regex:

    GBP|EUR|USD|JPY|CNY|CHF|RUB
Label: **CODE**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## name
Description:

Regex:

    Dirham|Peso|Dollar|Mark|Ruble|Real|Franc|Euro|Koruna|Krone|Dinar|Pound|Sterling|Rial|Won|Rupee|Shilling|Lira|Yuan|Yen
Label: **NAME**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources

# Languages

## english
Description:

Regex:

    [a-zA-Z]+
Label: **ENGLISH**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## french
Description:

Regex:

    [a-zA-Zéàèùâêîôûçäëïüœÿ]+
Label: **FRENCH**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## spanish
Description:

Regex:

    [a-zA-Záéíóúñ]+
Label: **SPANISH**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## arabic
Description:

Regex:

    [\\u0600-\\u06FF]+
Label: **ARABIC**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## hebrew
Description:

Regex:

    [\\u0590-\\u05FF]+
Label: **HEBREW**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## turkish
Description:

Regex:

    [a-zA-ZğüşöçİĞÜŞÖÇ]+
Label: **TURKISH**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## russian
Description:

Regex:

    [\\u0621-\\u064A\\u0660-\\u0669]+
Label: **RUSSIAN**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## german
Description:

Regex:

    [a-zA-Z\\u00E4\\u00F6\\u00FC\\u00C4\\u00D6\\u00DC\\u00df]+
Label: **GERMAN**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## chinese
Description:

Regex:

    [\\u4e00-\\u9fa5]+
Label: **CHINESE**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## greek
Description:

Regex:

    [\\u3131-\\uD79D]+
Label: **GREEK**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## japanese
Description:

Regex:

    [\\u3041-\\u3096\\u30A0-\\u30FF\\u3400-\\u4DB5\\u4E00-\\u9FCB\\uF900-\\uFA6A\\u2E80-\\u2FD5\\uFF5F-\\uFF9F\\u3000-\\u303F\\u31F0-\\u31FF\\u3220-\\u3243\\u3280-\\u337F]+
Label: **JAPANESE**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## hindi
Description:

Regex:

    [\\u0900-\\u097F]+
Label: **HINDI**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## bangali
Description:

Regex:

    [\\u0980-\\u09FF]+
Label: **BANGALI**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## armenian
Description:

Regex:

    [\\u0530-\\u058F]+
Label: **ARMENIAN**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## swedish
Description:

Regex:

    [åäöÅÄÖA-Za-z]+
Label: **SWEDISH**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## portoguese
Description:

Regex:

    [a-zA-Záéíóúçâêôãõà]+
Label: **PORTOGUESE**

Matches:

    matches
Non-Matches:)

    non-matches
Sources:

    sources
## balinese
Description:

Regex:

    [\\u1B00-\\u1B7F]+
Label: **BALINESE**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## georgian
Description:

Regex:

    [\\u10A0-\\u10FF]+
Label: **GEORGIAN**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources

# Time and Date

## time
Description:

Regex:

    ((([0]?[1-9]|1[0-2])(:|-|\\.)[0-5][0-9]((:|-|\\.)[0-5][0-9])?( )?(AM|am|aM|Am|PM|pm|pM|Pm))|(([0]?[0-9]|1[0-9]|2[0-3])(:|-|\\.)[0-5][0-9]((:|-|\\.)[0-5][0-9])?))
Label: **TIME**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## date
Description:

Regex:

    (0?[1-9]|[12][0-9]|3[01])[-/.](0?[1-9]|1[012])[-/.](19|20)?\\d{2}
Label: **DATE**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## year
Description:

Regex:

    (19|20)\\d{2}
Label: **YEAR**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources


# postal code

## us
Description:

Regex:

    \\d{5}(?:-\\d{4})?
Label: **US**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## canada
Description:

Regex:

    [ABCEGHJ-NPRSTVXY]\\d[A-Z][ -]?\\d[A-Z]\\d
Label: **CANADA**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## uk
Description:

Regex:

    [a-zA-Z]{1,2}[0-9][0-9A-Za-z]{0,1}[ -]{0,1}[0-9][A-Za-z]{2}
Label: **UK**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## france
Description:

Regex:

    (?:0[1-9]|[1-8]\\d|9[0-8])\\d{3}
Label: **FRANCE**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## spain
Description:

Regex:

    (?:0[1-9]|[1-4]\\d|5[0-2])\\d{3}
Label: **SPAIN**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources
## switzerland
Description:

Regex:

    [1-9]\\d{3}
Label: **SWITZERLAND**

Matches:

    matches
Non-Matches:)

    non-matches
Sources:

    sources
## brazilian
Description:

Regex:

    \\d{5}-\\d{3}
Label: **BRAZILIAN**

Matches:

    matches
Non-Matches:

    non-matches
Sources:

    sources



