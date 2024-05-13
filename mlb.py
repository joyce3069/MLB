import psycopg2
import requests
import json
import numpy as np
import pandas as pd
import time
import statsapi

mlb = statsapi.schedule(start_date= '1991-03-01', 
                        end_date='1991-10-31', 
                        team="", 
                        opponent="", 
                        game_id=None)


df_mlb=pd.json_normalize(mlb)

df_mlb_r = df_mlb[df_mlb['game_type']=="R"]

mlb_r= df_mlb_r[['game_id', 'game_datetime', 'game_date',
                     'away_name', 'home_name', 'away_id', 
                                      'home_id','venue_id', 'venue_name']]


#for i in range(1992, 2019):
    #y= statsapi.schedule(
                        #start_date=str(i)+'-03-01', 
                        #end_date=str(i)+'-10-31', 
                        #team="", opponent="",
                        #game_id=None)
        
    
   # mb=pd.json_normalize(y)
    #mbr = mb[mb['game_type']=="R"]
    #mb1 = mbr[['game_id', 'game_datetime', 'game_date',
                #'away_name', 'home_name', 'away_id', 
                 #'home_id','venue_id', 'venue_name']]
    #mlb_r = pd.concat([mlb_r, mb1], ignore_index=True)

game_ids=mlb_r['game_id'].unique().astype(list)


conn = psycopg2.connect(host='localhost',
                        port=5433,
                        database='postgres',
                        user='postgres',
                        password='q1w2e3r4***',
                        connect_timeout=10)


cur = conn.cursor()

sql = 'DROP TABLE IF EXISTS mlb_1991 CASCADE;'
print(sql)
cur.execute(sql)

sql = 'CREATE TABLE IF NOT EXISTS mlb_1991 (id INTEGER, total_hr INTEGER, temp INTEGER)'
print(sql)
cur.execute(sql)

for gid in game_ids:
    url='https://statsapi.mlb.com/api/v1/game/'+str(gid)+'/boxscore'
    r=requests.get(url)
    txt = json.loads(r.text)
    hr=txt['teams']['home']['teamStats']['batting']['homeRuns']
    ar=txt['teams']['away']['teamStats']['batting']['homeRuns']
    total=hr+ar
    for i in range(len(txt['info'])):
        if txt['info'][i]['label']=='Weather':
            temp =int(txt['info'][i]['value'][:2])
    sql = 'INSERT INTO mlb_1991 (id, total_hr, temp) VALUES (%s, %s, %s);'
    print(sql)
    cur.execute(sql, (gid, total, temp))

conn.commit()
cur.close()

exit()

