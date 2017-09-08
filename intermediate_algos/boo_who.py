def boo(b):
    if type(b) is bool:
        return True
    else:
        return False
        
        
print(boo(True))
print(boo(False))
print(boo("Hello"))
print(boo(1))
print(boo([1,2,3]))
    