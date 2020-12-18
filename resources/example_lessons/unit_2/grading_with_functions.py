import random # for randint()

def get_grade(score):
    if score < 60:
        grade = 'F'
    elif score < 70:
        grade = 'D'
    elif score < 80:
        grade = 'C'
    elif score < 90:
        grade = 'B'
    elif score <= 100:
        grade = 'A'

    return grade


user_score = input('Please enter your score 1-100: ')

# convert user_score to integer
user_score = int(user_score)

# generate a random integer between 1 and 100
rival_score = random.randint(1, 100)

# call the function to get the user's grade
user_grade = get_grade(user_score)

# call the function again to get the rival's grade
rival_grade = get_grade(rival_score)

print(f'{user_score} - {user_grade}')
print(f'{rival_score} - {rival_grade}')