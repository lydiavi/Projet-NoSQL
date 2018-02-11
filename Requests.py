#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 21:35:48 2018

@author: lydia
"""

import pymongo
from collections import OrderedDict
from operator import itemgetter


## Connexion à MongoDB et à la base de données NewYorkCity
cnx_string = "mongodb://localhost:27017"
cnx = pymongo.MongoClient(cnx_string)
database = cnx.NewYorkCity


##  On définie une variables par Collection
population = database.populations
felonies = database.felonies
libraries = database.libraries
trees = database.trees
rodents = database.rodents
stations = database.stations


## Pour pouvoir comparer les différents Borough,
## on récupère le nombre d'habitants par Borough.

popsQuery = list(population.find({},{'Borough':1,'2020':1,'_id':0} ))

result = dict()

for pq in popsQuery :
    result[pq['Borough'][3:].upper()] = float(pq['2020'])

print("Nombre d'habitants par Borough : ")
print(result)
print(" ")
print(" ")

## Premier critère de sélection :
## nombre crimes / pop -> faible.

felsQuery = list(felonies.aggregate([
        {'$group': {'_id': "$BORO_NM", 'tot':{ "$sum": 1}}}
]))
    
for fq in felsQuery :
    result[fq['_id']] = float(fq['tot'])/result[fq['_id']]

print("Crimes par habitants : ")
print(result)
print(" ")
print(" ")

## Trie pour ne garder que les 3 plus faibles

result= OrderedDict(sorted(result.items(), key=itemgetter(1)))

meilleurs = result.keys()[0:3]

print("Les 3 boroughs avec le plus faible nombre de crimes par habitants : ")
print(meilleurs)
print(" ")
print(" ")


result = {key:result[key] for key in meilleurs}
  


## Deuxième critère de sélection :
## taux d'arbres en bon état.  
totTrees = trees.find({'borough':{'$in':meilleurs},'status':"Alive"}).count()

treesQuery = list(trees.aggregate([
    {'$match':{'borough':{'$in':meilleurs},'status':"Alive"}},
    {'$group':{'_id' : "$borough",'count':{'$sum':1}}},
    {'$project':{'percent':{'$divide':["$count",totTrees]}
    }
  },
    {'$sort':{'percent':-1}}
]))

for tq in treesQuery :
    result[tq['_id']] = float(tq['percent'])
    
result = OrderedDict(sorted(result.items(), key=itemgetter(1)))

print("Taux d'arbres en bon état pour les 3 boroughs : ")
print(result)
print(" ")
print(" ")

meilleurs = result.keys()[len(result)-2:len(result)]
print("Les 2 boroughs avec le taux le plus élevé d'arbres : ")
print(meilleurs)
print(" ")
print(" ")

## Troisième critère de sélection :
## Hygiène -> pas de rats.

ratsQuery = list(rodents.aggregate([
    {'$match':{'BOROUGH':{'$in':meilleurs}}},
    {'$group':{'_id' : "$ZIP_CODE",'count':{'$sum':1}}},
    {'$sort':{'count':-1}}
]))
    
maxrats = ratsQuery[0]['count']
print(maxrats)
result = {dict['_id']: dict['count'] for dict in ratsQuery}

# la base données comporte des erreurs de correspondance ZIP/Borough 
print("Les ZIP du Queens et de Brooklyn et leur nombre de rats : ")
print(result)
print(" ")
print(" ")
 
## Quatrième critère de sélection :
## avoir une bibiliotèque.

libsQuery = list(libraries.aggregate([
    {'$match':{'BORO':{'$in':meilleurs}}},
    {'$group':{'_id' : "$ZIP",'count':{'$sum':1}}},
    {'$sort':{'count':-1}}
]))
    

print("Les ZIP du Queens et de Brooklyn et leur nombre de rats : ")
print(libsQuery)
print(" ")
print(" ")

resultlib = dict()

# scoring des Zipcode en fonction du nombre de rats et de bibliotèques
for zipcode in libsQuery:
    if zipcode['_id'] in result.keys():
        resultlib[zipcode['_id']]=-(float(result[zipcode['_id']]*5)/float(37147))+zipcode['count']
    
resultlib = OrderedDict(sorted(resultlib.items(), key=itemgetter(1)))

print("Les ZIP du Queens et de Brooklyn et leur score (fonction du nombre de rats et de bibliotèques) : ")
print(resultlib)
print(" ")
print(" ")

meilleurs = resultlib.keys()[len(resultlib)-3:len(resultlib)]

print("Les 3 ZIPs avec les meilleurs scores : ")
print(meilleurs)
print(" ")
print(" ")

