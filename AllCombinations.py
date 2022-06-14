def init():
    letters = input("Enter the letters: ")
    counter = len(letters) - 1
    printed = []
    for i in letters:
        printed.append(i)

    return counter,letters,printed

def AllRearranged(counter,letters,printed):
    if counter != -1:
##        for j in range(len(letters)):
##            printed.append('X')

        for le in letters:
            printed.pop(counter)
            printed.insert(counter,le)
            printed = AllRearranged(counter-1,letters[:letters.find(le)]+letters[letters.find(le)+1:],printed)

    else:
        for s in printed:
            print(s,end="")
        print()

    return printed

def AllPossible(counter,letters,printed):
    if counter != -1:
##        for j in range(len(letters)):
##            printed.append('X')

        for le in letters:
            printed.pop(counter)
            printed.insert(counter,le)
            printed = AllPossible(counter-1,letters,printed)

    else:
        for s in printed:
            print(s,end="")
        print()
    return printed

print('''
AllRearranged generates all possible rearrangements of entered characters.
Number of possible rearrangements = <numberOfCharacters>!

AllPossible generates all possible strings of length <numberOfCharacters>
made from the entered characters.
Number of possible strings = <numberOfCharacters> to the power <numberOfCharacters>
''')
