text = "Hi welcome to python "
print(text)

print(text[3])
print(text[5:15])  # range of text
print(text[5:])  # start 5 character until end
print(text[-6:]) # print from back to front only 6 characters

name="juan pietro"
print(name.upper())
print(name.lower())
print(name.capitalize())

chains = "php,java,selenium,javascript"
print(chains.split(','))
name2="laura"
lastname="Perez"
slastname = "zaens"

print(" you name {} you first lastname {} and your second lastname {}".format(name2,lastname,slastname))