#-*- coding:utf-8 -*-
"""
@info:
@author:Administrator
@file: A5T1.py
@time: 2021/04/13
"""
import sqlite3
import pandas as pd

conn = sqlite3.connect('mrsoft.db')
cursor = conn.cursor()

# 1
lists = pd.read_csv(r"C:\czy_python_project\czy\self\cur_job\x00101\YVR_Airbnb_reviews.csv")
cursor.execute("select tbl_name from sqlite_master where tbl_name = 'listings1' ")
if cursor.rowcount == 0:
    sql = '''
        create table listings1(
            listing_id int,
            id int,
            date date,
            reviewer_id int,
            reviewer_name int,
            comments text
        )
    '''
    cursor.execute(sql)
    conn.commit()

lists.to_sql(name='listings1',con=conn,index=False,if_exists='append')

# 1
lists = pd.read_csv(r"C:\czy_python_project\czy\self\cur_job\x00101\YVR_Airbnb_listings_summary.csv")
cursor.execute("select tbl_name from sqlite_master where tbl_name = 'listings' ")
if cursor.rowcount == 0:
    sql = '''
        create table listings(
            id int,
            name varchar(64),
            host_id int,
            host_name varchar(64),
            neighbourhood varchar(64),
            room_type varchar(64),
            price int,
            minimum_nights int,
            availability_365 int
        )
    '''
    cursor.execute(sql)
    conn.commit()

lists.to_sql(name='listings',con=conn,index=False,if_exists='append')