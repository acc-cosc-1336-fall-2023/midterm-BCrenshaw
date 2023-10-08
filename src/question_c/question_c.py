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

def create_global(new_multiplier):
    global multiplier
    multiplier = new_multiplier


def use_global(multiplier_addition):
    global multiplier
    multiplier = multiplier + multiplier_addition
    return multiplier