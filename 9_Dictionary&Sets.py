# Dictionary is the collection of keyvalue pairs.
dict1 = {"int" : "integer value", "char" : "character value", "vsccode" : "visualstudiocode",
"numbers": "1,2,3,4,5,6,,7,8,9,0" , 'dict2' : {'greetings':'hello there!'}}
print(dict1['int'])
print(dict1['char'])
print(dict1['numbers'])
print(dict1['dict2']) # dictionary in another dictionary
print(dict1['dict2'][ 'greetings'])
