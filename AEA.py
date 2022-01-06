import random

correct = 0

for i in range(5):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    op = random.choice(['+', '-', '*'])
    print(f'{a} {op} {b}')

    while True:
        answer = int(input())
        try:
            answer = answer
        except Exception:
            print('Incorrect format.')
        else:
            if op == "+" or op == "*" or op == "-":
                if answer == a + b or answer == a * b or answer == a - b:
                    print('Right')
                    correct =+ 1
                else:
                    print('Wrong')
                break
print(f'Your mark is {correct}/5.')
