import regex


def find_pattern_in_text(text, pattern, text_only=False):
    """Search for a regex_pattern on text."""
    matches = pattern.finditer(text)
    matched_coordinates = []
    matched_texts = []
    for match in matches:
        matched_coordinates.append(
            (match.span()[0], match.span()[1], pattern.label, match.group()))
        matched_texts.append(match.group())
    if text_only:
        return matched_texts
    return matched_coordinates


def extract_patterns_from_df(df, input_cols, patterns):
    """extract patterns from dataframe cols."""
    for input_col in input_cols:
        if input_col in df.cols:
            for pattern in patterns:
                output_col = input_col + "_" + pattern.label
                df[output_col] = df[input_col].apply(
                    lambda text: find_pattern_in_text(str(text), pattern, True
                                                      ))
        else:
            print("KeyWord Error: ", input_col, " is not not found.")
    return df


def extract_patterns_from_text(text, patterns):
    """extract patterns from simple text."""
    patterns_coordinates = []
    for pattern in patterns:
        patterns_coordinates.extend(
            find_pattern_in_text(str(text), pattern))
    patterns_coordinates.sort(key=lambda coordinates: coordinates[1])
    return patterns_coordinates


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
