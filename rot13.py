def rot13(message):      
    rot13 = []   
    for i in message:
        if i.isupper():
            if ord(i)+13 > 90:                
                rot13.append(chr(ord(i)-13))
            else:                
                rot13.append(chr(ord(i)+13))
        elif i.islower():
            if ord(i)+13 > 122:                 
                rot13.append(chr(ord(i)-13))
            else:                
                rot13.append(chr(ord(i)+13))
        else: rot13.append(i)                
    return "".join(rot13)       

mess = input('Enter your message: ')
print(rot13(mess))
