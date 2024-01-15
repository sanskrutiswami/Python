Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
str='You can use two or more specially designated characters within a string to format a string or perform a command. These characters are called escape sequences. An escape sequence in Python starts with a backslash (\). For example, \n is an escape sequence in which the common meaning of the letter n is literally escaped and given an alternative meaning - a new line.Displayed here are a few common escape sequences available in Python.'
print(str)
You can use two or more specially designated characters within a string to format a string or perform a command. These characters are called escape sequences. An escape sequence in Python starts with a backslash (\). For example, 
 is an escape sequence in which the common meaning of the letter n is literally escaped and given an alternative meaning - a new line.Displayed here are a few common escape sequences available in Python.
str='''You can use two or more specially designated characters within a string to format a string or perform a command. These characters are called escape sequences. An escape sequence in Python starts with a backslash (\). For example, \n is an escape sequence in which the common meaning of the letter n is literally escaped and given an alternative meaning - a new line.Displayed here are a few common escape sequences available in Python.'''
 
print(str)
 
You can use two or more specially designated characters within a string to format a string or perform a command. These characters are called escape sequences. An escape sequence in Python starts with a backslash (\). For example, 
 is an escape sequence in which the common meaning of the letter n is literally escaped and given an alternative meaning - a new line.Displayed here are a few common escape sequences available in Python.
str='''You can use two or more specially designated characters within a string to format a string or perform a command.
 These characters are called escape sequences. An escape sequence in Python starts with a backslash (\).
For example, \n is an escape sequence in which the common meaning of the letter n is literally escaped and given an alternative meaning - a new line.
Displayed here are a few common escape sequences available in Python.'''
 
print(str)
 
You can use two or more specially designated characters within a string to format a string or perform a command.
 These characters are called escape sequences. An escape sequence in Python starts with a backslash (\).
For example, 
 is an escape sequence in which the common meaning of the letter n is literally escaped and given an alternative meaning - a new line.
Displayed here are a few common escape sequences available in Python.
str= '''You can' use "two or more" specially designated characters within a string to format a string or perform a command. These characters are called escape sequences. An escape sequence in Python starts with a backslash (\). For example, \n is an escape sequence in which the common meaning of the letter n is literally escaped and given an alternative meaning - a new line.'''
print(str)

print(str)
You can' use "two or more" specially designated characters within a string to format a string or perform a command. These characters are called escape sequences. An escape sequence in Python starts with a backslash (\). For example, 
 is an escape sequence in which the common meaning of the letter n is literally escaped and given an alternative meaning - a new line.
str='You can\' \"use two or more"\ specially designated characters within a string to format a string or perform a command.\n These characters are called escape sequences. An escape sequence in Python starts with a backslash (\).\n For example, \n is an escape sequence in which the common meaning of the letter n is literally escaped and given an alternative meaning - a new line.Displayed here are a few common escape sequences available in Python.'
print(str)
You can' "use two or more"\ specially designated characters within a string to format a string or perform a command.
 These characters are called escape sequences. An escape sequence in Python starts with a backslash (\).
 For example, 
 is an escape sequence in which the common meaning of the letter n is literally escaped and given an alternative meaning - a new line.Displayed here are a few common escape sequences available in Python.
a='name'
 
b='surname'
 
print(a+b)
 
namesurname
print(a+\t b)
 
SyntaxError: unexpected character after line continuation character
print(a' '+b)
 
SyntaxError: invalid syntax
print(a+' '+b)
 
name surname
print(a+\t+b)
 
SyntaxError: unexpected character after line continuation character
b='hello world'
 
print(b*6)
 
hello worldhello worldhello worldhello worldhello worldhello world
print(b[1]*4)
 
eeee
