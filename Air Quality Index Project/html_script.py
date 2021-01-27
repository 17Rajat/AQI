# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:18:59 2020

@author: Rajat
""" 
import os
import time
import requests
import sys

def retrieve_html_data():
    for year in range(2013,2019):
        
        for month in range(1,13):
            if (month<10):
                url = "https://en.tutiempo.net/climate/0{}-{}/ws-421820.html".format(month,year)
            else:
                url = "https://en.tutiempo.net/climate/{}-{}/ws-421820.html".format(month,year)
            
            text_info = requests.get(url)
            text_utf = text_info.text.encode('utf=8')
            
            if not os.path.exists("Data/data_html/{}".format(year)):
                os.makedirs("Data/data_html/{}".format(year))
            with open("Data/data_html/{}/{}.html".format(year,month), "wb") as output:
                output.write(text_utf)
        
        sys.stdout.flush()
        
        
        
if __name__ == "__main__":
    start_time = time.time()
    retrieve_html_data()
    stop_time = time.time()
    print("The  time taken is {}".format(stop_time - start_time))