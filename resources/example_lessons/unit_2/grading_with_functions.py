import random # for randint()

#### add this function if there's time
"""# return True if the number is between 1 and 100
# return False otherwise
def get_modifier(score):
    '''
    return a grade modifier based on a score
    '''
    # isolate the ones digit of the score with % 10
    ones = score % 10

    modifier = ''
    if ones <= 3:
        modifier = '-'
    elif ones >= 7:
        modifier = '+'

    return modifier
"""

# define a function to convert scores to letter grades
def get_grade(score):
    # convert to letter grade
    if score >= 90 and score <= 100:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    elif score >= 0:
        grade = 'F'

    # return the letter grade
    return grade

while True:
  # ask the user for their score
  user_score = input("Please enter your score 1-100 or 'q' to quit: ")

  # exit if the user entered 'q'
  if user_score == 'q':
    print('Goodbye')
    break # end the loop

  # convert the score to an integer
  user_score = int(user_score)

  # generate a random rival score
  rival_score = random.randint(0, 100)

  # convert the user score with the function
  user_grade = get_grade(user_score)

  # convert the rival score with the function
  rival_grade = get_grade(rival_score)

'''
  # get the user's grade modifier
  user_mod = get_modifier(user_score)
  
  # get the user's grade modifier
  rival_mod = get_modifier(rival_score)
'''



  print(f'user: {user_score} - {user_grade}') #{user_mod}')
  print(f'rival: {rival_score} - {rival_grade}') # {rival_mod}')
