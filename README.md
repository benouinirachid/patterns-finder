# patterns-finder

Simple, Fast, Powerful and Easily extensible python package for extracting patterns from text, with over than 60 predefined Regular Expressions.

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

The results provided by the method `find` for each of pattern are in the form:
    
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
- `summary_type=finder.NONE` retruns a list with all details, without summarization.

```python
patterns = [ color_hex, ('\\b[a-zA-Z]+\\b', 'WORD'), web.emoji ]
finder.patterns_in_text(text, patterns, summary_type=finder.NONE)
# Output:
# [(10, 17, 'COLOR_HEX', '#A52A2A'),
#  (0, 3, 'WORD', 'the'),
#  (4, 9, 'WORD', 'quick'),
#  (20, 26, 'WORD', 'jumped'),
#  (29, 34, 'WORD', 'times'),
#  (35, 39, 'WORD', 'over'),
#  (40, 43, 'WORD', 'the'),
#  (44, 48, 'WORD', 'lazy'),
#  (18, 19, 'EMOJI', '🦊'),
#  (49, 50, 'EMOJI', '🐶')]
```

- `summary_type=finder.LABEL_TEXT_OFFSET` returns a dictionary of patterns labels as keys, with the corresponding offsets and text as values. 

```python
finder.patterns_in_text(text, patterns, summary_type=finder.LABEL_TEXT_OFFSET)
# Output:
# {
#  'COLOR_HEX': [[10, 17, '#A52A2A']],
#  'WORD': [[0, 3, 'the'], [4, 9, 'quick'], [20, 26, 'jumped'], [29, 34, 'times'], [35, 39, 'over'], [40, 43, 'the'], [44, 48, 'lazy']],
#  'EMOJI': [[18, 19, '🦊'], [49, 50, '🐶']]
# }
```

- `summary_type=finder.LABEL_TEXT` returns a dictionary of patterns labels as keys, with the corresponding text (without offset) as values. 

```python
finder.patterns_in_text(text, patterns, summary_type=finder.LABEL_TEXT)
# Output:
# {
#  'COLOR_HEX': ['#A52A2A'],
#  'WORD': ['the', 'quick', 'jumped', 'times', 'over', 'the', 'lazy'],
#  'EMOJI': ['🦊', '🐶']
# }
```

- `summary_type=finder.TEXT_ONLY` returns a list of the extracted text only. 

```python
finder.patterns_in_text(text, patterns, summary_type=finder.TEXT_ONLY)
# Output:
# ['#A52A2A', 'the', 'quick', 'jumped', 'times', 'over', 'the', 'lazy', '🦊', '🐶']
```

## Extract patterns from Pandas DataFrame

This package provides the capability to extract patterns from Pandas' DataFrame easily, by using the method `finder.patterns_in_df(df, input_col, output_col, patterns, ...)`.

```python
from patterns_finder import finder
from patterns_finder.patterns import web
import pandas as pd

patterns = [web.email, web.emoji, web.url]

df = pd.DataFrame(data={
    'text': ["the quick #A52A2A 🦊 jumped 3 times over the lazy 🐶",
                    "quick.brown@fox.com is the email of 🦊",
                    "The lazy 🐶 has a website https://lazy.dog.com"],
    })

finder.patterns_in_df(df, "text", "extraction", patterns, summary_type=finder.LABEL_TEXT)
# Output:
# |    | text                                                 | extraction                                          |
# |---:|:-----------------------------------------------------|:----------------------------------------------------|
# |  0 | the quick #A52A2A 🦊 jumped 3 times over the lazy 🐶 | {'EMOJI': ['🦊', '🐶']}                            |
# |  1 | quick.brown@fox.com is the email of 🦊               | {'EMAIL': ['quick.brown@fox.com'], 'EMOJI': ['🦊']} |
# |  2 | The lazy 🐶 has a website https://lazy.dog.com       | {'EMOJI': ['🐶'], 'URL': ['https://lazy.dog.com']}  |
```
The method `finder.patterns_in_df` have also the arguments `summary_type` and `sort_by`.

# List of all predefined patterns

- Web
```python
from patterns_finder.web import email, url, uri, mailto, html_link, sql, color_hex, copyright, alphanumeric, emoji, username, quotation, ipv4, ipv6
```

- Phone
```python
from patterns_finder.phone import generic, uk, us
```

- Credit Cards
```python
from patterns_finder.credit_card import generic, visa, mastercard, discover, american_express
```

- Numbers
```python
from patterns_finder.number import integer, float, scientific, hexadecimal, percent, roman
```

- Currency
```python
from patterns_finder.currency import monetary, symbol, code, name
```

- Languages
```python
from patterns_finder.language import english, french, spanish, arabic, hebrew, turkish, russian, german, chinese, greek, japanese, hindi, bangali, armenian, swedish, portoguese, balinese, georgian
```

- Time and Date
```python
from patterns_finder.time_date import time, date, year
```

- Postal Code
```python
from patterns_finder.postal_code import us, canada, uk, france, spain, switzerland, brazilian
```

# Contact

Please email your questions or comments to [me](mailto:benouini.rachid@gmail.com).
