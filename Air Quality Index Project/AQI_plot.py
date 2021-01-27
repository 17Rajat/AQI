# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 23:10:32 2020

@author: Rajat

"""
import pandas as pd
import matplotlib.pyplot as plt 

def average_data_2013():
    temp_i = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2013.csv',chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data = rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)
                    add_var = add_var + temp
        
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    return average 



def average_data_2014():
    temp_i = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2014.csv',chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data = rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)
                    add_var = add_var + temp
        
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    return average

def average_data_2015():
    temp_i = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2015.csv',chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data = rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)
                    add_var = add_var + temp
        
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    return average
    

def average_data_2016():
    temp_i = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2016.csv',chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data = rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)
                    add_var = add_var + temp
        
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    return average        


def average_data_2017():
    temp_i = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2017.csv',chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data = rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)
                    add_var = add_var + temp
        
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    return average

def average_data_2018():
    temp_i = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2018.csv',chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data = rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)
                    add_var = add_var + temp
        
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    return average

if __name__ == "__main__":
    lst_2013 = average_data_2013()
    lst_2014 = average_data_2014()
    lst_2015 = average_data_2015()
    lst_2016 = average_data_2016()
    lst_2017 = average_data_2017()
    lst_2018 = average_data_2018()
    plt.plot(range(0,365),lst_2013,label="2013 data")
    plt.plot(range(0,364),lst_2014,label="2014 data")
    plt.plot(range(0,365),lst_2015,label="2015 data")
    # plt.plot(range(0,121),lst_2016,label="2016 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()