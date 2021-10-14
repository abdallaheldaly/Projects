value = int( input("Guess a value contained in the bag.") ) 
if value in myBag:
    print( "The bag contains the value", value ) 
else :
    print( "The bag does not contain the value", value )