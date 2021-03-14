# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:30:08 2021

@author: hanyeob
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(data):
    print('start loading', data)
    # 데이터 불러오기
    data_address = 'https://raw.githubusercontent.com/hanyeob/fine_dust/master/csv%20files/'+data+'.csv'
    df = pd.read_csv(data_address)
    df = df[['tt', '0.3_outdoor', '0.5_outdoor', '1.0_outdoor', '3.0_outdoor',
             '5.0_outdoor', '10.0_outdoor', '0.3_classroom', '0.5_classroom',
             '1.0_classroom', '3.0_classroom', '5.0_classroom', '10.0_classroom',
             'CO2_outdoor', 'CO2_classroom']]
    # tt열 시계열 & 인덱스
    df['tt'] = pd.to_datetime(df['tt'], format="%d-%m-%Y %H:%M:%S")
    df.set_index('tt', inplace=True)
    # NaN값 채우기 (bfill & ffill)
    df.fillna(method='bfill', inplace=True)
    df.fillna(method='ffill', inplace=True)
    return df


def unit_change(df):
    df['0.3_outdoor'] = df['0.3_outdoor'] * 0.3 ** 3
    df['0.5_outdoor'] = df['0.5_outdoor'] * 0.5 ** 3
    df['1.0_outdoor'] = df['1.0_outdoor'] * 1.0 ** 3
    df['3.0_outdoor'] = df['3.0_outdoor'] * 3.0 ** 3
    df['5.0_outdoor'] = df['5.0_outdoor'] * 5.0 ** 3
    df['10.0_outdoor'] = df['10.0_outdoor'] * 10.0 ** 3
    df['0.3_classroom'] = df['0.3_classroom'] * 0.3 ** 3
    df['0.5_classroom'] = df['0.5_classroom'] * 0.5 ** 3
    df['1.0_classroom'] = df['1.0_classroom'] * 1.0 ** 3
    df['3.0_classroom'] = df['3.0_classroom'] * 3.0 ** 3
    df['5.0_classroom'] = df['5.0_classroom'] * 5.0 ** 3
    df['10.0_classroom'] = df['10.0_classroom'] * 10.0 ** 3


def merge_to_PM(df):
    df['PM2.5_outdoor'] = np.sum(
        df.loc[:, '0.3_outdoor':'1.0_outdoor'], axis=1)
    df['PM10_outdoor'] = np.sum(
        df.loc[:, '3.0_outdoor':'10.0_outdoor'], axis=1)
    df['PM2.5_classroom'] = np.sum(
        df.loc[:, '0.3_classroom':'1.0_classroom'], axis=1)
    df['PM10_classroom'] = np.sum(
        df.loc[:, '3.0_classroom':'10.0_classroom'], axis=1)


def make_change_column(df):
    df[['PM2.5_classroom_change', 'PM10_classroom_change', 'CO2_classroom_change']
       ] = df[['PM2.5_classroom', 'PM10_classroom', 'CO2_classroom']] - df.shift(1)[['PM2.5_classroom', 'PM10_classroom', 'CO2_classroom']]
    df.dropna(inplace=True)


def scaling(df):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[
        ['CO2_outdoor', 'PM2.5_outdoor', 'PM10_outdoor',
         'CO2_classroom', 'PM2.5_classroom', 'PM10_classroom',
         'CO2_classroom_change', 'PM2.5_classroom_change', 'PM10_classroom_change']
    ])
    scaled_data = pd.DataFrame(data=scaled_data, columns=['CO2_outdoor', 'PM2.5_outdoor', 'PM10_outdoor',
                                                          'CO2_classroom', 'PM2.5_classroom', 'PM10_classroom',
                                                          'CO2_classroom_change', 'PM2.5_classroom_change', 'PM10_classroom_change'])
    scaled_data.set_index(df.index, inplace=True)
    return scaled_data

def add_time(df):
    df = pd.concat([df,df.index.to_frame().loc[:,'tt'].dt.hour], axis=1)
    df.rename(columns={"tt": "hour"}, inplace=True)
    return df


def main():
    print("start")
    # sdc outdoor에 누락데이터 많음
    classlist = ['bbc','isc','nsc','sdc','sic']
    for i in classlist:
        df = load_data(i)
        unit_change(df)
        merge_to_PM(df)
        make_change_column(df)
        scaled_data = scaling(df)
        scaled_data = add_time(scaled_data)
        print(scaled_data.head())
        scaled_data.to_csv(f'./scaled_data/{i}_scaled.csv')

main()

#result

#index : tt
#columns :
# 'CO2_outdoor',         'PM2.5_outdoor',          'PM10_outdoor', 
# 'CO2_classroom',       'PM2.5_classroom',        'PM10_classroom', 
# 'CO2_classroom_change','PM2.5_classroom_change', 'PM10_classroom_change']
