
#manipulating strings
phrase = "learn python";
print("jason\npeters")
print(phrase.lower() + "is very good");
print(phrase.islower())
print(phrase.upper() + "is very good")
print(phrase.isupper())
print("the length is " + str(len(phrase)))
print("first char is " + phrase[0])
print("the index of n is " + str(phrase.index("n"))) # return the index of the first occurrence
print(phrase.replace("python","python 3.7"))

string = ""
if  string:
    print (True)
else:
    print(False)

print (string.__contains__("g"))

print (string.__len__())

print(phrase[1:2])
print(phrase[1:])