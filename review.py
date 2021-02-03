import json, random

with open('words_only.json') as f:
    cards = json.load(f)


def correct():
    while True:
        ui = input()
        if ui == "yes":
            return True
        if ui == "no":
            return False

t = input("practice (r)eading or (w)riting? ")
try:
    while True:
        card = random.choice(cards)
        if t == "r":
            print(card["character"])
            input()
            print(card["pinyin"])
            print(card["definition"])
            if correct():
                card["read_correct"] += 1
            print()
            card["read_attempts"] += 1
        elif t == "w":
            print(card["pinyin"])
            print(card["definition"])
            input()
            print(card["character"])
            if correct():
                card["write_correct"] += 1
            print()
            card["write_attempts"] += 1
        else:
            break

except KeyboardInterrupt:
    with open('words_only.json', 'w') as f:
        json.dump(cards, f, indent=2)