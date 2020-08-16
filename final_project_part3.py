#!/usr/bin/python
import json 
from bson import json_util
from pymongo import MongoClient
import math

#Setting up connection to the MongoDB
connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#User defined function find_Moving_Avg
#Parameters: high, low should be numeric
#Returns results as a count of applicable results
def find_Moving_Avg(high, low):
  temp = 0
  if (low > high):
    temp = low
    low = high
    high = temp
  try:
    myQuery = { "50-Day Simple Moving Average" : { "$gt" :  float(low), "$lt" : float(high)}}
    result  = collection.count(myQuery)
  except TypeError as te:
    return str(te)
  else:
    return result

#User defined function find_by_Industry
#Parameter:industry string
#Returns list of ticker symbols for stocks within supplied industry
def find_by_Industry(industry):
  result = []

  try:
    myQuery = {"Industry": industry}
    data = collection.find(myQuery, {"Ticker": 1, "_id": 0})
    
    for document in data:
      result.append(document)
    if not result:
      result = "There were no results returned for the Industry: " + industry
  except TypeError as te:
    return str(te)
  else:
    return result

#User defined function find_by_Sector
#Parameter: sector string
#Returns list grouped by industry totaling the number of outstanding shares
#   within supplIed sector
def find_by_Sector(sector):
  result = []
  try:
    data = collection.aggregate([{"$match": { "Sector" : sector}}, \
          { "$group" : { "_id" : "$Industry", "totalShares": \
                        { "$sum": "$Shares Outstanding"}}}])
  
    for document in data:
      result.append(document)
    if not result:
      result = "There were no results returned for the Sector: " + sector
  except TypeError as te:
    return str(te)
  else:
    return result
  
  
def main():
  #Program loops to allow user to use either of the queries until 'q' is entered 
  # to quit the program
  userInput = ""
  while userInput != "q":
    userInput = raw_input(
      "Enter 'h' for 50-Day Average Query, 'i' for Industry Query, 's' for Sector Query, or 'q' to quit: "
    )
    if userInput == "h":
      #III A i
      userLow = raw_input("Enter 50-Day low avg to query: ")
      res = False
      while not res:
        try :  
          float(userLow) 
          res = True
        except : 
          res = False
        if not res:
          userLow = raw_input("Enter a number for the 50-Day low avg to query:  ")
      userHigh = raw_input("Enter 50-Day high avg to query: ")
      res = False
      while not res:
        try :  
          float(userHigh) 
          res = True
        except : 
          res = False
        if not res:
          userHigh = raw_input("Enter a number for the 50-Day high avg to query: ")
      print find_Moving_Avg(userHigh, userLow)
    elif userInput == "i":
      #III A ii
      userIndustry = raw_input("Enter Industry: ")
      print find_by_Industry(userIndustry)
    elif userInput == "s":
      #III B 
      userSector = raw_input("Enter Sector: ")
      print find_by_Sector(userSector)   
    elif userInput == "q":
      print "good bye"
    else:
      print 'invalid option'
  

  
main()
  