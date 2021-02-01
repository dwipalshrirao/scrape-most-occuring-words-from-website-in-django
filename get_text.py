
import requests
from bs4 import BeautifulSoup
import time
from collections import Counter 
import re


def top10_word(url):

    print(time.time(),'start')
    res = requests.get(url)
    print(time.time(),'url')
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    
    text = soup.find_all(text=True)
    
    output = ''
    blacklist = ['[document]','noscript','header','html','meta','head', 'input','script']


    for i in text:
        if i.parent.name not in blacklist:
            # by using regex it takes only words not numbers or special charector from content
            output += re.sub(r"[^a-zA-Z]+", ' ', i.lower())
    # split text
    text=output.split()
    with open('stop_words_english.txt') as f:
        stop_words=f.read()

    # get all list of special characters to add them in list of stop words
    from string import punctuation
    special_char= set(punctuation)

    stop_words = set(stop_words.split()) 
    stop_words=stop_words.union(special_char)
    
    filtered_sentence = [w for w in text if not w in stop_words]  

    print(time.time(),'before')
    before=time.time()
    
    counter = Counter(filtered_sentence) 
    most_occur = counter.most_common(10) 
    
    after=time.time()
    print(after-before)
    return most_occur