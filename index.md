# Self Assessment
To say I learned a lot during my time in the Computer Science program at Southern New Hampshire University would be an understatement. Throughout the program I learned everything from basic coding in multiple languages, such as Python, Java, and C++, to some more advanced concepts in the later classes. I found my strengths lie in databases. Using programs like SQL worked well with my understanding of numbers and collected data and showed me a new way to manipulate that information. In my ePortfolio, that is enhanced with my artifact centered around the MongoDB database system. As the program continued, I found that a lot of programing’s success is based off of working in a group or team. I have taken classes that worked in the Github and taught us how to do things like code review and working as a team to build a successful program. I have had experience with security while taking networking classes where I had to learn how to install and maintain a network. Software engineering is highlighted in enhancement one where I had to remove unused imports and updating the main method to add the while loop as well as adding comments for better readability. Enhancement two showcases data structures where I had to expand certain methods as well as type checking for the user input to allow the program to be more user friendly. 

# The Artifact
The artifact that I enhanced is the final project from CS340, specifically, part three of the final project. The program was originally created in June of 2020 as I finished up the Advanced Programming Concepts class. The artifact is a python module used to query a MongoDB database. I chose this artifact because not only was it simple enough to run and manipulate, but it also encompassed all three sections that needed to be highlighted for the ePortfolio. 

You can view the entire enhanced artifact [here](https://github.com/djc0428/djc0428.github.io/blob/master/final_project_part3.py)

# Code Review of Original Artifact
<video src="2 CS499 Milestone 1.mp4" width="600" height="500" controls preload></video>

## Enhancement One: Software Design and Engineering
The section being looked at for the software design and engineering part of the portfolio showcases the use of multiple functions within the class, data structures, and common practices for software development. The improvements made were adding comments to make it more readable, made it more concise by removing unnecessary imports, and enhanced the usability by allowing the user to call any of the methods without changing the code and restarting the program.

### Reflection 

When creating the original project the goal was to query the MongoDB database for the goals specified by the assignment. When improving it, I learned to create more concise and well documented code, as well as an increased focus on user interaction versus meeting technical guidelines. There weren’t too many challenges when tackling this part of the portfolio. I could look at determining which imports could be removed as a challenge, as well as providing comments that would clearly describe the methods without being overly wordy. Also I had to align the logic to toggle through each of the calls in the main methods. 

Below is a snippet from the main method of the artifact showing the loop added to the method in order to allow the user to select from any of the queries. This previously could only be done by ending the connection and uncommenting the query to be used then restarting the connection.

```python
def main():
  #Program loops to allow user to use either of the queries until 'q' is entered 
  # to quit the program
  userInput = ""
  while userInput != "q":
    userInput = raw_input(
      "Enter 'h' for 50-Day Average Query, 'i' for Industry Query, 's' for Sector Query, or 'q' to quit: "
    )
```
## Enhancement Two: Algorithms and Data Structure
The section being looked at for the algorithms and data structure section of my ePortfolio was mainly making the main method more efficient and expanding the find by average method. The improvements made were adding type checking to the user inputs for the high and low values to search by as well as swapping the high and low values when necessary.

### Reflection

 When creating the original project the goal was to query the MongoDB database for the goals specified by the assignment. When improving it, I learned about how it is tricky to determine the typing of a variable in python. The best way to determine that is to try and convert to a float and if it failed, that showed it was not the correct type (string or double). The challenges were also shown in what I learned, where I had to determine the different types of variables in python. I had to try a few different methods before I was able to effectively determine if the input was a float. 
 
This snippet shows the enhancements to the main method to type check the high and low values
```python
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
```

This snippet shows the find_Moving_Avg function and the swapping of the high and low values if necessary
```python
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
```
## Enhancement Three: Databases
The goal for the changes in the section was to make the results easier to interpret, even when no results can be found. This, in the end, makes the program a little more user friendly. In determining how to check if there were no results I learned that python arrays have an inherent boolean property that allows you to check if it is false to determine if it is empty

### Reflection

When creating the original project, the goal was to query the MongoDB database for the goals laid out by the assignment. When focusing on database improvements, I learned how arrays in Python have built in boolean properties that allow you to see if the array is empty by checking if it is not true. The challenges with this section came from that property. Before, I wasn’t sure how to determine if the arrays were empty. After a little research I came to the realization stated above, and the rest of the modifications were simple enough from there. 

```python
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
```
