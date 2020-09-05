from string import Template

errno = 501597470054
name = 'Bob'
a = 5
b = 10
templ_string = 'Hey $name, there is a $errno error'
SECRET = 'this-is-a-secret'

print('Hello %s' % name)  # simple string old style
print('%x' % errno)  # implicit conversion of int to string in hex form
print('Hey %s, there is a 0x%x error!' % (name, errno))  # multiple positional reference
print('Hey %(name)s, there is a 0x%(errno)x error!' % {"name": name, "errno": errno})  # dictionary style

# newer style using string.format
print('Hello {}'.format(name))  # implicit
print('Hello {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno))  # explicit

# interpolation (3.6+)
print(f'hello, {name}')
print(f'five plus ten is {a + b} and not {2 * (a + b)}.')
print(f"Hey {name}, there's a {errno:#x} error!")

# template strings (need to import from string import Template)
print(Template(template=templ_string).substitute(name=name, errno=hex(errno)))

# demonstratation of preventing code injection using templates
# use input of ""

class Error:
    def __init__(self):
        pass


err = Error()

user_input = '{error.__init__.__globals__[SECRET]}'
print(user_input.format(error=err))  # this succeeds in extracting data

user_input = '${error.__init__.__globals__[SECRET]}'
try:  # done as try/except to prevent halt of execution
    print(Template(user_input).substitute(error=err))  # this fails
except Exception as e:
    print(e)

# lambda version of string formatting tests
# technically this is more verbose, but it demonstrates lambda more than strings
# note lambda format:
# (lambda input1,input2: input1 operand input2)(a,b)
# this is then enclosed within print()
print((lambda in_str: in_str.upper())("test"))
