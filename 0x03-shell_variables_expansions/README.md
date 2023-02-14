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
