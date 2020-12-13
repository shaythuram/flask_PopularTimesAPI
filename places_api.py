# -*- coding: utf-8 -*-

import livepopulartimes
import json

GOOGLE_MAPS_API_KEY = "AIzaSyCTj2k0Hf8b5Iav6W9cVbd4qE17a5l0SiE"

def search(i):
    x = (livepopulartimes.get_populartimes_by_PlaceID(GOOGLE_MAPS_API_KEY, "ChIJfz9ctf8W2jERqme0v9wA_og"))
    return (x["populartimes"][i])


def daily_avg_byID(ID,day):
    x = (livepopulartimes.get_populartimes_by_PlaceID(GOOGLE_MAPS_API_KEY,ID ))
    daily_PT_List = x["populartimes"][day]["data"]
    avg = sum(daily_PT_List) / len(daily_PT_List)
    avg = round(avg,1)
    day = x["populartimes"][day]["name"]
    data = {day:avg}
    return data


def weekly_avg_byID(ID):
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


def weekly_avg_for_each_ID(ID):

    data = []
    for i in ID:
        try:
            data.append(weekly_avg_byID(i))
        except :
            data.append(None)
         
    print(data)
    return data





