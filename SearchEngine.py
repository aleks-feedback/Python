text = input()
word = input()
def search(text, word):
    if word in text:
        return ("Word found")
    else:
        return("Word not found") 
print(search(text, word))

'''The search() function should return "Word found" 
 if the word is present in the text, or "Word not found", if it’s not.'''