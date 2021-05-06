from random import choice
from string import  ascii_uppercase,ascii_lowercase
let=ascii_uppercase+ascii_lowercase
def randchoes(let,len):
    a=choice(let)
    for i in range(len-1):
        a+=choice(let)
    return a
