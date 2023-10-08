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

import question_b

""" 
1) Create a function named get_miles_per_hour with parameters kilometers and minutes that returns
the miles per hour.  Use .621371 as conversion ratio.
Return the string error 'Invalid arguments' if negative kilometers or minutes are given.

2) Write the test case with arguments kilometers 32 and minutes 60 return value should be 19.883872 

3) In main.py write a program to get the kilometers and minutes from the keyboard (make sure to convert them to int),
    call the get_miltes_per_hour function using the variables kilometers and minutes, finally display the result.
"""

kilometers = input(' Please enter the number of kilometers traveled.\n\t>>> ')
minutes = input(' Please enter the number of minutes traveled.\n\t>>> ')

try:
    print(' You are traveling at a rate of:\n\t>>> ', round(int(kilometers)/(int(minutes)/60),1), ' kilometers per hour (kph)\n\tor\n\t>>> ', round(question_b.get_miles_per_hour(kilometers, minutes),1), ' miles per hour (mph)')
except (ValueError, TypeError):
    print(' Invalid arguments')