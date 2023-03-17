import re       # for RegEx

# String Parsing

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# Extract the host name

# 1. using string find  and string slicing
atpos = data.find('@')
# print(atpos)        # prints 21

sppos = data.find(' ', atpos)
# print(sppos)        # prints 31

host_name = data[atpos+1 : sppos]
print(host_name)    # prints uct.ac.za


# 2. Th eDouble Split Pattern
words = data.split()
email = words[1]
pieces = email.split('@')       # ['stephen.marquard', ''uct.ac.za']
print(pieces[1])


# 3. Regex version
'''
Breakdown of the RegEx 
@([^ ]*)

@   -   Look through the string until you find an @ sign
()  -   start extracting
[^ ]  - Match non-blank character
*   -   Match manu of them (0 or more time) greedy match
'''
host_with_regex = re.findall('@([^ ]*)', data)
print(host_with_regex)

# 3.1 Even Cooler RegEx version
'''
Breakdown of the RegEx 
^From .*@([^ ]*)

^From   -   Starting at the beginning of the line, look for the string 'From' and followed a space
.*   -   any number of characters
@   -   Look through the string until you find an @ sign
()  -   start extracting
[^ ]  - Match non-blank character
*   -   Match many of them (0 or more time) greedy match
'''
host_with_regex = re.findall('^From .*@([^ ]*)', data)
print(host_with_regex)

# 3.2 RegEx - Escape Character
# if you want a special regular expression character to just behave
# normally (most of the time) you prefix it with '\'
'''
Breakdown of the RegEx 
\$[0-9.]+

\$  -   a real dollar sign
[0-9.] - a digit or period
+   -   at least one or more
'''
sentence = 'We just received $10.00 for cookies.'
amount = re.findall('\$[0-9.]+', sentence)
print(amount)