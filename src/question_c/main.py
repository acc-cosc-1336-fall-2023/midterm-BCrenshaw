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

import question_c

"""
1) Write a program to show that a global variable can be modified inside a function.
Function: use_global with no parameters.

2) Write a test case using a global variable, modify the global variable in the test case function
(call the use_global variable function), afterward write the assertion to show that the value changes. 

3) Write a program that creates a global variable, change the value using the use_global, and finally
display the value to screen.
"""

created_variable = 3
addition_to_the_multiplier = 0

print(' Creating a new variable in question_c.py named multiplier with the value of\n\t>>> ', created_variable)
question_c.create_global(created_variable)

print(' Running the newly created variable through the function ' + '\033[1;4m' + 'use_global' + '\033[0m' + ', this results in the following number when that variable is\n\t>>> multiplied by 4 =', question_c.use_global(0)*4)
print(' Running the ' + '\033[1;4m' + 'use_global' + '\033[0m' + ' function again but ' + '\033[1;4m' + 'adding 1' + '\033[0m' + ' to the multiplier\n\t>>> multiplied by 4 =', question_c.use_global(1)*4)
print(' Running the ' + '\033[1;4m' + 'use_global' + '\033[0m' + ' function again but making no changes to show that the addition from the step before is still in the memory after the previous use of the function\n\t>>> multiplied by 4 =', question_c.use_global(0)*4)