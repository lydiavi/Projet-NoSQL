#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:05:40 2018

@author: lydia
"""

class FelonyDAO(object):

#Initialize our DAO class with the database and set the MongoDB collection we want to use
	def __init__(self, database):
		self.db = database
		self.felonies = database.felonies
		self.felonies.delete_many({})

#This function will handle the insertion of names
	def insert(self,data):
		self.felonies.insert(data)
        

class LibraryDAO(object):

#Initialize our DAO class with the database and set the MongoDB collection we want to use
	def __init__(self, database):
		self.db = database
		self.libraries = database.libraries
		self.libraries.delete_many({})
         

#This function will handle the insertion of names
	def insert(self,data):
		self.libraries.insert(data)
                

      
class PopulationDAO(object):

#Initialize our DAO class with the database and set the MongoDB collection we want to use
	def __init__(self, database):
		self.db = database
		self.populations = database.populations
		self.populations.delete_many({})

#This function will handle the insertion of names
	def insert(self,data):
		self.populations.insert(data)
        
        
        
class RodentDAO(object):

#Initialize our DAO class with the database and set the MongoDB collection we want to use
	def __init__(self, database):
		self.db = database
		self.rodents = database.rodents
		self.rodents.delete_many({})

#This function will handle the insertion of names
	def insert(self,data):
		self.rodents.insert(data)
        
class TreeDAO(object):

#Initialize our DAO class with the database and set the MongoDB collection we want to use
	def __init__(self, database):
		self.db = database
		self.trees = database.trees
		self.trees.delete_many({})

#This function will handle the insertion of names
	def insert(self,data):
		self.trees.insert(data)