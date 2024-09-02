def strFirsttwo(str1):
    c=""
    if(len(str1)>=2):
        a=str1[:2]
        b=str1[len(str1)-2:len(str1)]
        c=a+b
    else:
        return ""
    return c
    
    
print(strFirsttwo("W3resorce"))