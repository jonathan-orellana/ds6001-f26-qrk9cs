# %%
import numpy as np
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup 

# %%
url='https://www.rottentomatoes.com/browse/movies_in_theaters/sort:popular?page=4'

# %%
botname="ds6001_rt"
version='0.0'
purpose="class demonstration"
email="qrk9cs@virginia.edu"

useragent=f"{botname}/{version}({purpose},{email}) python-requests:{requests.__version__}"
headers={"User_Agent": useragent}
headers

# %%
response = requests.get(url, headers=headers)
response

# %%
response.text

# %%
mysoup = BeautifulSoup(response.text, 'html.parser')
mysoup


# %% [markdown]
# HTML is builds in tags
# 
# Syntax is:
# 
# `<tag attributes=value> navigable string </tag>`
# 
# It's possible fro your data to live on the attribute value, or the navaiagleble string
# 
# Our task: identify the tag, then extract the data we want

# %%
tags = mysoup.find_all('poster-tile', attrs={'media-url': True})
tags

# %%
# if the data were in the navigable string you would do:
# tags[0].string or tags[0].txt

# if the dat is in the attribute value: 
tags[0]['media-url']

# %%
movie_urls = ['https://rottentomatoes.com' + t['media-url'] for t in tags]

# %%
movie_urls[72]

# %%
r = requests.get(movie_urls[72], headers=headers)
r

# %%
mysoup = BeautifulSoup(r.text, 'html.parser')
mysoup

# %%
movie_dict = {}

# Title
title = mysoup.find('title')
title = title.string
movie_dict['title'] = title
movie_dict

# %%
# Director



# %%
# Rating


