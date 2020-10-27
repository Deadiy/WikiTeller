import os
import requests
import sys
import pyttsx3
import re
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen
import keyboard


if os.name == 'posix':
    clean =  ('clear')
else:
    clean =  ('cls')
while True:
    speaker = pyttsx3.init()
    url = 'https://en.wikipedia.org/wiki/Special:Random'
    html = urlopen(url) 
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find(id="firstHeading").string
    content = soup.find(id="bodyContent").find_all('p')
    content = re.sub(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});', "", str(content))
    print(title)
    speaker.say(title)
    speaker.runAndWait()
    print(content)
    speaker.say(content)
    speaker.runAndWait()
    os.system(clean)

    

    
