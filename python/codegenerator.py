import string
import random

if __name__ == "__main__":
    lw = string.ascii_lowercase
    up = string.ascii_uppercase
    dgt = string.digits #1-0
    symbl = string.punctuation # (*&^%&*&%$E#$%^&*())
    
    length = int(input("Enter password length \n"))
    s= []
    s.extend(list(lw))
    s.extend(list(up))
    s.extend(list(dgt))
    s.extend(list(symbl))
 
    # random.shuffle(s)
    # pw = ("".join(s[0:length]))
    pw = ("".join(random.sample(s,length)))
    print(pw)
    