def yourchoice():
    try:
        with open("50story.txt", "r") as s:
            o = s.read()
        o = o.split("||")
        print('''Welcome to 50 short story
        \n1:The Adventure
        \n2:The Magical Forest
        \n3:The Cosmic Adventure
        \n4:The Enchanted Garden
        \n5:The Pirate's Treasure
        \n6:The Time Traveler
        \n7:The Secret Garden
        \n8:The Explorer's Quest
        \n9:The Magical Circus
        \n10:The Inventor's Workshop
        \n11:The Musician's Journey
        \n12:The Chef's Culinary Adventure
        \n13:The Writer's Imagination
        \n14:The Artist's Canvas
        \n15:The Detective's Puzzle
        \n16:The Underwater Odyssey
        \n17:The Astronaut's Discovery
        \n18:The Magician's Enchantment
        \n19:The Botanist's Paradise
        \n20:The Time Traveler's Dilemma
        \n21:The Dreamer's Wonderland
        \n22:The Wildlife Explorer
        \n23:The Inventor's Legacy
        \n24:The Space Explorer
        \n25:The Artisan's Workshop
        \n26:The Chef's Culinary Journey
        \n27:The Musician's Symphony
        \n28:The Detective's Conundrum
        \n29:The Dreamer's Odyssey
        \n30:The Wildlife Photographer
        \n31:The Explorer's Legacy
        \n32:The Magical Forest
        \n33:The Archaeologist's Expedition
        \n34:The Botanist's Discovery
        \n35:The Artist's Canvas
        \n36:The Time Traveler's Odyssey
        \n37:The Dreamer's Wonderland
        \n38:The Inventor's Workshop
        \n39:The Musician's Melody
        \n40:The Detective's Riddle
        \n41:The Dreamer's Journey
        \n42:The Wildlife Biologist
        \n43:The Explorer's Quest
        \n44:The Magical Library
        \n45:The Chef's Culinary Delight
        \n46:The Space Explorer's Odyssey
        \n47:The Artist's Vision
        \n48:The Mystery of the Haunted House
        \n49:The Wizard's Spellbook
        \n50:The Detective's Riddle
        ''')
        ch = input("Enter the story no for creating a beautiful story :")
        try:
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
        except TypeError as a:
            print(a)
    except FileNotFoundError as e:
        print(e)
        print("Opps...! Sorry to interrupt \nOnce again verify that file name was correct")
    choice = input("Do you want to continue next story then press (y)? ")
    if choice.lower() == "y":
        yourchoice()
    else:
        pass
if __name__ == "__main__":
    yourchoice()