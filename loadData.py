#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:03:43 2018

@author: lydia
"""

import pymongo
import csv
import json
import allDAO
cnx_string = "mongodb://localhost:27017"
cnx = pymongo.MongoClient(cnx_string)
database = cnx.NewYorkCity

print("Chargement des données dans MongoDB (peut prendre quelques minutes)")

print("loading Population ...")
populations = allDAO.PopulationDAO(database)
with open('./downloads/Population.csv','r') as csvfile:
    populationsReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(populationsReader)
    for row in populationsReader:
        #print ', '.join(row)
        data = json.loads("{}")
        data["Age Group"] = row[0]
        data["Borough"] = row[1]
        data["2020"] = row[16]
        populations.insert(data)                   

print("")

print("loading Felonies ...")
felonies = allDAO.FelonyDAO(database)
with open('./downloads/Felonies.csv','r') as csvfile:
    feloniesReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(feloniesReader)
    for row in feloniesReader:
        #print ', '.join(row)
        data = json.loads("{}")
        data["CMPLNT_NUM"] = row[0]
        data["CMPLNT_FR_DT"] = row[1]
        data["CMPLNT_FR_TM"] = row[2]
        data["CMPLNT_TO_DT"] = row[3]
        data["CMPLNT_TO_TM"] = row[4]
        data["RPT_DT"] = row[5]
        data["KY_CD"] = row[6]
        data["OFNS_DESC"] = row[7]
        data["PD_CD"] = row[8]
        data["PD_DESC"] = row[9]
        data["CRM_ATPT_CPTD_CD"] = row[10]
        data["LAW_CAT_CD"] = row[11]
        data["JURIS_DESC"] = row[12]
        data["BORO_NM"] = row[13]
        data["ADDR_PCT_CD"] = row[14]
        data["LOC_OF_OCCUR_DESC"] = row[15]
        data["PREM_TYP_DESC"] = row[16]
        data["PARKS_NM"] = row[17]
        data["HADEVELOPT"] = row[18]
        felonies.insert(data)   
print("Felonies finish")

print("")


print("loading Trees ...")
trees = allDAO.TreeDAO(database)
with open('./downloads/Trees.csv','r') as csvfile:
    treesReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(treesReader)
    for row in treesReader:
        #print ', '.join(row)
        data = json.loads("{}")
        data["status"] = row[6]
        data["borough"] = row[29].upper()
        trees.insert(data)                   
print("Tree finish")   

print("")

print("loading Rodents ...")
rodents = allDAO.RodentDAO(database)
with open('./downloads/Rodents.csv','r') as csvfile:
    rodentsReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(rodentsReader)
    for row in rodentsReader:
        #print ', '.join(row)
        data = json.loads("{}")
        data["BBL"] = row[4]
        data["STREET_NAME"] = row[9]
        data["ZIP_CODE"] = row[10]
        data["BOROUGH"] = row[15].upper()
        rodents.insert(data)                   
print("Rodent finish")   


print("loading Libraries ...")
libraries = allDAO.LibraryDAO(database)
with open('./downloads/Libraries.csv','r') as csvfile:
    librariesReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(librariesReader)
    for row in librariesReader:
        #print ', '.join(row)
        data = json.loads("{}")
        data["the_geom"] = row[0]
        data["NAME"] = row[1]
        data["STREETNAME"] = row[2]
        data["HOUSENUM"] = row[3]
        data["CITY"] = row[4]
        data["ZIP"] = row[5]
        BORO = {'1':"MANHATTAN",'2':"BRONX",'3':"BROOKLYN",'4':"QUEENS",'5':"STATEN ISLAND"}
        data["BORO"] = BORO[row[12]]
        
        libraries.insert(data)
print("Libraries finish")

print("")




print("----")
print("----")

print("finish")