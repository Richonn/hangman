import random

words = []
with open("words.txt") as fl:
    for l in fl:
        words.append(l.rstrip("\n"))
word = random.choice(words)

letters = []
wrong = 0
right = 0
len_word = len(word)
find = False
full_body = ["o", "/", "|", "\\", "/", "\\"]
body = [" ", " ", " ", " ", " ", " "]

while not find:
    print(" +---+")
    print(" |   |")
    print(" |   {}".format(body[0]))
    print(" |  {}{}{}".format(body[1], body[2], body[3]))
    print(" |  {} {}".format(body[4], body[5]))
    print("_|_")
    print("| |")
    for l in word:
        if l in letters:
            print(l, end=" ")
        else:
            print("_", end=" ")
    print()
    print("Lettre utilisées - ", end=" ")
    for l in letters:
        print(l, end=" | ")
    print()

    if right == len_word:
        find = True

    if wrong > 5:
        print("\nTu as perdu !")
        print("Mot - {}".format(word))
        break


    if find == True:
        print("\nTu as gagné !")
        break

    letter = input("\nEntrez une lettre: ")
    letters.append(letter)

    if letter not in word:
        body[wrong] = full_body[wrong]
        wrong += 1
    else:
        right += 1
