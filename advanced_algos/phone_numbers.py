#Return true if the passed string is a valid US phone number.
import string


def valid(arr,num):
    if num in arr:
        return True
    else:
        return False


def valid_number(num):
    result = ""
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    
    valid_num = ['555-555-5555', '5-555-555-5555']
    
    num_two = num.replace("-","").replace(" ", "").replace("(","").replace(")","")
    
    if len(num_two) == 11 and num_two[0] != '1':
        print(False)
        return
    
    print(result)
    
    for n in num:
        
        if n in numbers:
            result += str(5)
        elif n == '-' or n == ' ':
            result += '-'
        elif n == '(' or n == ')':
            pass
            
            
    is_valid = valid(valid_num,result)
    print(is_valid)
            
        
valid_number('456-789-2222')
valid_number('456 789 4444')
valid_number('1 222-333-5467')
valid_number('1 (555) 555-5555')
valid_number('1 555)555-5555')
valid_number("55554665")
valid_number("-1 (757) 622-7382")
valid_number("2(757)622-7382")
valid_number("(555)5(55?)-5555")

