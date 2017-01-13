from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from collections import  defaultdict
#from satool import aggtool
from adverseimpact.forms import DataEntryForm
#PG's libraries first port Twister v.35
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as stats
from pandas import Series, DataFrame, ExcelWriter
import pandas as pd
import csv
import json
import string
import StringIO
from datetime import datetime
import sys
import os
#import sklearn
#import pyttsx
import time

def index(request):
    context = dict()
    context ['title_1'] = " Adverse Impact "
    context['title_2'] = " Science Cloud "
    version_now = "Patch 1.0"
    context["version_now"] = version_now
    data_entry_form = DataEntryForm()
    context['data_entry_form'] = data_entry_form
    #context['start_time'] = start_time
    #return HttpResponse("The sky grows dark...") #this is its just a direct Response
    return render(request, 'adverseimpact/index.html', context)


def effect_summary(request):
    context = dict()
    scoreboard_input_data = os.getcwd() + '/twister/templates/twister/scoreboard_stock.csv'
    ifile = open(scoreboard_input_data, "r+")
    all_scores = pd.read_csv(ifile)
    ifile.close()
    print all_scores
    print all_scores['Field Sample'].sum()

    beat_list = all_scores['Beat Time'].values
    sec_list = []
    for i in beat_list:
        hs = int(i.split(':')[0])*60*60
        ms = int(i.split(':')[1])*60
        s = int(i.split(':')[2])
        sec_list = sec_list + [hs+ms+s]

    UserTime_sec = sum(sec_list)

    if UserTime_sec < 60:
        UserTime_seconds = UserTime_sec
        UserTime_minutes = 0
        UserTime_hours = 0
    elif UserTime_sec < (60*60):
        UserTime_hours = 0
        UserTime_minutes = UserTime_sec / 60
        try:
            UserTime_seconds = UserTime_sec % 60
        except:
            UserTime_seconds = 0
    else:
        UserTime_hours = UserTime_sec / (60*60)
        if UserTime_sec % 60*60 == 0:
            UserTime_minutes = 0
            UserTime_seconds = 0
        else:
            UserTime_minutes = UserTime_sec % 60*60
            if UserTime_sec % 60 == 0:
                UserTime_seconds = 0
            else:
                UserTime_seconds = (UserTime_sec % 60*60) % 60


    if UserTime_minutes < 10:
        UserTime_minutes = '0{}'.format(UserTime_minutes)
    else:
        pass
    if UserTime_seconds < 10:
        UserTime_seconds = '0{}'.format(UserTime_seconds)
    else:
        pass

    context["TotalSample"] = all_scores['Field Sample'].sum()
    context["UserTime_seconds"] = UserTime_seconds
    context["UserTime_minutes"] = UserTime_minutes
    context["UserTime_hours"] = UserTime_hours
    context["TotalRuns"] = len(sec_list)
    return render(request, 'adverseimpact/effect_summary.html', context)
