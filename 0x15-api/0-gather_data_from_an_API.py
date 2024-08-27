#!/usr/bin/python3

"""Returns info about a user todo list"""

from requests import get
from sys import argv


if __name__ == "__main__":
    responce = get('https://jsonplaceholder.typicode.com/todos/')
    data = responce.json()
    completed = 0
    total = 0
    tasks = []
    responce2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = responce2.json()

    for i in data2:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')
 
    for i in data:
        if i.get('userId') == int(argv[1]):
            total += 1

            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        employee, completed, total
    ))

    for i in tasks:
        print("\t {}".format(i))
        
