print("=======By the end of Day 5, you'll be able to build text-processing features that are heavily used in chatbots, LLM prompts, and AI applications.========")
print("======String slicing========")
text = "Python"


print(text[0:2])
print(text[2:5])
print(text[:4])
print(text[3:])
print(text[:])


print("=====Steps in Strings")
text = "Python"

print(text[::2])
print(text[::-1])

print("====string length")
string = "Noman"
print(len(string))


print("====String Cancatenation")

first = "Hello"
second= "Noman"
print(first + " " + second)     #Hello Noman

print("===String repitition")
print("Noman "*10)


print("=========Membership operators=====")
text = "python"
print("p" in text)   #true
print("h" in text)    #true
print("z" not in text)   #true



text = "he is my best friend"
print(text.title())


text = "   Hello Noman   "
print(text)
print(text.strip())
print(text.split())


text = "Hello"
print(text)
print(text.count("l"))
print(text.replace("Hello", "Noman"))
print(len(text))
print("a" in text)
print(text.startswith("Hel"))




text =  "   Welcome Noman    "
print(text.capitalize())
print(text.endswith("man"))
print(text.find("com"))
print(text.count("o"))
print(text.index("c"))
print(text.isalpha())
print(text.isalnum())
print(text.isdigit())
print(text.islower())
print(text.isprintable())
print(text.isupper())
print(text.lstrip())
print(text.rstrip())
print(text.isspace())
print(text.replace("Noman","Ai engineer"))
print(text.split(" , "))
print(text.startswith("Wel"))
print(text.title())


