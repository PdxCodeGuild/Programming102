# 2.1
"""
hero = {
    "name": "Andromeda",
    "hp": 100,
    "attack": 35
}

villain = {
    "name": "Helios",
    "hp": 100,
    "attack": 33
}

def is_defeated(character):
    '''
    Returns False if the character's hp is greater than zero
    Returns True if the character's hp is less than or equal to
    '''
    return character['hp'] <= 0




while True:
    print(f"{hero['name']} has {hero['hp']} hp!")
    print(f"{villain['name']} has {villain['hp']} hp!")

    input("\nPress enter to begin the battle!")

    # Hero attacks
    print(f"\n{hero['name']} attacks!")

    # subtract hero's attack strength from the villain's hp
    villain['hp'] -= hero['attack']

    # check if the villain is defeated
    if is_defeated(villain):
        print(f"{villain['name']} has been defeated! {hero['name']} is victorious!")
        break # end the loop

    print(f"{hero['name']} has {hero['hp']} hp!")
    print(f"{villain['name']} has {villain['hp']} hp!")

    input("\nPress enter to continue the battle!")
 
    # Villain attacks
    print(f"\n{villain['name']} attacks!")

    # subtract hero's attack strength from the villain's hp
    hero['hp'] -= villain['attack']

    # check if the hero is defeated
    if is_defeated(hero):
        print(f"{hero['name']} has been defeated! {villain['name']} is victorious!")
        break # end the loop

"""

# 2.2
"""
# ----------------------------------------------------------- #
# Setup
# ----------------------------------------------------------- #

hero = {
    "name": "Andromeda",
    "hp": 100,
    "attack": 35
}

villain = {
    "name": "Helios",
    "hp": 100,
    "attack": 33
}

def is_defeated(character):
    '''
    Returns False if the character's hp is greater than zero
    Returns True if the character's hp is less than or equal to
    '''
    return character['hp'] <= 0

def attack(attacker, opponent):
    '''
    Apply battle damage to the opponent using the attacker's attack stat
    If the opponent is defeated, return True, signifying the battle is over
    Otherwise return False, signifying the battle will continue for another round
    '''

    print(f"{attacker['name']} has {attacker['hp']} hp!")
    print(f"{villain['name']} has {villain['hp']} hp!")

    input("\nPress enter to battle!")

    # attacker attacks
    print(f"\n{attacker['name']} attacks!")

    # subtract attackers's attack strength from the opponents's hp
    opponent['hp'] -= attacker['attack']

    # return True if the opponent is defeated, otherwise False
    return is_defeated(opponent)

# ----------------------------------------------------------- #
# Battle!
# ----------------------------------------------------------- #


# this will alternate between 0 and 1 to decide whose turn it is
turn_counter = 0

while True:

    # stat dictionaries stored at matching keys
    all_stats = {
        'hero': hero,
        'villain': villain
    }

    # keys for the all_stats dictionary
    # the turn_counter will alternate between 0 and 1 to decide whose turn it is
    stat_keys = list(all_stats.keys()) # ['hero', 'villain']

    # get the key of the current warrior
    attacker_key = stat_keys[turn_counter]
    # get the stat dictionary of the current warrior
    attacker = all_stats[attacker_key]


    # get the key of the current warrior
    # -1 if turn_counter is 0
    # 0 if the turn_counter is 1
    opponent_key = stat_keys[turn_counter - 1]
    # get the stat dictionary if the opponent
    opponent = all_stats[opponent_key]

    # execute current round of battle
    # receive True if opponent is defeated, otherwise False
    victorious = attack(attacker, opponent)

    # check the outcome of the battle. 
    # if the opponent was defeated, end the loop
    if victorious:
        print(f"{opponent['name']} has been defeated! {attacker['name']} is victorious!")
        break # end the loop


    # increment the turn_counter
    turn_counter += 1

    # make sure the turn_counter will only ever be 0 or 1 using % 2; if/elif could be used instead
    turn_counter %= 2
"""

    
# ------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------- #

# 2.3

# ----------------------------------------------------------- #
# Setup
# ----------------------------------------------------------- #
hero = {
    "name": "Andromeda",
    "hp": 100,
    "attack": 7,
    "defense": 6,
    "stance": "" # 'attack' or 'defend'
}

villain = {
    "name": "Helios",
    "hp": 100,
    "attack": 5,
    "defense": 5,
    "stance": "" # 'attack' or 'defend'
}


