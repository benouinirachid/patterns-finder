""""regex patterns definitions."""

def select_patterns(patterns_dict, selected_labels):
    """Select a list of pattern from a dict of patterns."""
    selected_patterns = {}
    for label in selected_labels:
        if label in patterns_dict.keys():
            selected_patterns[label] = patterns_dict[label]
    return selected_patterns

patterns = {
    "Company-Number": {
        "regex":
        "\d{8}|(AC|BR|CE|FC|GE|GN|GS|IC|IP|LP|NA|NF|NI|NL|NO|NP|NR|NZ|OC|RC|RS|SA|SC|SF|SI|SL|SO|SP|SR|SZ|ZC|R)\d{5,6}[CDFLR]?",
        "label":"Company-Number",
        "description":
        "UK Company Registration Number.",
        "sources": [
            "https://gist.github.com/rob-murray/01d43581114a6b319034732bcbda29e1"
        ],
        "matches": [],
        "non-matches": []
    },
    "Year": {
        "regex": "(?<=\s)(19|20)\d{2}(?=\s)",
        "label":"Year",
        "description": "",
        "sources": [],
        "matches": ["2013", "1989", "2003"],
        "non-matches": ["232019", "2300", "20190", "22.2003"]
    },
    "Date": {
        "regex":
        "(0?[1-9]|[12][0-9]|3[01])[-/.](0?[1-9]|1[012])[-/.][19|20]?\d\d",
        "label": "Date",
        "description": "Detect general data format",
        "sources": [],
        "matches": ["1:01 AM", "1-01 AM", "23:52:01", "03.24.36 AM"],
        "non-matches": ["19:31 AM", "9:9 PM", "25:60:61"]
    },
    "Time": {
        "regex":
        "(?<=(\s))((([0]?[1-9]|1[0-2])(:|-|\.)[0-5][0-9]((:|-|\.)[0-5][0-9])?( )?(AM|am|aM|Am|PM|pm|pM|Pm))|(([0]?[0-9]|1[0-9]|2[0-3])(:|-|\.)[0-5][0-9]((:|-|\.)[0-5][0-9])?))",
        "label":"Time",
        "description": "Detect general data format.",
        "sources": [],
        "matches": [],
        "non-matches": []
    },
    "Credit-Card": {
        "regex": "\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}",
        "label":"Credit-Card",
        "description": "Major credit card validator. Only checks that the format is 16 digits (optionally separated by hyphens), not the value of any of the digits.",
        "sources": ["https://regexlib.com/REDetails.aspx?regexp_id=29"],
        "matches": ["1111-2323-2312-3434", "1234343425262837", "1111 2323 2312 3434"],
        "non-matches": ["1111 2323 2312-3434", "34323423", "1111-2323-23122-3434"]
    },
    "Email": {
        "regex": "(?<=\s)\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*",
        "label":"Email",
        "description": "Detect emails.",
        "sources": ["https://regexr.com/3e48o"],
        "matches": ["h@a.co","me@con.com","not-re_aly@gmail.com","him.him@that.this"],
        "non-matches": ["djhqdjk@g_ch@s.com", "@sss.com", "b-@b-b.com"]
    },
    "Email_v0": {
        "regex": "\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*",
        "label":"Email",
        "description": "",
        "sources": [],
        "matches": [],
        "non-matches": []
    },
    "URL":{
        "regex": "((ftp|https?):\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})",
        "label":"URL",
        "description": "",
        "sources": ["https://stackoverflow.com/posts/17773849/revisions", "https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url"],
        "matches": [],
        "non-matches": []
    },
    "URL_v0": {
        "regex":
        "((http|https)\\:\/\/)?[a-zA-Z0-9\\.\/\\?\\:@\\-_=#]+\\.([a-zA-Z]){2,6}([a-zA-Z0-9\\.\\&\/\\?\\:@\\-_=#])*",
        "label":"URL",
        "description": "",
        "sources": [],
        "matches": [],
        "non-matches": []
    },
    "Monetary": {
        "regex":
        "[\p{Sc}][\s]?[0-9.,]+[KMBTkmbt]?",
        "label":"Monetary",
        "description":
        "Detects monetary values and amounts.",
        "sources": [
            "https://stackoverflow.com/questions/14169820/regular-expression-to-match-all-currency-symbols"
        ],
        "matches": ["$50m", "$50.2m", "$10,000,00", "$10000", "¥ 1M", "€50m"],
        "non-matches": ["$", "¥", "10", "M" "10.00$"]
    },
    "Phone": {
        "regex":
        "(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}",
        "label":"Phone",
        "description": "Match standard 10 digit phone number.",
        "sources": ["https://regex101.com/r/DsaRfI/1"],
        "matches": ["+1 (800) 123-4567", "18001234567", "1 800 123 4567"],
        "non-matches": ["1.800.123@4567", "+1 123-4567", "180234567", "12 800 129.45"]
    },
    "Postal-Code": {
        "regex": "[a-zA-Z]{1,2}[0-9][0-9A-Za-z]{0,1} {0,1}[0-9][A-Za-z]{2}",
        "label":"Postal-Code",
        "description": "UK Postcode regular expression that should prevent the majority of miskeying.",
        "sources": ["https://regexlib.com/REDetails.aspx?regexp_id=38"],
        "matches": ["W1A 1AA", "EC2V 1JN", "GIR 0AA"],
        "non-matches": ["TB12 1AB", "EC2V 1JM", "W2A 1AA"]
    },
    "Percent": {
        "regex": "(?<=\s)([+-]?\d{1,4}([,.]\d{0,2})?%)",
        "label":"Percent",
        "description": "Basically this matches into variables for percentages. It allows as much whitespace before the expression.",
        "sources": ["https://www.regexlib.com/REDetails.aspx?regexp_id=831"],
        "matches": ["+5.6%","1234.56%","-42.23%"],
        "non-matches": ["+5.6", "0.5", "-100", "%23.6"]
    }
}
