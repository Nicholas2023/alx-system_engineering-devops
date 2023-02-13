####0. Hello World####

*echo "Hello, World" : A script that prints "Hello, World",followed by a new line to the standard output.

####1. Confused Smiley####

*echo '"(^Oo)'\' : A script that displays a confused smiley.

####Let's display a file####

*cat /etc/passwd : Displays the content of /etc/passwd file.

####3. What about 2?####

*cat /temp/passwd /temp/hosts : Display the content of /etc/passwd and /etc/hosts

####4.Last lines of a file####

*tail /etc/passwd : Display the last 10 lines of /etc/passwd

####5. I'd prefer the first ones actually####

*head /etc/passwd : Display the first 10 lines of /etc/passwd

####6. Line #2####

*head -3 iacta | tail +3 :  a script that displays the third line of the file iacta.

####7. It is a good file that cuts iron without making a noise#

*echo "Best School" > \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) : a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.

####8. Save current state of directory####

*ls -la > ls_cwd_content : a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

####9. Duplicate last line####

*tail -1 iacta >> iacta :  a script that duplicates the last line of the file iacta

####10. No more javascript####

*find . -type f -name | rm *.js :  a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.

####11. Don't just count your directories, make your directories count####

*find . -type d ! -path |wc -l :  a script that counts the number of directories and sub-directories in the current directory.

####12. What’s new####

*ls -lt | head :  a script that displays the 10 newest files in the current directory.

####13. Being unique is better than being perfect####

*sort |uniq -u : a script that takes a list of words as input and prints only words that appear exactly once.

####14. It must be in that file####

* cat /etc/passwd | grep root : Display lines containing the pattern “root” from the file /etc/passwd

####15. Count that word####

* cat /etc/passwd | grep bin | wc -l : Display the number of lines that contain the pattern “bin” in the file /etc/passwd

####16. What's next?####

* cat /etc/passwd | grep -A 3 root : Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd

####17. I hate bins####

* cat /etc/passwd | grep -v "bin" : Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.

####18. Letters only please####

* cat /etc/ssh/sshd_config | grep -i '^[a-z]' : Display all lines of the file /etc/ssh/sshd_config starting with a letter.

####19. A to Z####

* tr "A" "Z" | tr "c" "e" 

####20. Without C, you would live in hiago####

* tr -d "Cc" : Create a script that removes all letters c and C from input.
