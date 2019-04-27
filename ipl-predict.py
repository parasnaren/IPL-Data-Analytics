import requests
from bs4 import BeautifulSoup

li=[]
def get_item_data():
    url='http://www.espncricinfo.com/ci/content/squad/index.html?object=1165643'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    
    for link in soup.findAll('ul',{'class':'squads_list'}):
        for link2 in link.findAll('a'):
            headline ='http://www.espncricinfo.com'+link2.get('href')

            source_code2 = requests.get(headline)
            plain_text2=source_code2.text
            soup2 = BeautifulSoup(plain_text2, "html.parser")
            for names in soup2.findAll('ul',{'class':'large-block-grid-2 medium-block-grid-2 small-block-grid-1 '}):
                for n in names.findAll('a'):
                    player=n.text
                    li.append(player.strip())
                    
          

get_item_data()
li=pd.DataFrame(li)
li.replace('', np.nan, inplace=True)
li.dropna(inplace=True)
li = li.reset_index(drop=True)
li.to_csv('players2.csv', index=False)


#ooo = pd.read_csv('players2.csv')

import pandas as pd
import numpy as np
from pyxlsb import open_workbook as open_xlsb

player_names = pd.read_csv('players2.csv')
player_names.columns = ["Player's Name"]

def open_ipl(name, sheetno):
    df = []
    with open_xlsb(name) as wb:
        with wb.get_sheet(sheetno) as sheet:
            for row in sheet.rows():
                df.append([item.v for item in row])
    
    df = pd.DataFrame(df[1:], columns=df[0])
    return df

def ind_or_ovs(df):
    if df != "IND":
        return "OVS"
    else:
        return "IND"

def numeric_values(val):
    if val == np.nan:
        return 0
    if type(val) == str:
        return 0
    else:
        return val

## IPL2018
ipl18 = open_ipl('IPL2018.xlsb', 3)
ipl18 = ipl18[["Player's Name", 'From', 'Run', 'Strike Rate', 'Economy', 'Wickets', 'Ct_St', 'Matches Played']]
ipl18['From'] = ipl18['From'].apply(lambda x: ind_or_ovs(x))
ipl18['Average_18'] = pd.to_numeric(ipl18['Run'] / ipl18['Matches Played'])
ipl18['Wkt_per_match_18'] = pd.to_numeric(ipl18['Wickets']/ipl18['Matches Played'])
ipl18['Strike Rate_18'] = ipl18['Strike Rate'].apply(lambda x: numeric_values(x))
ipl18['Economy_18'] = pd.to_numeric(ipl18['Economy'].apply(lambda x: numeric_values(x)))
ipl18['Matches_18'] = ipl18['Matches Played']
ipl18['Ct_St_18'] = ipl18['Ct_St']
ipl18 = ipl18.fillna(0)
ipl18 = ipl18.drop(['Run','Wickets','Strike Rate','Economy','Matches Played','Ct_St'], axis=1)

## IPL2017
ipl17 = open_ipl('IPL2017.xlsb', 3)
ipl17 = ipl17[["Player's Name", 'Run', 'Strike Rate', 'Economy', 'Wickets', 'Ct_St', 'Matches Played']]
ipl17['Average_17'] = pd.to_numeric(ipl17['Run'] / ipl17['Matches Played'])
ipl17['Wkt_per_match_17'] = pd.to_numeric(ipl17['Wickets']/ipl17['Matches Played'])
ipl17['Strike Rate_17'] = ipl17['Strike Rate'].apply(lambda x: numeric_values(x))
ipl17['Economy_17'] = pd.to_numeric(ipl17['Economy'].apply(lambda x: numeric_values(x)))
ipl17['Matches_17'] = ipl17['Matches Played']
ipl17['Ct_St_17'] = ipl17['Ct_St']
ipl17 = ipl17.fillna(0)
ipl17 = ipl17.drop(['Run','Wickets','Strike Rate','Economy','Matches Played','Ct_St'], axis=1)


