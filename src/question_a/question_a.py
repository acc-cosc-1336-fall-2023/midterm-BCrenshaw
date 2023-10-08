# write functions here, don't add input('') statements here!

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

def test_config():
    return True

def is_prime(num):
    determination = ''

    if num > 1:
        
        for n in range(2, int(num/2)+2):
            
            if num % n == 0 and num != 2:
            
                determination = 'False'
                break

            else: determination = 'True'
    else:
        determination = 'False'

    return determination

def is_number_qualified(num):
    if num.isnumeric():
        return 'True'
    else: return 'False'


def exit_confirmation_loop(user_confirmation):
    exit_clause = '2'
    confirmation = 'YES'

    if user_confirmation != exit_clause:
        
        user_confirmation = input(' Would you like to exit? [YES/NO]\n\t>>>')
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
            print('\x1B[3m' + ' Exiting the Midterm Menu' + '\x1B[0m')   
        
        else: result = 0

    return result