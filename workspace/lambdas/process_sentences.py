"""
# Process Sentences Python (Assignment)

## Problem Statement

Given a list of strings `sentences` representing sentences, write a Python method called `processSentences` that performs the following operations:

-   Filter out sentences that contain the word `"python"`.
-   Map each filtered sentences to its length.
-   Find the average length of the sentences.
-   Convert the average length to an integer by rounding down.
-   Return the rounded average length.

## Instructions

1.  Implement the `processSentences` method inside the `processSentence.py` file
2.  Return the rounded down average length.
"""
def processSentences(sentences):

    if len(sentences) == 0:
        return 0

    python_sentences = list(filter(lambda sentence: 'python' in sentence.lower(), sentences))
    python_lengths = list(map(lambda sentence: len(sentence), python_sentences))

    avg_length = 0
    if len(python_lengths) > 0:
        avg_length = int(sum(python_lengths)/len(python_lengths))

    return avg_length
