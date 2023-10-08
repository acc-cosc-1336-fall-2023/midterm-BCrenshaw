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

def get_miles_per_hour(kilometers, minutes):
    
    if isinstance(kilometers, str) and isinstance(minutes, str):   
        
        try:
            kilometers = int(kilometers)
            minutes = int(minutes)
        except (AttributeError, ValueError, TypeError):
            return 'Invalid arguments'
            
    if int(kilometers) < 0 or int(minutes) < 0:
        return 'Invalid arguments'
    
    else:
        hours = int(minutes)/60
        miles_to_kilometers_ratio = .621371
        miles = int(kilometers) * miles_to_kilometers_ratio
        miles_per_hour = miles/hours
        return miles_per_hour