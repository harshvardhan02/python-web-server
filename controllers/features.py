from rich import print

def get_features_name():
    return 'Features'

def get_fruits():
    mylist = ["apple", "banana", "cherry"]
    return mylist

def users():
    my_list_of_dicts = [
        {'name': 'John', 'age': 30},
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 35},
    ]
    print("Hello, [bold magenta]World[/bold magenta]!", ":star:", my_list_of_dicts)
    return my_list_of_dicts