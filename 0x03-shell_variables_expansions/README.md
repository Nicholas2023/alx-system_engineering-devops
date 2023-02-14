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
