def morse(a):
    text = a.upper()
    in_morse = text.replace("A", ".- ").replace("B", "-... ").replace("C","-.-. ")\
        .replace("D", "-.. ").replace("E", ". ").replace("F", "..-. ").replace("G", "--. ")\
        .replace("H", ".... ").replace("I", ".. ").replace("K", "-.- ").replace("L", ".-.. ")\
        .replace("M", "-- ").replace("N", "-. ").replace("O", "--- ").replace("P", ".--. ")\
        .replace("Q", "--.- ").replace("R", ".-. ").replace("S", "... ").replace("T", "- ")\
        .replace("U", "..- ").replace("V", "...- ").replace("W", ".-- ").replace("X", "-..- ")\
        .replace("Y", "-.-- ").replace("Z", "--.. ").replace("0", "----- ").replace("1", ".---- ")\
        .replace("2", "..--- ").replace("3", "...-- ").replace("4", "....- ").replace("5", "..... ")\
        .replace("6", "-.... ").replace("7", "--... ").replace("8", "---.. ").replace("9", "----. ")\
        .replace("Ä", ".-.- ").replace("Õ", "Ö").replace("Ö", "---. ").replace("Ü", "..-- ")\
        .replace("&", ".-... ").replace("'", ".----. ").replace("@", ".--.-. ").replace(")", "-.--.- ")\
        .replace("(", "-.--. ").replace(":", "---... ").replace(",", "--.-- ").replace("=", "-...- ")\
        .replace("!", "-.-.-- ").replace("+", ".-.-. ").replace('"', '.-..-. ')\
        .replace("?", "..--.. ").replace("/", "-..-. ").replace("J", ".--- ")
    return in_morse

while True:
    ans = input("Enter your text: ")
    b = morse(ans)
    print(f"Your text in morse: {b}")
    ans2 = input("Save file? ").lower()
    if ans2 == "y" or ans2 == "yes":
        ans3 = input("Name your file: ")
        f = open(ans3 + ".txt", "w+")
        f.write("Your original text: " + ans + "\nOriginal text in morse: " + b)
        f.close()
    else:
        break
