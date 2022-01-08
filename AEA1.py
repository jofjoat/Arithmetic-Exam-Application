import random
n = 0
level1 = '1 (simple operations with numbers 2-9)'
level2 = '2 (integral squares of 11-29)'
print('Which level do you want? Enter a number:\n'
      '1 - simple operations with numbers 2-9\n'
      '2 - integral squares of 11-29')

user_input = int(input())

# user_input = int(input())
if user_input == 1:
    for i in range(5):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        op = random.choice(['+', '-', '*'])
        print(f'{a} {op} {b}')

        while True:
            answer = input()
            try:
                answer = int(answer)
            except ValueError:
                print('Wrong format! Try again.')
            else:
                break

        if op == '+' or op == '-' or op == '*':
            if answer == a + b or answer == a * b or answer == a - b:
                print('Right!')
                n += 1
            else:
                print('Wrong!')
    print(f'Your mark is {n}/5. Would you like to save your result to the file? Enter yes or no.')

elif user_input == 2:
    for i in range(5):
        x = random.randint(11, 29)
        print(x)

        while True:
            answer = input()
            try:
                answer = int(answer)
            except ValueError:
                print('Wrong format! Try again.')
            else:
                break
        if answer == pow(x, 2):
            print('Right!')
            n += 1
        else:
            print('Wrong!')

    print(f'Your mark is {n}/5. Would you like to save your result to the file? Enter yes or no.')
a = ['yes', 'y', 'Yes', 'YES']
print_result = str(input())
if print_result in a:
    username = input('What is your name? ')
    file = open('results.txt', 'a', encoding='utf-8')
    if user_input == 1:
        file.write(f'{username}: {n}/5 in level {level1}')
    elif user_input == 2:
        file.write(f'{username}: {n}/5 in level {level2}')
    file.close()
    print('The results are saved in "results.txt".')
else:
    exit()
