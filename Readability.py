#!/usr/bin/env python3
import re
from cs50 import get_string


def main():
    getText = get_string("Text: ")
    index = calculateCL(getText)

    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def countWords(text):
    words = text.split()
    return len(words)


def countLetters(text):
    numLetters = 0
    for char in text:
        if char.isalpha():
            numLetters += 1
    return numLetters


def countSentences(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)


def calculateCL(text):
    numWords = countWords(text)
    numLetters = countLetters(text)
    numSentences = countSentences(text)

    L = (numLetters / numWords) * 100
    S = (numSentences / numWords) * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)
    print(numWords, numLetters, numSentences)
    return index


main()
