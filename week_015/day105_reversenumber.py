def reverse(self, x: int)
    is_negative = False
    if x < 0:
        is_negative = True
    
    num = str(x)
    
    if is_negative:
        num = num[1:][::-1]
    else:
        num = num[::-1]
    
    num = int(num)
    
    if is_negative:
        num *= -1
    
    if num > 2147483647 or num < -2147483648:
        return 0
    return num