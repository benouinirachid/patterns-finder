# definition of the main pattern class
import regex


class Pattern():

    def __init__(self, pattern, label, flags=regex.V0):
        # Compile the regex and init the label
        self.pattern = regex.compile(pattern, flags)
        self.label = label
        # The following initialization will allow the object to act
        # as an instance of the regex._regex.Pattern
        self.search = self.pattern.search
        self.findall = self.pattern.findall
        self.finditer = self.pattern.finditer
        self.match = self.pattern.match
        self.fullmatch = self.pattern.fullmatch
        self.scanner = self.pattern.scanner
        self.split = self.pattern.split
        self.splititer = self.pattern.splititer
