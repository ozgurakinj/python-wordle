from datetime import datetime

def win(answer):
    print_table(tries,answer)
    print("Congratulations! The word was : "+answer)
    print("You found the word in "+str(len(tries))+" tries")
    x = input("Press enter to quit")
    quit()

def lose(answer):
    print("Sorry! The word was : "+answer)
    x = input("Press enter to quit")
    quit()

def print_table(tries,answer):
    for t in tries:
        row = ""
        for i in range(5):
            if t[i]==answer[i]:
                row+=t[i].upper()+"  "
            elif t[i] in answer:
                row+=t[i]+"* "
            else:
                row+=t[i]+"  "
        print(row)
        row = ""
    for x in range(6-len(tries)):
        print("_  _  _  _  _ ")


def get_answer():
    start_date = datetime.now()
    today = datetime(day=19, month=6, year=2021)
    daycount = (start_date - today).days
    return answers[daycount]

def make_guess(answer):
    guess = input("Your guess: ")

    if guess in words or guess in answers:
        if guess in tries:
            print("You already tried this word.")
        else:
            tries.append(guess)
            if guess==answer:
                win(answer)
    else:
        print("Invalid word. Try again")
        print_table(tries,answer)
        make_guess(answer)

answers = [line.strip() for line in open("answers.txt", 'r')]
words = [line.strip() for line in open("words.txt", 'r')]
tries = []

def start():
    answer = get_answer()
    while len(tries)!=6:
        print_table(tries,answer)
        make_guess(answer)
    lose(answer)

print("Welcome to Python-Wordle")
start()