# Purpose 

Aim of this challenge is threefold:

1. Evaluate your coding abilities
2. Test you analytical skills (understanding the problem and solving it accordingly)
3. Judge your technical experience and/or learning curve

# Instructions 

This coding exercise should be performed in python. 
You are free to use the internet and any other libraries. 
Please save your work in a zip file and email it to us for review. Do not push your work to a public git repository! 

# Objective

Develop a monitoring software for a vessel's ballasting system.

## The situation

The ballasting system on Marine vessels consist of tanks, pumps, valves, pipes and sea inlets (seachest) and sea outlets (overboard). 
Water is pumped from the sea to the tanks to control the vessel's heel, trim and draught and to account for tidal changes. 
A marine engineer created a settings file (*vessel.yml*) that contains all the tanks, pumps, pipes and seas together 
with a list of the valves each piece of equipment is connected to.

Your task is to build the vessel model from the settings file using at least one of the creational design patterns.
Furthermore, you should write a module to identify which equipment is connected to which equipment when certain 
valves are open and other valves are closed. Create a few scenarios with different valve settings to 
showcase the functionality of your module.

## Take the following things into account:
* Use Poetry as package manager
* Implement Pydantic's BaseModel for data validation
* Enhance readability by exploiting type hinting
* Follow the PEP8 coding guidelines
* Write usefull and clear comments
* Use clear function and variable names
* Design your solution for modularity
* Write unit tests for all functions
* Exploiting design patterns is a bonus

We recommend using PyCharm as an IDE

# Getting started
* Install latest python version (3.11)
* Install Poetry: `pip3.11 install poetry` or `python3.11 -m pip install poetry`
* Run: `poetry install` inside this project folder to install all dependencies
* You can add new packages to the project via: `poetry add [PACKAGE_NAME]`
* Execute programs using `poetry run ...`
  * For example: 
    * `poetry run python main.py`
    * `poetry run pytest .`
    * `poetry run mypy .`
* Testing and formatting scripts can be found in the **scripts** folder

# Bonus question
Extra points can be obtained when the Visitor design pattern is used in the module to calculate the connections 
between the pieces of equipment.

## Good luck!
