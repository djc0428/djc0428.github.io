
## Code Review of Original Artifact
<video src="2 CS499 Milestone 1.mp4" width="600" height="500" controls preload></video>

## The Artifact
The artifact that I enhanced is the final project from CS340, specifically, part three of the final project. The program was originally created in June of 2020 as I finished up the Advanced Programming Concepts class. The artifact is a python module used to query a MongoDB database.

## Enhancement One: Software Design and Engineering
The section being looked at for the software design and engineering part of the portfolio showcases the use of multiple functions within the class, data structures, and common practices for software development. The improvements made were adding comments to make it more readable, made it more concise by removing unnecessary imports, and enhanced the usability by allowing the user to call any of the methods without changing the code and restarting the program. 
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
## Enhancement Three: Databases
