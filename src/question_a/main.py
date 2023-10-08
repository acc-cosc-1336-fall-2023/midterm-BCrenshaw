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

import question_a

""" 
1) Write a function is_prime that returns True if a number is prime False otherwise.

2) Test the function with values 4 returns False, 5 returns True, and 11 returns True.

3) Write a program that runs until the user decided to quit, prompt the user for a number, 
    and display the result.
"""



# List of TRUE returns [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
# List of FALSE returns [4,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28,30,32,33,34,35,36,38,39]
#for n in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]:

#num = '11'
#print(question_a.is_prime(int(num)))
#print(question_a.is_number_qualified(num))


exit_clause = '2'
confirmation = 'YES'
user_selection = '0'
prime_query = ''
prime_conclusion = ''

while user_selection != exit_clause:
    user_selection = input(' ' + "\x1B[4m" + 'Welcome to the Midterm Menu:' + "\x1B[0m" + '\n  Press [1] for prime determinacy\n        [2] to  Exit the program\n\t>>> ')
    if user_selection == '1':
        
        prime_query = input(' Please select a number if you are curious whether or not it is prime\n\t>>> ')

        if question_a.is_number_qualified(prime_query) == 'True':
            
            if question_a.is_prime(int(prime_query)) == 'True': 
                prime_conclusion = 'prime' 
            else: prime_conclusion = 'not prime'

            print(' Your number: ' + prime_query + ' is ' + prime_conclusion)

            user_selection = question_a.exit_confirmation_loop(user_selection)
        
        else: 
            print(' I apologize. That was an invalid entry.')
            user_selection = question_a.exit_confirmation_loop(user_selection)

    elif user_selection == '2':  
        user_selection = question_a.exit_confirmation_loop(user_selection)
    else: 
        print(' I apologize. That was an invalid entry.')
        user_selection = question_a.exit_confirmation_loop(user_selection)