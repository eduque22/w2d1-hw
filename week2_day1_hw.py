##Exercise1 - Accept two user ages as inputs and give us the difference between them(answer should always be positive)

age1 = int(input('What is your age User 1? '))

age2 = int(input('\nWhat is your age User 2? '))

if age1 >= age2:
    print(f"The difference between those ages is {age1 - age2}")
elif age2 >= age1:
    print(f"The difference between those ages is {age2 - age1}")




##Exercise2 - Accept 3 user inputs for variables named 'noun', 'verb' and 'adjective'.Print out a formatted string using the outputs

noun = input('Enter a noun: ')
verb = input('\nEnter a verb: ')
adj = input('\nEnter an adjective: ')

sent = f"The {noun} {verb} over the {adj} mountain."
print(sent)



##Excercise3 - Take in users input for their age, if they are younger than 18 print 'kids', if theyre 18 to 65 print adults, else print senior.

user_age = int(input('How old are you? '))

if user_age < 18:
    print(f"You are only {user_age}, child.")
elif user_age > 18 and user_age < 65:
    print(f"Ahhh because youre {user_age}, you think youre an adult.")
elif user_age >= 65:
    print(f"Ohhh youre {user_age}, you must be as wise as me.")


##Exercise4 - Take in a number from input, output the number squared

num = int(input('Give me a number and I will square it: '))
new_num = num**2
print(f"That number squared is {new_num}")


##Exercise5 - Check variable's length. If length of word is greater than 5, output True, else False

word1 = 'panini'
word2 = 'bulbasaur'
word3 = 'pie'
word4 = 'dolphin'
word5 = 'dog'

words = [word1, word2, word3, word4, word5]
for word in words:
    if len(word) > 5:
        print('True')
    else:
        print('False')