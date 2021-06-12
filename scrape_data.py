from bs4 import BeautifulSoup
from urllib.request import urlopen,Request
import pandas as pd
def operation_with_row_data(row):
    row_list=[]
    imagelink=""
    countrylink=""
    if row.find('th')!=None:
        if row.find('th').find('img')!=None:
            imagelink=row.find('th').find("img")['src']
    else:
        imagelink="None"
    if len(row.find_all('th'))>0:
        if row.find_all('th')[1]!=None:
            if row.find_all('th')[1].find('a')!=None:
                #countrylink=row.find('th').find("a")['href']
                countrylink=row.find_all('th')[1].find("a")['href']
        else:
            countrylink="None"


    data=row.text
    #print(data.replace('\n',','))
    data=data.strip()
    data=data.replace('\n',',')
    data=data.split(",,")
    data[0]=data[0].lower()
    if data[1]!="No data" and data[1]!="No data" and data[3]!="No data":
        t=int(data[1].replace(',',''))
        d=int(data[2].replace(',',''))
        r=int(data[3].replace(',',''))
        a=t-(d+r)
        data[4]=a
    else:
        data[4]="Not Found"
    data.append(imagelink)
    data.append(countrylink)
    return data

def return_data():
    html=urlopen("https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data").read()
    soup=BeautifulSoup(html,"lxml")

    table = soup.find('table',{"class":"wikitable"}).find('tbody')

    all_rows = table.find_all('tr')
    #print(len(all_rows))
    all_rows.pop(0)
    all_rows.pop()
    all_rows.pop()

    main_list=[]
    
    for row in all_rows: 
        #print(operation_with_row_data(row))
        main_list.append(operation_with_row_data(row))
    main_list.pop(0)
    #main_list.pop(0)
   

    worlddata=main_list[0]
    
    return main_list,worlddata



def globe_data():
    req=Request("https://www.worldometers.info/coronavirus/", headers={'User-Agent': 'Mozilla/5.0'})
    html=urlopen(req).read()
    soup=BeautifulSoup(html,"lxml")

    table = soup.find('table',{"id":"main_table_countries_today"}).find('tbody')
    all_rows = table.find_all('tr')
    del all_rows[0:7]
    main_list=[]
    for row in all_rows:
        small_list=[]
        columns=row.find_all('td')
        for column in columns:
            small_list.append(column.text)
        main_list.append(small_list)
    return main_list


def row_operation_on_country(row):
    data=row.text
    #print(data.replace('\n',','))
    data=data.strip()
    data=data.replace('\n',',')
    data=data.split(",,")
    data[0]=data[0].lower()
    return data


'''
def india():
    html=urlopen("https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India").read()
    soup=BeautifulSoup(html,"lxml")

    table = soup.find('table',{"class":"wikitable"}).find('tbody')

    all_rows = table.find_all('tr')
    print(len(all_rows))
    
    main_list=[]
    
    for row in all_rows: 
        main_list.append(row_operation_on_country(row))
    main_list.pop(0)
    main_list.pop(0)
    india=main_list[0]
    main_list.pop(0)
    main_list.pop()
    main_list.pop()
    
    return main_list,india
'''
'''
def district_wise_state_data(state_name):
    
    req=Request("https://www.grainmart.in/news/covid-19-coronavirus-india-state-and-district-wise-tally/", headers={'User-Agent': 'Mozilla/5.0'})
    html=urlopen(req).read()
    soup=BeautifulSoup(html,"lxml")
    result_list=[]
    
    html = urlopen('http://www.grainmart.in/news/covid-19-coronavirus-india-state-and-district-wise-tally/').read()
    soup  = BeautifulSoup(html,'lxml')
    
    table = soup.find("section",{"id":"covid-19-table"})
    state_rows = table.find_all('div',{'class','skgm-states'})
    for state_row in state_rows:
        if (state_row.find('span',{'class','show-district'}).text)[0:5] == state_name[0:5]:
            districts=state_row.find('div',{'class','skgm-districts'})
            district_rows = districts.find_all('div',{'class','skgm-tr'})
            for district_row in district_rows:
                small_list=[]
                columns = district_row.find_all('div',{'class','skgm-td'})
                for column in columns:
                    data=(column.string).strip()
                    small_list.append(data)
                print(small_list)
                result_list.append(small_list)
            break
    return result_list
'''
def district_wise_state_data(state_name):
    data = pd.read_csv('https://api.covid19india.org/csv/latest/district_wise.csv')

    result_list=[]
    for d in data.index:
        if data['State'][d][0:5]==state_name[0:5]:
            small_list=[data['District'][d],str(data['Confirmed'][d]),
            str(data['Active'][d]),str(data['Recovered'][d]),
            str(data['Deceased'][d]),str(data['Delta_Confirmed'][d]),str(data['Delta_Active'][d]),
            str(data['Delta_Recovered'][d]),str(data['Delta_Deceased'][d])]
            #print(small_list)
            result_list.append(small_list)
    return result_list


