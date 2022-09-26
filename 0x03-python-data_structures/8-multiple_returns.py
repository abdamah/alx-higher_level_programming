#!/usr/bin/python3
def multiple_returns(sentence):
    """It return length of a string and first char of sentence"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