### IPL2016
ipl16 = open_ipl('IPL2016.xlsb', 2)
ipl16 = ipl16[["Player's Name", 'Run', 'Strike Rate', 'Economy', 'Wickets', 'Ct_St', 'Matches Played']]
ipl16['Average_16'] = pd.to_numeric(ipl16['Run'] / ipl16['Matches Played'])
ipl16['Wkt_per_match_16'] = pd.to_numeric(ipl16['Wickets']/ipl16['Matches Played'])
ipl16['Strike Rate_16'] = ipl16['Strike Rate'].apply(lambda x: numeric_values(x))
ipl16['Economy_16'] = pd.to_numeric(ipl16['Economy'].apply(lambda x: numeric_values(x)))
ipl16['Matches_16'] = ipl16['Matches Played']
ipl16['Ct_St_16'] = ipl16['Ct_St']
ipl16 = ipl16.fillna(0)
ipl16 = ipl16.drop(['Run','Wickets','Strike Rate','Economy','Matches Played','Ct_St'], axis=1)


### IPL2015
ipl15 = open_ipl('IPL2015.xlsb', 1)
ipl15 = ipl15[["Player's Name", 'Run', 'Strike Rate', 'Economy', 'Wickets', 'Ct_St', 'Matches Played']]
ipl15['Average_15'] = pd.to_numeric(ipl15['Run'] / ipl15['Matches Played'])
ipl15['Wkt_per_match_15'] = pd.to_numeric(ipl15['Wickets']/ipl15['Matches Played'])
ipl15['Strike Rate_15'] = ipl15['Strike Rate'].apply(lambda x: numeric_values(x))
ipl15['Economy_15'] = pd.to_numeric(ipl15['Economy'].apply(lambda x: numeric_values(x)))
ipl15['Matches_15'] = ipl15['Matches Played']
ipl15['Ct_St_15'] = ipl15['Ct_St']
ipl15 = ipl15.fillna(0)
ipl15 = ipl15.drop(['Run','Wickets','Strike Rate','Economy','Matches Played','Ct_St'], axis=1)


ipl = pd.merge(player_names, ipl18, how='left', on="Player's Name")
ipl = pd.merge(ipl, ipl17, how='left', on="Player's Name")
ipl = pd.merge(ipl, ipl16, how='left', on="Player's Name")
ipl = pd.merge(ipl, ipl15, how='left', on="Player's Name")
ipl = ipl.fillna(0)
ipl2 = ipl.drop_duplicates("Player's Name")

#ipl2.to_csv('ipl_total.csv', index=False)

#ipl2 = pd.read_csv('ipl_total.csv').drop('Unnamed: 0', axis=1)
ipl = pd.DataFrame()
ipl['Name'] = ipl2["Player's Name"]
ipl['From'] = ipl2['From']
ipl['Batting score_18'] = ipl2['Average_18'] + 0.01*ipl2['Strike Rate_18']
ipl['Bowling score_18'] = (ipl2['Wkt_per_match_18'] - 0.005*ipl2['Economy_18'] )*ipl2['Matches_18']
ipl['Allround score_18'] = ipl['Batting score_18'] * ipl['Bowling score_18']
ipl['Matches_18'] = ipl2['Matches_18']
ipl['Batting score_17'] = ipl2['Average_17'] + 0.1*ipl2['Strike Rate_17']
ipl['Bowling score_17'] = (ipl2['Wkt_per_match_17'] - 0.005*ipl2['Economy_17'])*ipl2['Matches_17']
ipl['Allround score_17'] = ipl['Batting score_17'] * ipl['Bowling score_17']
ipl['Matches_17'] = ipl2['Matches_17']
ipl['Batting score_16'] = ipl2['Average_16'] + 0.1*ipl2['Strike Rate_16']
ipl['Bowling score_16'] = (ipl2['Wkt_per_match_16'] - 0.005*ipl2['Economy_16'])*ipl2['Matches_16']
ipl['Allround score_16'] = ipl['Batting score_16'] * ipl['Bowling score_16']
ipl['Matches_16'] = ipl2['Matches_16']
ipl['Batting score_15'] = ipl2['Average_15'] + 0.1*ipl2['Strike Rate_15']
ipl['Bowling score_15'] = (ipl2['Wkt_per_match_15'] - 0.005*ipl2['Economy_15'])*ipl2['Matches_15']
ipl['Allround score_15'] = ipl['Batting score_15'] * ipl['Bowling score_15']
ipl['Matches_15'] = ipl2['Matches_15']

