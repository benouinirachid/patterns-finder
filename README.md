# patterns-finder

# list of patterns

# Email
### Description
Check and detect emails.
### Sources
https://regexr.com/3e48o
### Regex 
    "(?<=\\s|^)\\w+([-+.']\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*(?=\\s|$|\\.)"
### Matches
    "h@a.co",
    "me@con.com",
    "not-re_aly@gmail.com",
    "him.him@that.this"
### Non-Matches
    "test@test@s.com",
    "@site.com",
    "test-@not-b.com"
### Tags
email, mail, web

# URL
- Description

- Sources

- Regex

- Matches

- Non-Matches

# URI
- Description
generic URI
- Sources
https://www.regextester.com/94092
- Regex
\w+:(\/?\/?)[^\s]+
- Matches
http://in.im/user/skykey?id=3
https://in.im/
tox:sky@in.com
tox:E214958A86122ACF81BB852D
r:BC767EB8A3A7281A8EDBC
- Non-Matches

# Mailto
- Description
match and detect mailto link.
- Sources

- Regex
    "mailto:\\w+([-+.']\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*"
- Matches

- Non-Matches

# Phone
- Description

- Sources

- Regex

- Matches

- Non-Matches


# HTML
- Description

- Sources

- Regex

- Matches

- Non-Matches

# HTML a tags
- Description

- Sources
https://www.regextester.com/27540
- Regex
<\s*a[^>]*>(.*?)<\s*\/\s*a>
- Matches
Aenean lacinia bibendum <a href="/life">life</a> sed consectetur. <a href="/work">Work</a> quis risus eget urna mol ornare <a href="/about">about</a> leo. <a> me </a>
- Non-Matches


# SQL
- Description
match and detect sql keywords.
- Sources
https://stackoverflow.com/questions/41591777/regex-to-match-sql-keywords-in-c-sharp-code , https://stackoverflow.com/questions/1506699/regular-expression-to-match-select-from-where-sql-queries
- Regex
"(?i)(?s)\b(select)\b(.*?)\b(from)\b|\b(insert)\b(.*?)\b(into)\b|\b(update)\b(.*?)\b(set)\b|\b(delete)(.*?)\b(from)\b"
- Matches

- Non-Matches

# Hex Color
- Description

- Sources

- Regex
    "#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})"
- Matches

- Non-Matches


# ZIP / Postal Code

