# definition of the main pattern class
import regex


class Pattern():
    """Pattern class that associate a label with regex."""

    def __init__(self, pattern, label, flags=regex.V0):
        # Compile the regex and init the label
        self.pattern = regex.compile(pattern, flags)
        self.label = label
        # The following initialization will allow the object to act
        # as an instance of the regex._regex.Pattern class
        self.search = self.pattern.search
        self.findall = self.pattern.findall
        self.finditer = self.pattern.finditer
        self.match = self.pattern.match
        self.fullmatch = self.pattern.fullmatch
        self.scanner = self.pattern.scanner
        self.split = self.pattern.split
        self.splititer = self.pattern.splititer

    def find(self, text):
        """Search for a pattern on text."""
        matched_coords = []
        # find all the occurences of pattern in the text.
        matches = self.pattern.finditer(text)
        for match in matches:
            # get start, end, label and group of text matching the pattern
            matched_coords.append(
                (match.span()[0], match.span()[1], self.label, match.group()))
        return matched_coords
