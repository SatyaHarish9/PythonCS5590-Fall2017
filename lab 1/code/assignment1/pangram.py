from string import ascii_lowercase
print(ascii_lowercase)
def pangram(input_string):
    return(set(ascii_lowercase).issubset(input_string))
input_string = input("enter the string")
print(pangram(input_string))