#ipl.to_csv('ipl_scores.csv', index=False)

######################################################
#ipl = pd.read_csv('ipl_scores.csv')

final = pd.DataFrame()
final['Name'] = ipl['Name']
final['From'] = ipl['From']
final['Batting score'] = ipl['Batting score_18'] + 0.8*ipl['Batting score_17'] + 0.6*ipl['Batting score_16'] + 0.4*ipl['Batting score_18']
final['Bowling score'] = ipl['Bowling score_18'] + 0.8*ipl['Bowling score_17'] + 0.6*ipl['Bowling score_16'] + 0.4*ipl['Bowling score_18']
final['Allround score'] = ipl['Allround score_18'] + 0.8*ipl['Allround score_17'] + 0.6*ipl['Allround score_16'] + 0.4*ipl['Allround score_18']

#final.to_csv('final.csv', index=False)

df = final

batsmen=pd.DataFrame()
batsmen['Name']=df['Name']
batsmen['From']=df['From']
batsmen['Batting score']=df['Batting score']
batsmen = batsmen.sort_values(by=['Batting score' ],ascending=False)[:10]
batsmen.to_csv('ipl_batsmen.csv', index=False)

bowlers=pd.DataFrame()
bowlers['Name']=df['Name']
bowlers['From']=df['From']
bowlers['Bowling score']=df['Bowling score']
bowlers = bowlers.sort_values(by=['Bowling score' ],ascending=False)[:10]
bowlers.to_csv('ipl_bowlers.csv', index=False)

all_rounders=pd.DataFrame()
all_rounders['Name']=df['Name']
all_rounders['From']=df['From']
all_rounders['Allround score']=df['Allround score']
all_rounders = all_rounders.sort_values(by=['Allround score' ],ascending=False)[:10]
all_rounders.to_csv('ipl_allrounders.csv', index=False)

ovs = 3
c = 0
bat = []
players = []
print("\n-- 5 batsmen --")
for i, row in batsmen.iterrows():
    if c == 5:
        break
    if ovs and row['From'] != 'IND':
        ovs-=1
    elif not ovs and row['From'] != 'IND':
        continue
    #print(c+1, ': ', row['Name'], row['From'])
    c+=1
    bat.append(row['Name'])
    players.append([row['Name'], row['From'], 'Batsman'])

ovs = 1
c = 0
print("\n-- 3 allrounders --")
for i, row in all_rounders.iterrows():
    if c == 3:
        break
    if ovs and row['From'] != 'IND':
        ovs-=1
    elif not ovs and row['From'] != 'IND':
        continue
    #print(c+1, ': ', row['Name'], row['From'])
    c+=1
    players.append([row['Name'], row['From'], 'All-rounder'])

ovs = 0
c = 0
print("\n-- 3 bowlers -- ")
for i, row in bowlers.iterrows():
    if c == 3:
        break
    if ovs and row['From'] != 'IND':
        ovs-=1
    elif not ovs and row['From'] != 'IND':
        continue
    #print(c+1, ': ', row['Name'], row['From'])
    c+=1
    players.append([row['Name'], row['From'], 'Bowler'])
    

ipl['catches'] = ipl2['Ct_St_18']+ipl2['Ct_St_17']+ipl2['Ct_St_16']+ipl2['Ct_St_15']
    
ct = pd.concat([ipl['Name'], ipl['catches']], axis=1).sort_values(by=['catches'], ascending=False)
for i, row in ct.iterrows():
    if row['Name'] in bat:
        #print('Wicketkeeper: ', row['Name'])
        wk = row['Name']
        break

for i in range(len(players)):
    if players[i][0] == wk:
        players[i][2] = 'Batsman/Wicketkeeper'
        break
    
for i in players:
    for x, y, z in i:
        print(x,'\t', y, '\t', z)
    print()
    
fin = pd.DataFrame(players, columns = ['Name','From','Position'])
fin.to_csv('final_11.csv', index=False)