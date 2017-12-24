

# Rot 13 challenge solution

import string


def rot13(s):
    def new_l(l):
        def upper_or_lower(b, value):
            if b:
                return value.upper()
            else:
                return value

        alphabet = list(string.ascii_lowercase)
        upper = None

        if l.istitle():
            upper = True

        try:
            # Find index
            index = alphabet.index(l.lower())

            new_index = index + 13

            if new_index >= len(alphabet):
                new_index -= len(alphabet)

            return upper_or_lower(upper, alphabet[new_index])
        except ValueError:
            return l

    result = [new_l(l) for l in s]
    return ''.join(result)
