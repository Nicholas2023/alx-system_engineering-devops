#!/usr/bin/env ruby

# Define the regular expression pattern
regex = /School/

# Read the input from the command line argument
input = ARGV[0]

# Find all occurences of the regex pattern in the input
matches = input.scan(regex)

# Join the matched occurence into a single string
matched_string = matches.join

# Output the matched string followed by the end -f line marker
puts matched_string
