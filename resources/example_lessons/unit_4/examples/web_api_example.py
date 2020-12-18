# API = Application Programming Interface

# the requests module can be installed by running the following command in the terminal
# pip install requests
import requests

# request the first todo item
url = 'https://jsonplaceholder.typicode.com/todos/1'

# ping the url for data, save data in response variable
response = requests.get(url)

# save response as dictionary (JSON = JavaScript Object Notation)
to_do = response.json()

display = f"""
Created by: {to_do['userId']}
Todo #{to_do['id']} - {to_do['title']}
Completed: {to_do['completed']}
"""

# print(display)

# -------------------------------------- #

# Then ping /todos for a list of todos and loop 
# loop through first 10 todos and display data for each
for index in range(10):
    # grab the todo dictionary at the current index
    todo = todos[index]
​
    # print(todo)
​
    print(f'''
    {todo['id']}. {todo['title']}
    Created by: {todo['userId']}
    Completed: {todo['completed']}
    ''')