def india():
    data = pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')
    result_list=[]
    for d in data.index:
        small_list=[]
        small_list=[str(data["State"][d]).lower(),
        str(data['Confirmed'][d]),str(data['Recovered'][d]),
        str(data['Deaths'][d]),str(data['Active'][d]),
        str(data['Delta_Confirmed'][d]),str(data['Delta_Recovered'][d]),
        str(data['Delta_Deaths'][d]),str(data['Last_Updated_Time'][d]),
        str(data['Migrated_Other'][d])]
        #print(small_list)
        result_list.append(small_list)
    
    india=result_list[0]
    result_list.pop(0)
    return result_list,india
    

def state_name():
    data = pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')
    result_list=[]
    for d in data.index:
        result_list.append(data['State'][d])
    return result_list

def district_page_response(state_name):
    state_info=[]
    data = pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')
    for d in data.index:
        if data['State'][d][0:5] == state_name[0:5]:
            state_info=[str(data["State"][d]),
            str(data['Confirmed'][d]),str(data['Recovered'][d]),
            str(data['Deaths'][d]),str(data['Active'][d]),
            str(data['Delta_Confirmed'][d]),str(data['Delta_Recovered'][d]),
            str(data['Delta_Deaths'][d]),str(data['Last_Updated_Time'][d]),
            str(data['Migrated_Other'][d])]
            break;

    data = pd.read_csv('https://api.covid19india.org/csv/latest/district_wise.csv')
    result_list=[]
    for d in data.index:
        if data['State'][d][0:5]==state_name[0:5]:
            small_list=[data['District'][d],str(data['Confirmed'][d]),
            str(data['Active'][d]),str(data['Recovered'][d]),
            str(data['Deceased'][d]),str(data['Delta_Confirmed'][d]),str(data['Delta_Active'][d]),
            str(data['Delta_Recovered'][d]),str(data['Delta_Deceased'][d])]
            #print(small_list)
            result_list.append(small_list)
    return state_info,result_list


def india_stats():
    india_info=[]
    data = pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')
    for d in data.index:
        if data['State'][d] == 'Total':
            india_info=[str(data["State"][d]).lower(),
            str(data['Confirmed'][d]),str(data['Recovered'][d]),
            str(data['Deaths'][d]),str(data['Active'][d]),
            str(data['Delta_Confirmed'][d]),str(data['Delta_Recovered'][d]),
            str(data['Delta_Deaths'][d]),str(data['Last_Updated_Time'][d]),
            str(data['Migrated_Other'][d])]
            break;
    
    data = pd.read_csv('https://api.covid19india.org/csv/latest/case_time_series.csv')
    growth_result=[]
    for d in data.index:
        small_list=[data['Date'][d].strip().split(),int(data['Total Confirmed'][d]),int(data['Total Recovered'][d]),int(data['Total Deceased'][d])]
        growth_result.append(small_list)

    daily_result=[]
    for d in data.index:
        small_list=[data['Date'][d].strip().split(),int(data['Daily Confirmed'][d]),int(data['Daily Recovered'][d]),int(data['Daily Deceased'][d])]
        daily_result.append(small_list)

    return india_info,growth_result,daily_result
