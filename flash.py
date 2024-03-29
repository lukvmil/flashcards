import json

with open('flashcards.json') as f:
    try:
        flashcards = json.load(f)
    except json.decoder.JSONDecodeError:
        flashcards = {}
    
def save():
    with open('flashcards.json', 'w') as f:
        json.dump(flashcards, f, indent=2)

# --------------------------------------------
# loading years

years = len(flashcards.keys())

if years == 0:
    flashcards['Year 1'] = {}
    years = 1

curr_year = flashcards[f'Year {years}']

# --------------------------------------------
# loading lessons 

lesson = list(curr_year.keys())[-1]

curr_lesson = curr_year[lesson]

# --------------------------------------------

while True:
    print(f'Year {years}, {lesson}')
    print('(enter: add to current location, lesson: add lesson, year: add year, quit: quit)')
    ui = input()
    
    if ui == '':
        while True:
            char = input('C: ')
            if char == '':
                break
            pinyin = input('P: ')
            defin = input('D: ')
            print()
            print(f'add {char} {pinyin} {defin}?')
            ui = input()
            if ui == '':
                curr_lesson.append([char, pinyin, defin])
                print('added')
                save()
            else:
                print('entry was removed')
            print()
            
    elif ui == 'lesson':
        if curr_lesson:
            while True:
                print('Lesson number? ', end='')
                try:
                    lesson_number = int(input())
                    new_lesson = f'Lesson {lesson_number}'
                    if new_lesson in curr_year:
                        print('Lesson already exists')
                        continue
                    else:
                        break
                except ValueError:
                    continue
            
            lesson = new_lesson
            curr_year[new_lesson] = []
            curr_lesson = curr_year[new_lesson]
        else:
            print('current lesson is empty')
        print()

    elif ui == 'year':
        if curr_year:
            years = len(flashcards.keys()) + 1
            flashcards[f'Year {years}'] = {}
            curr_year = flashcards[f'Year {years}']
            
            curr_year['Lesson 1'] = []
            curr_lesson = curr_year['Lesson 1']
            lessons = 1
        else:
            print('current year is empty')
        print()

    elif ui == 'quit':
        break

    elif ui == 'disp':
        print(flashcards)

    
words_only = []

for year in flashcards:
    for lesson in flashcards[year]:
        for word in flashcards[year][lesson]:
            card = {
                "character": word[0],
                "pinyin": word[1],
                "definition": word[2],
                "read_correct": 0,
                "read_attempts": 0,
                "write_correct": 0,
                "write_attempts": 0
            }
            words_only.append(card)

with open('words_only.json', 'w') as f:
    json.dump(words_only, f, indent=2)