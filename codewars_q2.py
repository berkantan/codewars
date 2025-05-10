# QUESTION-2
# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending),
# the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

def longest(a1, a2):
    new_string = ""
    concatenation_string = ''.join(sorted(a1+ a2))
    for i in concatenation_string:
        if not i in new_string:
            new_string += i
        else:
            continue
    return new_string



