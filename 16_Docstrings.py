# Docstrings(.__doc__) are used right after the definition 
# of a function, method, class, or module. 
# These are written inbetween triple single quotes '''  '''.
# While python comments are completely ignored by the interpretor,
# docstrings are printed as an output.
# These are used to document the code.

def cube(x=int(input("Enter a number : "))):
    '''This will return the cube of the input integer.'''
    print(x**3);
cube();
print(cube.__doc__); # to acces the docstring use  .__doc__ attribute

# if docstring is not present in the code and still is called, it will display the output
# as 'None'.

