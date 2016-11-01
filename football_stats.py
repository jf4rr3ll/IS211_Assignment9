#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module generates football stats"""

import urllib2
import json
from bs4 import BeautifulSoup

url = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2016-season-regular-category-touchdowns'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())


def footballStats():
    rows = soup.find_all('tr')
    rownum = 0
    if rownum < 20:
        for i in rows:
            try:
                player = i.contents[0].get_text()
                position = i.contents[1].get_text()
                team = i.contents[2].get_text()
                tds = i.contents[6].get_text()
                json_string = {"Player Name": player, "Team": team, "Player Position": position, "Touchdown Total": tds}
                print(json.dumps(json_string))
                rownum += 1
            except:
                continue
    return


if __name__ == "__main__":
    footballStats()