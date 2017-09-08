
def string_to_bin(string):
    result = ''
    for l in string:
        if l.isalpha():
            result += bin(ord(l))
        else:
            result += '0' + bin(ord(l))
    return result

def bin_to_string(zeros_and_ones):
    zeros_and_ones = zeros_and_ones.replace('b', '')
    return zeros_and_ones

def magic(string):
    data_bin = string_to_bin(string)
    data_bin = data_bin.replace('b', '')

    print('Original string: %s' % (string))
    print('Binary data: %s' % (data_bin))

magic('def test(): return 1 + 1')


