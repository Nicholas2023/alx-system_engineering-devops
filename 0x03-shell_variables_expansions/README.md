#!/bin/bash 

####0. <o>####

* alias ls = "rm *" : a script that creates an alias.


####1. Hello you####

* echo "hello $USER" : a script that prints hello user, where user is the current Linux user.


####2. The path to success is to take massive, determined action####

* PATH=$PATH:/action : Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program


####3. If the path be beautiful, let us not ask where it leads####

* echo $PATH | tr ':' '\n' | wc -l : a script that counts the number of directories in the PATH.


####4. Global variables####

* printenv : a script that lists environment variables.


####5. Local variables####

* set : a script that lists all local variables and environment variables, and functions.


####6. Local variable####

* BEST="School" :  a script that creates a new local variable.


####7. Global variable####

* export BEST="School" : a script that creates a new global variable.


####8. Every addition to true knowledge is an addition to human power####

* echo $((128 + $TRUEKNOWLEDGE)) : a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line


####9. Divide and rule####

* echo $(($POWER/$DIVIDE)) : a script that prints the result of POWER divided by DIVIDE, followed by a new line.


####10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath####

* echo $(($BREATH**$LOVE))


####11. There are 10 types of people in the world -- Those who understand binary, and those who don't####

* echo $((2#$BINARY)) : a script that converts a number from base 2 to base 10


####12. Combination####

* echo {a..z}{a..z}|tr ' ' '\n'| grep -v "oo" :  script that prints all possible combinations of two letters, except oo.


####13. Floats####

* printf '%.2f\n' $NUM : a script that prints a number with two decimal places, followed by a new line


####14. Decimal to Hexadecimal####

* printf '%x\n' $DECIMAL : a script that converts a number from base 10 to base 16.


####15. Everyone is a proponent of strong encryption####

* tr 'A-Za-z' 'N-ZA-Mn-za-m' : a script that encodes and decodes text using the rot13 encryption. Assume ASCII.


####16. The eggs of the brood need to be an odd number####

* paste -d, - - | cut -d, f1 :  a script that prints every other line from the input, starting with the first line.


####17. I'm an instant star. Just add water and stir.####

* printf "%0\n" $(( $((5#$(echo $WATER |tr water 01234))) * $((5#$(echo $STIR |tr stir. 01234))) )) | tr 01234567 bestchol :  a shell script that adds the two numbers stored in the environment variables WATER and STIR and prints the result.
