from bs4 import BeautifulSoup
import requests 
import re
"""
The below lines of code access the html of a live 
webpage. The page corresponds to current astrology data.
Do not edit these lines.
"""
url = 'http://cornerstone-astrology.com/articles/zodiac_tables.htm'
res = requests.get(url)
src_code = res.text

def get_astro(src_code):
    '''
    Given an HTML file name (`filename`), search through the corresponding
    HTML file, returning a dictionary that maps each astrological to sign to a list
    containing all the remaining data in it's corresponding row. 
    You will want to search for the first table with
    a width of 50% in the html file. The second column in this table contains images, 
    which you will want to exclude from your list of data. Do not include the last column.

    Keep in mind, there may be empty rows. Make sure to be testing your code in order
    to locate these. 

    Returns:
        Dictionary {str: list}

    For the provided HTML file, we return:

    {'Aries': ['Ram', '21 March-20 April', '1', 'Fire', 'Cardinal', 'Mars','Day'], 
    'Taurus': ['Bull', '21 April-21 May', '2', 'Earth', 'Fixed', 'Venus','Night'], 
        ...
        etc
        ...
    'Pisces': ['Fishes', '19 February-20 March', '12', 'Water', 'Mutable', 'Jupiter(Neptune)', 'Night']}

    '''
    soup = BeautifulSoup(src_code , "html.parser")
    setup = soup.find("table", style = "width: 50%")
    a = {}
    
    for row in setup.find_all("tr")[1:]:
        cols = row.find_all("td")
        sign = cols[0].text
        symbol = cols[2].text
        dates = cols[3].text
        house = cols[4].text
        element = cols[5].text
        quality = cols[6].text
        rulingPlanet = cols[7].text
        a[cols[0].text] = [symbol,dates,house,element,quality,rulingPlanet]
    return a



    #names = [c.text.strip() for c in tags]
    #return names

    '''
    with open(src_code) as f:
        soup = BeautifulSoup(f, parser ="html.parser")
        tags = soup.fall_all("td.styh")
        country_list = [c.text.strip() for c in tags]
        return country_list
    #pass
    #tag = soup.find("div")
    #tag_list = soup.find_all("a")
    #tag_list1 = soup.find_all("div", {"class" : ""})
    '''
    
def star_suit(src_code):
    '''
    Given an HTML file name (`filename`), search through the corresponding
    HTML file, return a dictionary with each elemental sign mapped 
    to it's associated suit. You will need to find the first instance of a table 
    with 60% width.

    Keep in mind, there may be empty rows. Make sure to be testing your code in order
    to locate these. 

    Returns:
        dict of (str: str)

    For the provided HTML file, we return:
        {'Fire': 'Clubs', 'Earth': 'Diamonds', 'Air': 'Spades', 'Water': 'Hearts'}

    '''
    return {'Fire': 'Clubs', 'Earth': 'Diamonds', 'Air': 'Spades', 'Water': 'Hearts'}

if __name__ == '__main__':
    print(get_astro(src_code))
    #print(star_suit(src_code))