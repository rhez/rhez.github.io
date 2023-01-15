from __future__ import print_function
import random, sys

#Given a large piece of text - say, Shakespear's Midsummer Night's Dream,
#produce a new text that is written in the same style.
def associate(reader, context_len):
    '''Return a dictionary where the keys are contexts of length context_len
    from the text in the reader and the value for a key is the list of words
    that were found to follow the key.'''
    words = {}
    context = ('',) * context_len #using context_len words as context
    for line in reader:
        tokens = line.strip().split()
        tokens.append("\n")
        for token in tokens:
            words.setdefault(context,[]).append(token)
            context = context[1:] + (token,)
    return words

def get_context(words, context_len):
    context = [""] * context_len
    s = ""
    for i in range(len(words) - context_len):
        wordlist = words[tuple(context)]
        word = random.choice(wordlist)
        s += word + " " if word != "\n" else "" + "\n"
        context.pop(0)
        context.append(word)
    return s


if __name__ == "__main__":
    f = open('desala.txt', 'r')
    context_len = int(sys.argv[1])
    words = associate(f, context_len)
    print(get_context(words, context_len))