- US
\d{5}(-\d{4})?$)|(^[ABCEGHJKLMNPRSTVXY]{1}\d{1}[A-Z]{1} *\d{1}[A-Z]{1}\d{1}
https://projects.lukehaas.me/regexhub/

- Canada
\d{5}(-\d{4})?$)|(^[ABCEGHJKLMNPRSTVXY]{1}\d{1}[A-Z]{1} *\d{1}[A-Z]{1}\d{1}
https://projects.lukehaas.me/regexhub/

- France

- UK

- Spain

- Italy

- Brazilian
    
    "[0-9]{5}-[0-9]{3}"

# Languages

## English
desc: 
regex: "[a-zA-Z]+"
source: 

## French
desc: 
regex: "[a-zA-Zéàèùâêîôûçäëïüœÿ]+"
source: https://en.wikipedia.org/wiki/French_language#Writing_system

## Spanish
desc: 
regex: "[a-zA-Záéíóúñ]+"
source: https://stackoverflow.com/questions/896374/what-is-the-regular-expression-for-a-spanish-word

## Arabic
desc: match and validate Arabic characters in a string.
regex: "[\u0600-\u06FF]+"
source: https://regexpattern.com/arabic-characters/
matches:
عبارة
عنوان
الشبكة
non-matches:
Uniform 
123
Abcd

## Hebrew
desc: 
regex: "[\u0590-\u05FF]+"
source: 

## Turkish
desc: 
regex: "[a-zA-ZğüşöçİĞÜŞÖÇ]+"
source: https://stackoverflow.com/questions/16933672/qt-turkish-characters-in-regular-expressions

## Russian
desc: match and validate Russian Cyrillic alphabet characters.
regex: "[\u0621-\u064A\u0660-\u0669]+"
source: https://regexpattern.com/russian-cyrillic-characters/
Matches:
Привет мир
Россия
Москва
Non-matches:
Hello World
Russia
Moscow 

## German
desc: 
regex: "[a-zA-Z\u00E4\u00F6\u00FC\u00C4\u00D6\u00DC\u00df]+"
source: https://www.regextester.com/104175, https://stackoverflow.com/questions/17153545/regex-to-disallow-all-special-chars-but-allow-german-umlauts-in-jquery

## Chinese
desc: Matches any Chinese characters (both Simplified and Traditional Chinese).
regex: "[\u4e00-\u9fa5]+"
source: https://regexpattern.com/chinese-characters/

## Korean (Hangul)
desc: 
regex: "[\u3131-\uD79D]+"
source: https://memory.loc.gov/diglib/codetables/9.3.html , https://stackoverflow.com/questions/38156300/regex-how-do-you-match-korean-hangul-letters-in-javascript-es6

## Greek
desc: 
regex: "[\u0300-\u03E1]+"
source: https://memory.loc.gov/diglib/codetables/53.html , 

## Japanese
desc: 
regex: "[\u3041-\u3096\u30A0-\u30FF\u3400-\u4DB5\u4E00-\u9FCB\uF900-\uFA6A\u2E80-\u2FD5\uFF5F-\uFF9F\u3000-\u303F\u31F0-\u31FF\u3220-\u3243\u3280-\u337F]+"
source: https://regex101.com/r/xhHFs2/1 , https://www.regextester.com/106010

## Hindi
desc: Match and validate text containing Devanagari characters for writing languages such as Hindi, Marathi, Bodo, Maithili, Sindhi, Nepali, and Sanskrit, among others
regex: "[\u0900-\u097F]+"
source: https://www.regular-expressions.info/unicode.html#script , https://stackoverflow.com/questions/41356013/how-to-detect-if-a-string-contains-hindi-devnagri-in-it-with-character-and-wor

## Bangali
desc:
regex: "[\u0980-\u09FF]+"
source: https://www.regular-expressions.info/unicode.html

## Armenian
desc: Match and validate text containing characters for writing the Armenian language.
regex: "[\u0530-\u058F]+"
source: https://www.regular-expressions.info/unicode.html

## Swedish
desc: Match and validate text containing characters for writing the Swedish language.
regex: "[åäöÅÄÖA-Za-z]+"
source: https://stackoverflow.com/questions/39317008/regex-to-match-swedish-words-but-not-numbers


## Portoguese
desc: Match and validate text containing characters for writing the Portoguese language.
regex: "[a-zA-Záéíóúçâêôãõà]+"
source: https://www.regextester.com/115591, https://over.wiki/ask/regular-expression-that-recognizes-words-in-the-portuguese-language-accented-using-python/

## Balinese
desc: 
regex: "[\u1B00-\u1B7F]+"
source: https://en.wikipedia.org/wiki/Unicode_block

## Georgian
desc: Match and validate text containing the Mkhedruli and Asomtavruli Georgian characters used to write Modern Georgian, Svan, and Mingrelian languages.
regex: "[\u10A0-\u10FF]+"
source: https://en.wikipedia.org/wiki/Unicode_block


# Alphanumeric
- Description
Alphanumeric part numbers and references like: 1111_A, AA1AAA or 1-1-1-A, 21A1 and 10UC10P-BACW, abcd-1234, 1234-pqtJK, sft-0021 or 21-1_AB and 55A or AK7_GY.
This can be very useful if you are translating documents that have a lot of alphanumeric codes or references in them, and you need to be able to find them easily.
- Sources
https://atrilsolutions.zendesk.com/hc/en-us/articles/205539861-Useful-regular-expressions
- Regex
"([-A-Za-z0-9_]*?([-A-Za-z_][0-9]|[0-9][-A-Za-z_])[-A-Za-z0-9_]*)"
- Matches

- Non-Matches


# Emoji
desc: A regular expression to match all Emoji-only symbols as per the Unicode Standard.
source: https://regexr.com/3buf8
regex: "[\uD800-\uDBFF]|[\u2702-\u27B0]|[\uF680-\uF6C0]|[\u24C2-\uF251]"

# Username
desc: matches all valid usernames (unique identifier), 6-20 chars, with dash and underscore.
regex: "[a-zA-Z][a-zA-Z0-9_-]{6,20}"
source: https://regexpattern.com/username/

# Password
- Easy
- Medium
- Hard

# IP
- IPv4
"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
- IPv6
"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"
# Social Security Number
- US

# ISBN
- ISBN-10

- ISBN-13

# Quoted String
A regular expression that matches a quoted string, which is a string literal between quotation marks (“).

/"((\\")|[^"(\\")])+"/

