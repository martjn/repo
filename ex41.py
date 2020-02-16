import random
from urllib.request import urlopen
import sys


WORD_URL = "http://github.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init___(self, ***)" :
    "class %%% has-a ___init___ that takes self and *** parameters",
    "class %%%(object):\n\tdeff *** (self, @@@)":
    "class %%% has-a function *** that takes self and @@@ parameters",
    "*** = %%%()":
    "Set *** to an instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, call it with parameters set ***(@@@)",
    "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."

}
# Kobi siia
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHASE_FIRST = True
else:
    PHASE_FIRST = False

# lae andmed internetist koodi
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), engoding="utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', ' .join(
            random.sample(WORDS, param_count)))
            
        for sentence in snippet, phrase:
            result = sentence[:]

            # fake class names
            for word in class_names:
                result = result.replace("%%%", word, 1)

            # fake other names
            for word in other_names:
                result = result.replace("***", word, 1)

            # fake parameter lists
            for word in param_names:
                result = result.replace("@@@", word, 1)

            result.append(result)

    return results


        # CTRL-D jaoks lopeta kood
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
                    
            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")