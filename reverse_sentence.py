from typing import Sequence


def reverse_sentence(sentence):
    stack = []
    reversed_sentence = ""

    for word in sentence.split():
        stack.append(word)

    while len(stack)>0:
        reversed_sentence += stack.pop()+" "

    return reversed_sentence.strip()

Sentence = "Good Morning, How are you?"
print(reverse_sentence(Sentence))