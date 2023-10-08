#write functions here, don't add input('') statements here!

# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=C0301
# pylint: disable=C0303
# pylint: disable=C0304
# pylint: disable=C0321
# pylint: disable=E0401
# pylint: disable=R1705
# pylint: disable=R1723
# pylint: disable=W0601
# pylint: disable=W0603

import random as r

def use_global_variables(min_random_n, max_random_n):
    global min_random
    min_random = min_random_n
    global max_random
    max_random = max_random_n

def get_random_number():
    global min_random
    global max_random
    random_number = r.randint(min_random, max_random)
    return random_number

def exit_confirmation_loop(user_confirmation):
    exit_clause = '2'
    confirmation = 'YES'

    if user_confirmation != exit_clause:
        
        user_confirmation = input(' Would you like to exit? [YES/NO]\n\t>>> ')

        if user_confirmation.upper() == confirmation or user_confirmation.upper() == confirmation[0:1:1] or user_confirmation.upper() == confirmation[0:2:1]:
            
            user_confirmation = input(' Are you sure you want to exit? Enter [YES], all other selections will return you to the menu.\n\t>>> ')

            if user_confirmation.upper() == confirmation or user_confirmation.upper() == confirmation[0:1:1] or user_confirmation.upper() == confirmation[0:2:1]:
                result = exit_clause
                print('\x1B[3m' + ' Exiting the Midterm Menu' + '\x1B[0m')
            
            else: result = 0
        
        else: result = 0
    
    else:
        
        user_confirmation = input(' Are you sure you want to exit? Enter [YES], all other selections will return you to the menu.\n\t>>> ')
        if user_confirmation.upper() == confirmation or user_confirmation.upper() == confirmation[0:1:1] or user_confirmation.upper() == confirmation[0:2:1]:
            result = exit_clause
            print('\x1B[3m' + ' Exiting the Midterm  random-number, guessing, game menu' + '\x1B[0m')   
        
        else: result = 0

    return result

def check_the_guess(user_answer, random_number):
    
    while isinstance(user_answer, str):
        try:
            user_answer = int(user_answer)
        except (AttributeError, ValueError, TypeError):
            return 'error'
    
    if random_number == user_answer:
        user_result = 1
    else:
        user_result = 0
    return user_result