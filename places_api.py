# -*- coding: utf-8 -*-

import livepopulartimes
import json

GOOGLE_MAPS_API_KEY = "INSERT YOUR API KEY HERE"


def search(i):
    x = (livepopulartimes.get_populartimes_by_PlaceID(GOOGLE_MAPS_API_KEY, "ChIJfz9ctf8W2jERqme0v9wA_og"))
    return (x["populartimes"][i])



############################  WEEKLY AVERAGE FOR EACH STORE ################################
def weekly_avg_for_each_ID(ID):
    x = (livepopulartimes.get_populartimes_by_PlaceID(GOOGLE_MAPS_API_KEY,ID ))
    x = x["populartimes"]
    l = []
    for i in x:
        daily_List = i["data"]
        avg = sum(daily_List) / len(daily_List)
        avg = round(avg,3)
        l.append(avg)
    weekly_avg = sum(l) / len(l)
    weekly_avg= round(weekly_avg,1)
    return weekly_avg


def weekly_avg_byID(ID):

    data = []
    for i in ID:
        try:
            data.append(weekly_avg_for_each_ID(i))
        except :
            data.append(None)
         
    # print(data)
    return data



############################  DAILY AVERAGE FOR EACH STORE ################################


def daily_avg_for_each_ID(ID,day):
    x = (livepopulartimes.get_populartimes_by_PlaceID(GOOGLE_MAPS_API_KEY,ID ))
    daily_PT_List = x["populartimes"][day]["data"]
    # print(daily_PT_List , ID)
    avg = sum(daily_PT_List) / len(daily_PT_List)
    avg = round(avg,1)
    return avg

def daily_avg_byID(ID,day):

    data = []
    for i in ID:
        try:
            data.append(daily_avg_for_each_ID(i,day))
        except :
            data.append(None)
         
    # print(data)
    return data

############################  HOURLY VALUE FOR EACH STORE ################################



def hourly_for_each_ID(ID,day,hour):
    x = (livepopulartimes.get_populartimes_by_PlaceID(GOOGLE_MAPS_API_KEY,ID ))
    hourly_value = x["populartimes"][day]["data"][hour]
    # print(hourly_value)
    return hourly_value

def hourly_data(ID,day,hour):

    data = []
    for i in ID:
        try:

            data.append(hourly_for_each_ID(i,day,hour))
        except :
            data.append(None)
         
    # print(data)
    return data





if __name__ == '__main__':
    store_list = ['ChIJL2u2o7YX2jERLceCHtqWtbg', 'ChIJJ4D-iA0W2jERMYhpmY9c0tM', 'ChIJl90eFkYW2jERJrNOeEpFn8M', 'ChIJm1VWmzcW2jERw59ivKJB_ec', 'ChIJjfwsS6YX2jERe2R1BY6qD78', 'ChIJ_fViycoX2jERTz46epUpx58', 'ChIJP1zOtHkX2jERarC4GGPgQSQ']
    hourly_data(store_list ,2,12)
