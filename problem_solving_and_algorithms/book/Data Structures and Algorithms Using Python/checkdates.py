from datetime import date 
def main():
    # Date before which a person must have been born to be 21 or older.
    bornBefore = date(2021, 9, 23)
# Extract birth dates from the user and determine if 21 or older.
    datetime = promptAndExtractDate() 
    while datetime is not None :
        if datetime <= bornBefore :
            print( "Is at least 21 years of age: ", datetime )
        datetime = promptAndExtractDate()


def promptAndExtractDate():
    
    print( "Enter a birth date." )
    month = int( input("month (0 to quit): ") ) 
    if month == 0:
        return None 
    else :
        day = int( input("day: ") ) 
        year = int( input("year: ") ) 
        return date(year, month, day )
#Call the main routine.
main()