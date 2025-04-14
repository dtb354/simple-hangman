galgjeWoord = input("Speler 1, geef een woord in:").lower()
wrongGuesses = 0
hiddenWord = ["_" for _ in galgjeWoord]
correctGuesses = []
player2Guesses = []

print("scroll naar beneden :)")
print("\n" * 50)
print("Speler 1 heeft een woord gekozen.")
print("Woord: " + " ".join(hiddenWord))
print("Speler 2 moet nu letters kiezen om het woord te vinden")
print("Speler 2 mag alleen 9 fouten maken")

while wrongGuesses < 9:
    speler2Guess = input("Speler 2, kies een letter:").lower()

    if speler2Guess == "":
        print("Je... Je hebt niks ingevoerd... WAT?!?!")
        continue

    if speler2Guess in galgjeWoord:
        print("Ja, dat zit in het woord!")
        correctGuesses.append(speler2Guess)

        for i in range(len(galgjeWoord)):
            if galgjeWoord[i] == speler2Guess:
                hiddenWord[i] = speler2Guess
    else:
        print("OOPSIE DAISY, niet in het woord :(")
        wrongGuesses += 1

    print("Woord: " + " ".join(hiddenWord))

    if "_" not in hiddenWord:
        print("GEFELICITEERD! Je hebt het woord geraden!")
        print("Het woord was: " + galgjeWoord.upper())
        break

    print(f"Foute pogingen: {wrongGuesses}/9")

if wrongGuesses == 9:
    print("Helaas, je hebt 9 keer fout geraden.")
    print(f"Het woord was: {galgjeWoord.upper()}")
    print("Volgende keer beter!")