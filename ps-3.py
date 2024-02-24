'''
There is an id code that is supposed to be given to all the aspirants of an exam. It is actually a
substring of a given string. That means, the authority takes a string and then assigns all the unique
substrings to all the students. Suppose there is a string “abcde”, so the ids of the students will be
“a”,”b”,”c”,”d”,”e”,’ab”,”abc”,”abcd”,”abcde”,”bc”,”bcd”,”bcde”,”cd”,”cde”,”de”.
The students are standing in a line according to the lexicographic order of their given ids. You have to
find out the id of the last student for the given input string from which the ids are generated.
• Input Format:
o Single line with the id generating string
• Output format:
o The last id as per lexicographical order
• Constraints:
o Number of characters in the string<=10^9
'''
import random
import string

'''
Solution Approach: 
    Tested for Number of characters in the string < 10^4
    
    # using two pointer approach, 
    # first pointer at first character
    # second pointer at second character 

    # initialize a [] to keep a list of substrings which has to be sorted later on

    #  while (i < j ) : 
    #  i till j pointer will become a subtring --> sub_str = code_str[i:j]
    #  therefore i should always be less than j 
    #  j is next of i 
    #  while j <= len(code_str): j should be less than size of input string 
    # when i = 0, j will be from 1 to n-1, 
    # when i = 1, j will be from 2 to n-1 and so on
    thus lastly append all substr as code_str[i:j] in substrings list
    sort them out so as to get in alphabetical order 
    return last element

    # other approach could have been:
    to not append in a list to save space
    or while appending make sure we are appending in ascending order, this can avoid sorting later on
'''

def get_last_substr(code_str):

    i = 0
    j = 1
    substrings = []
    while i < j:     
        j = i+1
        while j <= len(code_str):
            sub_str = code_str[i:j]
            substrings.append(sub_str)
            j +=1
        i +=1 
    return sorted(substrings)[-1]

# TC 1: unordered alphabets  : Success
s = get_last_substr("abdc")
print(s)

# TC 2: ordered alphabets  : Success
s = get_last_substr("abcde")
print(s)

# TC 3: single alphabet : Success
s = get_last_substr("a")
print(s)

# TC 4: 10 raised to 3 characters : Success
random_string = ''.join(random.choices(string.ascii_letters, k=10**3))
s = get_last_substr(random_string)
print(s)

# TC 5: 10 raised to 4 or more characters : Fails
# random_string = ''.join(random.choices(string.ascii_letters, k=10**4))
# s = get_last_substr(random_string)
# print(s)
