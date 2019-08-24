#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 22:23:17 2019

@author: awesome_k
"""
# Homework 7. Download the most recent ten comics from gocomics.com/pearlsbeforewine. Khari Shiver
import requests
import os
from bs4 import BeautifulSoup

url = 'https://www.gocomics.com/pearlsbeforeswine/'

# Access website, check url status, and pass the page into BeautifulSoup
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text)

funny_link = soup.select('a[data-link="comics"]')[0]
funny_url = 'https://www.gocomics.com' + funny_link.get('href')


i = 0
while i < 10:
    funny_res = requests.get(funny_url)
    funny_res.raise_for_status()
    funny_soup = BeautifulSoup(funny_res.text)

    # Locates the most recent comic
    image = funny_soup.select('a[itemprop="image"]')
    image_url = image[0].img.attrs['src'] + '.png'

    # Downloads the strip found in the block of code above
    image_res = requests.get(image_url)
    image_res.raise_for_status()

    # Saves the strip in the url to the working drive
    image_file = open(os.path.basename(image_url), 'wb')
    for chunk in image_res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    # find the previous url
    prev_link = funny_soup.select('div.gc-calendar-nav__previous')[0].contents[3]
    comic_url = 'https://www.gocomics.com' + prev_link.get('href')

    i += 1