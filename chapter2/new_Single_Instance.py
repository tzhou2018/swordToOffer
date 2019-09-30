class SingleTon(object):
    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingleTon, cls).__new__(cls, *args, **kwargs)
        print (cls._instance)
        return cls._instance[cls]


class MyClass(SingleTon):
    class_val = 22

# 示例 1
class Other(object):
    val = 123

    def __init__(self):
        print ('other instance')


class NoReturn(object):

    def __new__(cls, *args, **kwargs):
        print ('NoReturn __new__')
        return Other()

    def __init__(self, a):
        print (a)
        print ('NoReturn __init__')

t = NoReturn(12)
print (type(t))
# 示例 2
import re

def mul_2(matched):
    val = int(matched.group('val'))
    return str(val * 2)
s = 'A23G4HFD567'
print(re.sub(r'(?P<val>\d+)', mul_2, s))

# re.sub(r'\s', lambda m: '[' + m.group(0) + ']', text, 0)