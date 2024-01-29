languages =['php', 'java', 'python', 'javascript']

print("language select " + languages[2])

languages[2] = "Djgango"
print("language select " + languages[2])

languages.append("groovy")

print(languages)
languages.remove('java')
print(languages)