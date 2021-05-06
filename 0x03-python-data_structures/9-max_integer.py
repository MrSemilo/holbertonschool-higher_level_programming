#!/usr/bin/python3
def multiple_returns(sentence):
    stri = None
    if sentence:
        stri = sentence[0]
    len_sentence = len(sentence)
    return (len_sentence, stri)
