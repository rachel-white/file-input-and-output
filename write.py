f = open('newfile.txt', 'a')
lines = ["Hello", "good morning", "greetings", "bonjour", "shalom"]
text = '\n'.join(lines)
f.writelines(text)
f.close()

