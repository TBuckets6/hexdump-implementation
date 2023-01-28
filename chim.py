
from typing import Any, Union

from typing_extensions import TypeAlias

sequence: TypeAlias = Union[list, range, tuple, str]
number: TypeAlias = Union[int, float]
'''
#print(number)

x: TypeAlias = 'chim'

#print(x)    

f = open("hi.txt", "r")
#print(f.read())


#str = 'hiiiii'.encode('utf-8')
#print(str.hex())

def f(seq: sequence, index: int) -> Any:
    return seq[index]

l = ['a','b','c']
#print(l[-1])

x = f(['zip','zop','swiffft'],1)
#print(x)

num = [1,2,3]
print(sum(num))
def func():
    l = [1,2,3,4,5]
    for element in l:
        if element == 2:
            return 'yooo'

x = func()
print(x)
if not a:
  print("List is empty"
'''
def all_even(l) -> bool:
    """Return true iff every element in seq is an even integer (or seq is empty)."""
    for element in l:
        if not l:
            return True 
x = all_even([1,234])
print(x)