#print(india_stats())
state_code={'Andaman and Nicobar Islands': 'AN', 'Andhra Pradesh': 'AP', 
'Arunachal Pradesh': 'AR', 'Assam': 'AS', 'Bihar': 'BR', 'Chandigarh': 'CH',
 'Chhattisgarh': 'CT', 'Dadra and Nagar Haveli and Daman and Diu': 'DN',
  'Delhi': 'DL', 'Goa': 'GA', 'Gujarat': 'GJ', 'Haryana': 'HR', 
  'Himachal Pradesh': 'HP', 'Jammu and Kashmir': 'JK', 'Jharkhand': 'JH', 
  'Karnataka': 'KA', 'Kerala': 'KL', 'Lakshadweep': 'LD', 'Madhya Pradesh': 'MP',
   'Maharashtra': 'MH', 'Manipur': 'MN', 'Meghalaya': 'ML', 'Mizoram': 'MZ', 
   'Nagaland': 'NL', 'Odisha': 'OR', 'Puducherry': 'PY', 'Punjab': 'PB', 
   'Rajasthan': 'RJ', 'Sikkim': 'SK', 'Tamil Nadu': 'TN', 'Telangana': 'TG', 
   'Tripura': 'TR', 'Uttar Pradesh': 'UP', 'Uttarakhand': 'UT', 'West Bengal': 'WB'}
'''
def timepass():
    state_code={}
    html = urlopen('https://kb.bullseyelocations.com/support/solutions/articles/5000695302-india-state-codes').read()
    soup = BeautifulSoup(html,'lxml')
    rows  = soup.find('table').find('tbody').find_all('tr')
    for row in rows:
        small_list=[]
        for td in row.find_all('td'):
            small_list.append(td.text)
        small_list.pop()
        state_code[small_list[0]]=small_list[1]
    del state_code['State Name']
    print(state_code)
    print(len(state_code))
#timepass()
'''
def get_statecode(state_name):
    for key,value in state_code.items():
        if state_name  in key:
            return value
    return 'Not Found'

#print(get_statecode("Dadra and Nagar Haveli and Daman and Diu"))

def statewise_statistic(state_name):
    state_code=get_statecode(state_name)
    if state_code == 'Not Found':
        return 'No Data'
    Confirmed_list=[]
    Recovered_list=[]
    Death_list=[]

    data=pd.read_csv('https://api.covid19india.org/csv/latest/state_wise_daily.csv')
    for d in data.index:
        date=data['Date'][d].split('-')
        
        if data['Status'][d] == 'Confirmed':
            Confirmed_list.append([date,data['Status'][d],int(data[state_code][d])])
        if data['Status'][d] == 'Recovered':
            Recovered_list.append([date,data['Status'][d],int(data[state_code][d])])
        if data['Status'][d] == 'Deceased':
            Death_list.append([date,data['Status'][d],int(data[state_code][d])])

    return Confirmed_list,Recovered_list,Death_list

import requests
import json
def covid_news():
    result_list=[]
    x = requests.get('http://covid-19india-api.herokuapp.com/headlines')
    data=json.loads(x.text)
    if len(data['headlines'])== len(data['headlines_summary']) and len(data['headlines'])== len(data['image_link']):
        for i in range(len(data['headlines'])):
            small_list=[data['headlines'][i],data['headlines_summary'][i],data['image_link'][i] ]
            result_list.append(small_list)
    return result_list
#state_news()


def timepass():
    data = pd.read_csv('https://api.covid19india.org/csv/latest/case_time_series.csv')
    high= int(data.tail(1)['Total Confirmed'])//100000
    #print(high)
    small_list=[]
    privious_value=0
    for i in range(1,high+1):
        j=0
        for d in data.index:
            if int(data['Total Confirmed'][d]) > i*100000:
                small_list.append(j)
                break
            j=j+1
    new_list=[]
    for i in range(0,len(small_list)):
        if i == 0:
            new_list.append({"y":small_list[i],"label":str(i*100000)+" to "+str((i+1)*100000)})
            continue
        elif len(small_list)-1 ==i:
            value = small_list[i] -small_list[i-1]
            new_list.append({"y":value,"label":str(i*100000)+" to "+str((i+1)*100000)})
        else:
            value = small_list[i] -small_list[i-1]
            new_list.append({"y":value,"label":str(i*100000)+" to "+str((i+1)*100000)})
    #print(new_list)
    return new_list