# AirBnB Clone ― An ALX Full-stack engineering program project

## Description of the project
The goal of the Airbnb_clone project is to deploy a replica of the [Airbnb Website](https://www.airbnb.com/) using a web-server. This version of this project have:
- A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)

## Files and Directories
- ```models``` directory contains all the classes used for the entire project.
- ```tests``` directory will contain all unit tests.
- ```console.py``` file is the entry point of our command interpreter.
- ```models/engine``` directory will contain all storage classes (responsible for serialization/deserialization of objects).

## Description of the command interpreter
| Commands  | Description |
| ------------- | ------------- |
| ```quit```  | Quits the console  |
| ```Ctrl+D``` or  ```EOF``` | Quits the console  |
| ```help``` or ```help <command>```  | Displays all commands or Displays instructions for a specific command
| ```create <class>```  | Creates an object of type ```<class>```, saves it to a JSON file, and prints the objects ID
| ```show <class> <ID>```  | Shows string representation of an object
| ```destroy <class> <ID>```  | Deletes an object
| ```all or all <class>```  | Prints all string representations of all stored objects or Prints a filtred string representations of a specific class type.
| ```update <class> <id> <attribute name> "<attribute value>"```  | Updates an object's attribute
| ```<class>.all()```  | Same as all ```<class>```
| ```<class>.count()```  | Prints the number of stored objects of a certain class
| ```<class>.show(<ID>)```  | Same as show ```<class> <ID>```
| ```<class>.destroy(<ID>)```  | Same as destroy ```<class> <ID>```
| ```<class>.update(<ID>, <attribute name>, <attribute value>```  | Same as update ```<class> <ID> <attribute name> <attribute value>```
| ```<class>.update(<ID>, <dictionary representation>)```  | Updates an objects based on a dictionary representation of attribute names and values

## Execution and usage
The shell works like this in interactive mode (to start it execute console.py file):
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
