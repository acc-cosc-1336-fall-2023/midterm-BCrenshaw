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
# pylint: disable=W0105

import question_d as qd

"""
1)  Write a program that generates a random number in the range of 1 through 5, and asks the user to guess what the number is. 
    If the user guesses the number, the application should congratulate the user and generate a new random number so the game can start over.
    
    Function:
                get_random_number 

2)  Test the get_random_number to make sure it generates number in the range of 1 to 5.


3)  In main write a program that runs until the user decides to quit. (User continue loop)
    Create another loop, the game loop, that loops until the user guesses the number.
    If the user guesses congratulate else ask them to try again.
"""
exit_clause = '2'
confirmation = 'YES'
user_selection = '0'
current_score = 0
attempt_count = 0
accuracy = 0
min_random = 1
max_random = 5
user_answer = ''
user_result = ''
random_number = 0


qd.use_global_variables(min_random, max_random)

while user_selection != exit_clause:
    random_number = qd.get_random_number()
    user_selection = input(' ' + "\x1B[4m" + 'Welcome to the Midterm random-number, guessing, game menu:' + "\x1B[0m" + '\n  Press [1] for guessing numbers!\n        [2] to  Exit the program\n\t>>> ')
    keep_playing = 'y'
    while user_selection == '1' and (keep_playing.upper() == confirmation or keep_playing.upper() == confirmation[0:1:1] or keep_playing.upper() == confirmation[0:2:1]):
        user_answer = input(' Please select a number between ' + str(min_random) + ' and ' + str(max_random) + ' \n\t>>> ')
        user_result = qd.check_the_guess(user_answer, random_number)
        while user_result != 1 and user_result != 0 or (int(user_answer) < min_random or int(user_answer) > max_random):
            print('Try again please.')
            user_answer = input(' Please select a number between ' + str(min_random) + ' and ' + str(max_random) + ' \n\t>>> ')
            user_result = qd.check_the_guess(user_answer, random_number)
        if user_result == 1:
            print(' Good work!', user_answer, 'was equal to', random_number, 'and is therefore correct!')
        else:
            print(' I am sorry', user_answer, 'was not equal to', random_number, 'and was therefore was not correct.')

        current_score += user_result
        attempt_count += 1
        print(' Your current score is', current_score, ' and your accuracy is', round(current_score/attempt_count*100, -1))
        random_number = qd.get_random_number()
        keep_playing = input(' Would you like to keep playing? [YES/NO]\n\t>>> ')

    if user_selection == '2':  
        user_selection = qd.exit_confirmation_loop(user_selection)
    
    else: 
        user_selection = qd.exit_confirmation_loop(user_selection)