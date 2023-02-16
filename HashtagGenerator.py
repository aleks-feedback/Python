usertext = input()

def hashtag(usertext):
    text = usertext.replace(" ", "")
    return "#" + text
    
print(hashtag(usertext))