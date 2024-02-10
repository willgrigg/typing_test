import time
import random

f = open("words/words.txt")
w = f.readlines()

words = []
for word in w:
    words.append(word.split("\n")[0])

print("Are you ready to take the test? Y/N:\n")
response = input()

if response.lower() == "y":
    counter = 0
    start = time.perf_counter()
    while time.perf_counter() - start < 60:
        rand = random.randint(0, len(words))
        random_word = words[rand]
        print(random_word)
        user_word = input()
        if user_word == random_word:
            counter += len(random_word) / 5.0
        else:
            print("INCORRECT!")
    end = time.perf_counter() - start
    print(f"{(counter / end) * 100} WPM")

elif response.lower() == "n":
    print("Too bad! Goodbye.")
else:
    print("No idea what that means. Buh-bye.")