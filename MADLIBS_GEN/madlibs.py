try:
    with open("50tory.txt", "r") as s:
        o = s.read()
    o = o.split("||")
    print("Welcome to 50 short story")
    ch = input("Enter the story no for creating a beautiful story :")
    if ch.isdigit():
        ch = int(ch)
    else:
        print("Invalid value,try again")
    story = o[ch - 1]
    placeholders = set()
    startingword = -1
    target_integator = "<"
    endOfTarget = ">"
    for i, char in enumerate(story):
        if char == target_integator:
            startingword = i
        if char == endOfTarget and startingword != -1:
            word = story[startingword:i + 1]
            placeholders.add(word)
            startingword = -1
    answers = {}
    for word in placeholders:
        answer = input("Enter the word for " + word + ": ")
        answers[word] = answer
    for word in placeholders:
        story = story.replace(word, answers[word])
    print(story)
except FileNotFoundError as e:
    print(e)
    print("Opps...! Sorry to interrupt \nOnce again verify that file name was correct")
