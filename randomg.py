from random import choice
import os
projects = ["a store finder", "a bruteforcer", "an antivirus", "a selenium web bot", "a web scraper", "a crypto currency", "a shell", "a game", "a social platform", "code snippets app", "a code help website"]
combiners = ["make", "code", "program"]
languages = ["python", "c#", "ruby", "javascript", "rust", "java", "typescript", "go", "dart", "kotlin", "PHP", "dart"]
improvers = ["improve", "remake", "modify", "add a feature to "]

def give():
    if not os.path.exists("used.txt"):
        with open ("used.txt", "a") as f:
            f.close()
    f = open("used.txt", "r")
    gen = f"{choice(combiners)} {choice(projects)} in {choice(languages)}"
    if gen in f.readlines():
        gen = gen.replace(gen.split(" ")[0], choice(improvers), 1)
    f.close()
    with open("used.txt", "a") as f:
        f.write(gen + "\n")
    return gen