https://regexpattern.com/quoted-string/

Matches:
“Regex”
“Regex Pattern”
“Regex\”Pattern”
Non-matches:
‘Regex’
“Regex
Regex Pattern”

# Numbers
- Integer
    (\-|\+|±)?\d+
- Float
desc:
source:
regex: (\-|\+|±)?\d+\.?\d*
matches:
1.10
+10.10
-10.10
±10
non-matches:
--+
-.a
b+

- Hexadecimal
0[xX][0-9a-fA-F]+
https://stackoverflow.com/questions/9221362/regular-expression-for-a-hexadecimal-number

- Percent
regex: "(?<=\s)([+-]?\d{1,4}([,.]\d{0,2})?%)",
description: "Basically this matches into variables for percentages. It allows as much whitespace before the expression.",
sources: ["https://www.regexlib.com/REDetails.aspx?regexp_id=831"],
matches: ["+5.6%","1234.56%","-42.23%"],
nonmatches": ["+5.6", "0.5", "-100", "%23.6"]

- Roman 
desc: Roman numeral, the thousands, hundreds, tens, and units are each captured in their own group.
source: https://rgxdb.com/r/1HXJUYQR
regex: "(?=[MDCLXVI])(M*)(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})"
III match
MCIV match
MMCDXLVI match
IIII	no match
IM	no match

# Copyright year
desc: Matches a copyright with year with HTML encoding allowed. There must be only whitespace characters between the copyright text and the year. This can easily be adjusted.
source: https://rgxdb.com/r/564MOVFC
regex: (?:©|\(c\)|copyright\b|(?-i:&copy;|&COPY;)|&#x0{0,3}a9;|&#169;)\s*(\d{4})

# Credit Cards
source: https://rgxdb.com/

- Generic Credit Card
Major credit card validator. Only checks that the format is 16 digits (optionally separated by hyphens), not the value of any of the digits."

\d{4}(| |-)(?:\d{4}\1){2}\d{4}

- Visa Credit Card
Matches a Visa credit card number.

/^4\d{3}(| |-)(?:\d{4}\1){2}\d{4}$/

4000 0000 0000 0000 match
4000-0000-0000-0000 match
4000000000000000 match
4000-0000 00000000	no match

- Mastercard Credit Card
Matches a MasterCard credit card number.

/^5[1-5]\d{2}(| |-)(?:\d{4}\1){2}\d{4}$/

5100 0000 0000 0000 match
5200-0000-0000-0000 match
5300000000000000 match
4000 0000 0000 0000	no match
5000 0000-0000-0000	no match


- Discover Credit Card
Matches a Discover credit card number.

/^6(?:011|5\d\d)(| |-)(?:\d{4}\1){2}\d{4}$/

6011000000000000 match
6011-0000-0000-0000 match
6011 0000 0000 0000 match
6500000000000000 match
6500-0000-0000-0000 match
6500 0000 0000 0000 match
6011-0000 0000-0000	no match
6000-0000-0000-0000	no match

- American Express Credit Card

Matches an American Express credit card number with hyphens or spaces.

/^3[47]\d{1,2}(| |-)\d{6}\1\d{6}$/

340 000000 000000 match
370-000000-000000 match
3400000000000000 match
3000 0000-0000-0000	no match
3000 0000 0000 0000	no match

# Month

# Day

# Time

# Date

# Year

# MD5

# Cardinals

# Currency

# Vehicle Registration Numbers
https://regexpattern.com/uk-vehicle-registration-numbers/

# Cryptocurrency
- Names
- Address

# File Extension
- Images
".+(\.(gif|png|jpg|jpeg|webp|svg|psd|bmp|tif)"

- Documents 
".+(\.(gif|png|jpg|jpeg|webp|svg|psd|bmp|tif)"

# Hashtag

# mime type

# data type
