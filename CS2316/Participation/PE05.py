import requests
from pprint import pprint
import re


def script_searcher(keyword, target):
    """ Q1
    In your free time, you decided to spend some time and mess around with the
    script to the Bee Movie. Given a string that represents the keyword and a
    string that represents a quote from the Bee Movie script, return the given
    keyword along with the word following immediately before.
    This must be implemented in one line.

    Hint: You may assume the word before the keyword will contain letters, followed
    by a space.

    Args:
        keyword (str): the specific keyword to search for
        target (str): the string to search in
    Returns:
        str

    >>> script_searcher("night", "Why is yogurt night so difficult?")
    'yogurt night'

    >>> script_searcher("Industries", "And begins your career at Honex Industries!")
    'Honex Industries'

    >>> script_searcher("bug", "Are you her little... bed bug?")
    'bed bug'
    """
    #pass   
    return re.findall("[A-Za-z]+ " + keyword, target)[0]
    
def double_l(target):
    """ Q2
    You're given a string of random words. Return a list of strings for all the
    words which contain two 'l's. Think of how words are distinctly seperated in the string,
    and keep in mind some words with two 'l's might be at the end of the string.
    This must be implemented in one line.

    Args:
        target (str): the string to search in
    Returns:
        list of strings
    >>> double_l("Autumn leaves falling down like pieces into place")
    ['falling']
    >>> double_l("I remember it All Too Well")
    ['All', 'Well']

    """
    return re.findall("[A-Za-z]*ll[A-Za-z]*",target)

def mathmatic(target):
    """ Q3
    You are doing fun math problems. Given a string of combination of '{}', '[]',
    '()', you are required to return the substring included by the outermost '{}'.
    You need to write your code in one line.

    Args:
        target (str): the string to search in
    Returns:
        list of str

    >>> mathmatic('{[[[[]()]]]}')
    '[[[[]()]]]'

    >>> mathmatic('[(){([{}])}]')
    '([{}])'

    """
    #pass
    return re.findall(r'{([^A-Z]*)}',target)[0]

def quotable(target, character):
    """ Q4
    Given a string of lines from the Bee Movie script and a character parameter, return the first line
    in the script that the character says, excluding their name. 
    which that character speaks.

    You need to write your code in one line.

    Args:
        target (str): the string to search in
        character (str): the character whose first line you want to return
    Returns:
        str of first match

    >>> quotes: "Vanessa Bloome: [shock] How did you learn to do that?" + \
        " Barry B. Benson: Do what?" + \
        " Vanessa Bloome: That, that- the talking thing!"
    >>> character = "Vanessa Bloome"

    >>> quotable(quotes, character)

    "[shock] How did you learn to do that?""

    """
    return re.findall(character + ': ([^..^?^\.^!]*[?\.!])', target)[0] #[A-Za-z\s]



if __name__ == "__main__":
    #####Question 1#####
    #print(script_searcher("night", "Why is yogurt night so difficult?"))
    #print(script_searcher("Industries", "And begins your career at Honex Industries!"))
    #print(script_searcher("bug", "Are you her little... bed bug?"))

    #####Question 2#####
    #print(double_l("Autumn leaves falling down like pieces into place"))
    #print(double_l("I remember it All Too Well"))

    #####Question 3#####
    #print(mathmatic('[(){([{}])}]'))
    #print(mathmatic('{[[[[]()]]]}'))

    #####Question 4#####
    astr ="Vanessa Bloome: [shock] How did you learn to do that?" + \
    " Barry B. Benson: Do what?" + \
    " Vanessa Bloome: That, that- the talking thing!"

    print(quotable(astr,"Vanessa Bloome"))
