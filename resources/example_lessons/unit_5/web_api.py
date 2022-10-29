# API - application programming interface

# requests module is used to make HTTP requests to websites
import requests, json



# ask user for their search term
joke = input('Enter a joke topic: ')

# url to access a list of dad jokes
url = 'https://icanhazdadjoke.com/search'
payload = {'term': joke}

# make an HTTP GET request to the url and save the HTTP response in a variable
response = requests.get(
    url, headers={'Accept': 'application/json'}, params=payload)

# JSON - JavaScript Object Notation (JS's version of a dictionary)
# convert the response data from JSON to Python dictionary
# using the .json() method of the response object

data = json.loads(response.text)

# display the data
# print(data['results'][0])
# print(data['results'][0]['joke'])


num_of_jokes = int(input('\nHow may jokes do you want to hear? '))
for x in range(num_of_jokes):
    if x < len(data['results']):
        print('\n' + data['results'][x]['joke'])
