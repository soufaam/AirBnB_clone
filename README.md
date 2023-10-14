# AirBnB Clone - The Console

This is a command-line application for managing AirBnB objects.
The main purpose of this project is to build a command interpreter
that can create, retrieve, update, and delete objects in the AirBnB clone.

## Description

The AirBnB Clone project is a team project that involves
building a Python-based application for managing AirBnB-like
objects. The project is split into several tasks, with each
task focusing on a specific aspect of the application's development.

## Command Interpreter

The command interpreter is a command-line interface (CLI)
that allows users to interact with the AirBnB clone application.
It provides a set of commands for performing various actions on
objects within the application.

# Tasks

## Task 0: README, AUTHORS (mandatory)

- Write a `README.md`:
  - Description of the project.
  - Description of the command interpreter.
  - How to start it.
  - How to use it.
  - Examples.

- Create an `AUTHORS` file at the root of your repository,
listing all individuals having contributed content to the
repository. Follow the format of Docker's AUTHORS page.

- Use branches and pull requests on GitHub for better
team organization.

## Task 1: Be pycodestyle compliant! (mandatory)

- Write beautiful code that passes the pycodestyle checks.

## Task 2: Unittests (mandatory)

- Ensure all your files, classes, and functions are
tested with unit tests.

- Note that the number of tests you create can be
different from the example provided.

- Unit tests must also pass in non-interactive mode.

## Task 3: BaseModel (mandatory)

- Write a class `BaseModel` that defines all common
attributes/methods for other classes:
  - `id`: string, assign with a UUID when an instance is created.
  - `created_at`: datetime, assign with the current
  datetime when an instance is created.
  - `updated_at`: datetime, assign with the current
  datetime when an instance is created and updated
  every time you change your object.
  - `__str__`: should print `[<class name>]
  (<self.id>) <self.__dict__>`.
  
- Implement public instance methods `save(self)
 and `to_dict(self)`.

## Task 4: Create BaseModel from dictionary (mandatory)

- Update `BaseModel` to be created from a dictionary representation.

## Task 5: Store first object (mandatory)

- Implement saving `BaseModel` instances to a JSON file.

## Task 6: Console 0.0.1 (mandatory)

- Write a program called `console.py` that contains the
entry point of the command interpreter.

- Use the `cmd` module.

- Implement commands: `quit`, `EOF`, `help`,
and a custom prompt `(hbnb)`.

## Task 7: Console 0.1 (mandatory)

- Update `console.py` to include commands:
`create`, `show`, `destroy`, `all`, and `update`.

  - `create`: Creates a new instance of `BaseModel`,
  saves it to the JSON file, and prints the ID.
  
  - `show`: Prints the string representation of an
  instance based on the class name and ID.
  
  - `destroy`: Deletes an instance based on the class name and ID.
  
  - `all`: Prints all string representations of instances.
  
  - `update`: Updates an instance based on the class
  name and ID by adding or updating an attribute.

  Follow the specified error handling rules.
