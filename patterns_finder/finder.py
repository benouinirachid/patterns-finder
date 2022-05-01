from .patterns import Pattern

NONE = None
START = "start"
END = "end"
LABEL = "label"
TEXT = "text"

START_INDEX = 0
END_INDEX = 1
LABEL_INDEX = 2
TEXT_INDEX = 3

LABEL_TEXT_OFFSET = "label_text_offset"
LABEL_TEXT = "label_text"
TEXT_ONLY = "text_only"


def pattern_in_text(text, pattern):
    """Search for a regex_pattern on text."""
    matched_coordinates = []
    # find all the occurences of pattern in the text.
    matches = pattern.finditer(text)
    for match in matches:
        # get start, end, label and group of text matching the pattern
        matched_coordinates.append(
            (match.span()[0], match.span()[1], pattern.label, match.group()))
    return matched_coordinates


def build_patterns_list(patterns):
    _patterns = []
    for element in patterns:
        if isinstance(element, Pattern):
            # if: it's already of Pattern type
            # then: we add it as it is
            _patterns.append(element)
        elif isinstance(element, str):
            # if: it's a string like "pattern"
            # then: we will add a Pattern instance with pattern="regex" and label"pattern"
            _patterns.append(Pattern(element, element))
        elif isinstance(element, tuple):
            # if: it's a tuple it should be in the form ("regex", "label")
            # then: we will add a Pattern instance with "regex" and "label"
            if isinstance(element[0], str) and isinstance(element[1], str):
                _patterns.append(Pattern(element[0], element[1]))
            else:
                raise Exception(
                    "The pattern tuple must in the form (str,str), like ('\\w+','word')"
                )
        else:
            raise Exception("Unsuported type of input.")
    return _patterns


def summarize(coordinates, summary_type=None):
    if summary_type is None:
        summary = coordinates
    elif summary_type == LABEL_TEXT_OFFSET:
        summary = {}
        for element in coordinates:
            if element[LABEL_INDEX] not in summary:
                summary[element[LABEL_INDEX]] = []
            summary[element[LABEL_INDEX]].append([
                element[START_INDEX], element[END_INDEX], element[TEXT_INDEX]
            ])
    elif summary_type == LABEL_TEXT:
        summary = {}
        for element in coordinates:
            if element[LABEL_INDEX] not in summary:
                summary[element[LABEL_INDEX]] = []
            summary[element[LABEL_INDEX]].append(element[TEXT_INDEX])
    elif summary_type == TEXT_ONLY:
        summary = []
        for element in coordinates:
            summary.append(element[TEXT_INDEX])
    else:
        raise Exception(
            "The value of summary_type should be one of the following:" +
            " None, LABEL_TEXT_OFFSET, LABEL_TEXT or TEXT_ONLY.")
    return summary


def patterns_in_text(text,
                     patterns,
                     skip_build=False,
                     sort_by=None,
                     summary_type=None):
    """extract patterns from simple text.
    sort: None,  start, end, label, text
    skip_build: bool, True, False
    """
    patterns_coords = []
    if skip_build:
        # this allows to skip build and compile patterns if they are already compiled
        patterns_ = patterns
    else:
        # rebuild the patterns list with element from the Pattern class.
        patterns_ = build_patterns_list(patterns)

    for pattern in patterns_:
        # extract results for each pattern
        patterns_coords.extend(pattern_in_text(text, pattern))

    # sort results according to
    if sort_by is NONE:
        # no sort is required
        pass
    elif sort_by == START:
        patterns_coords.sort(key=lambda coords: coords[START_INDEX])
    elif sort_by == END:
        patterns_coords.sort(key=lambda coords: coords[END_INDEX])
    elif sort_by == LABEL:
        patterns_coords.sort(key=lambda coords: coords[LABEL_INDEX])
    elif sort_by == TEXT:
        patterns_coords.sort(key=lambda coords: coords[TEXT_INDEX])
    else:
        raise Exception(
            "The value of sort should be one of the following None, 'start', 'end', 'label' or 'text'."
        )
    # summarize results
    patterns_coords = summarize(patterns_coords, summary_type=summary_type)

    return patterns_coords


def patterns_in_df(df,
                   input_col,
                   output_col,
                   patterns,
                   skip_build=False,
                   sort_by=None,
                   summary_type=None):
    """extract patterns from dataframe cols."""
    if input_col not in df.columns:
        print("KeyWord Error: ", input_col, " is not not found.")

    if skip_build:
        # this allows to skip build and compile patterns if they are already compiled
        patterns_ = patterns
    else:
        # rebuild the patterns list with element from the Pattern class.
        patterns_ = build_patterns_list(patterns)

    df[output_col] = df[input_col].apply(
        lambda text: patterns_in_text(text,
                                      patterns_,
                                      skip_build=True,
                                      sort_by=sort_by,
                                      summary_type=summary_type))

    return df


def get_patterns_annotations(text, patterns_coordinates):
    if len(patterns_coordinates) == 0:
        return [text]
    else:
        start = 0
        end = len(text)
        start_, end_, _, _ = patterns_coordinates[0]
        annotated_text = []
        for i in range(len(patterns_coordinates)):
            start_, end_, label, _ = patterns_coordinates[i]
            if start_ != start:
                annotated_text.append(text[start:start_])
                annotated_text.append((text[start_:end_], label))
                # print(i, " ", start,start_, "o")
                # print(i, " ", start_,end_, label)
                start = end_
            else:
                annotated_text.append((text[start_:end_], label))
                # print(i, " ", start_,end_, label)
                start = end_

        if end_ != end:
            annotated_text.append(text[end_:end])
            # print(i, " ", end_, end, "o")
        return annotated_text
