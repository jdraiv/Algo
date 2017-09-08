
def roman_converter(num):
    keys = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    roman = ''

    while num > 0:
        for i, r in keys:
            while num >= i:
                roman += r
                num -= i
                
    return roman
    
print(roman_converter(2))
print(roman_converter(5))
print(roman_converter(83))