def is_defeated(character):
    '''
    Returns False if the character's hp is greater than zero
    Returns True if the character's hp is less than or equal to
    '''
    return character['hp'] <= 0


def set_stance(character):
    '''
    Set the character's stance stat with user 
    input and return the updated dictionary
    '''

    stance_options = {
        '1': 'attack',
        '2': 'defend'
    }

    prompt = f"""
    {character['name']}, how would you like to proceed?

    1. Attack
    2. Defend

    Enter the number of the option 
    > """

    stance_number = input(prompt)

    while stance_number not in ['1', '2']:
        print('\n!***! Invalid selection !***!')
        stance_number = input(prompt)

    # Once the user has entered a valid selection, set the dictionary-    
    character['stance'] = stance_options[stance_number]

    return character


def defend(character, incoming_damage):
    '''
    Calculate the amount the incoming_damage will be reduced 
    based on the character's 'defense' stat. 
    
    Return the amount the incoming_damage will be reduced
    in a variable called 'damage_reduction'
   
    0 - 4 = 10%, 5 - 7 = 33%, 8 - 10 = 66%
    '''
    defense = character['defense']
    if defense < 5:
        damage_reduction = incoming_damage * .1
    elif defense < 8:
        damage_reduction = incoming_damage * .33
    else:
        damage_reduction = incoming_damage * .66

    # return the reduction amount, rounded to the nearest integer
    return round(damage_reduction)


def attack(attacker, opponent):
    '''
    Apply battle damage to the opponent using the attacker's attack stat
    If the opponent is defeated, return True, signifying the battle is over
    Otherwise return False, signifying the battle will continue for another round
    '''
    battle_over = False

    print("\n" + ("-" * 50)) # print a divider

    # display hp
    print(f"\n{attacker['name']} has {attacker['hp']} hp!")
    print(f"{opponent['name']} has {opponent['hp']} hp!")

    input("\nPress enter to battle!")


    # attacker chooses stance
    attacker = set_stance(attacker)

    print("\n" + ("-" * 50)) # print a divider
    
    if attacker['stance'] == 'attack':
        # attacker attacks
        print(f"\n{attacker['name']} attacks!")

        # damage to be dealt to the opponent
        damage = attacker['attack'] * 5 # multiply damage to speed up the game

        # if the opponent chose to defend last turn
        if opponent['stance'] == 'defend':
            # calculate the damage reduction
            damage_reduction = defend(opponent, damage)   

            # reduce damage
            damage -= damage_reduction

            print(f"\n{opponent['name']} defends! Damage reduced by {damage_reduction}!") 

        # subtract attackers's attack strength from the opponents's hp
        opponent['hp'] -= damage

        print(f"{opponent['name']} takes {damage} damage!")

    elif attacker['stance'] == 'defend':
        print(f"\n{attacker['name']}, the next damage you receive will be reduced!")

    # return True if the opponent is defeated, otherwise False
    return is_defeated(opponent)


# ----------------------------------------------------------- #
# Battle!
# ----------------------------------------------------------- #

# this will alternate between 0 and 1 to decide whose turn it is
turn_counter = 0

while True:

    # stat dictionaries stored at matching keys
    all_stats = {
        'hero': hero,
        'villain': villain
    }

    # keys for the all_stats dictionary
    # the turn_counter will alternate between 0 and 1 to decide whose turn it is
    stat_keys = list(all_stats.keys()) # ['hero', 'villain']

    # get the key of the current warrior
    attacker_key = stat_keys[turn_counter]
    # get the stat dictionary of the current warrior
    attacker = all_stats[attacker_key]


    # get the key of the current warrior
    # -1 if turn_counter is 0
    # 0 if the turn_counter is 1
    opponent_key = stat_keys[turn_counter - 1]
    # get the stat dictionary if the opponent
    opponent = all_stats[opponent_key]

    # execute current round of battle
    # receive True if opponent is defeated, otherwise False
    victorious = attack(attacker, opponent)

    # check the outcome of the battle. 
    # if the opponent was defeated, end the loop
    if victorious:
        print(f"\n{opponent['name']} has been defeated! {attacker['name']} is victorious!")
        break # end the loop


    # increment the turn_counter
    turn_counter += 1

    # make sure the turn_counter will only ever be 0 or 1 using % 2; if/elif could be used instead
    turn_counter %= 2