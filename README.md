# CS-340
MongoDB

About the Project/Project Title
This project utilizes the data structure of MongoDB to manipulate data using Python. The Python code allows a user to access the specific database in MongoDB instantly to create and read instances of animals that Austin Animal Center has in their custody.

This information is then imported to a web page for the company Grazioso Salvare. This page is designed so that a user can filter through the options to find rescue dog candidates. 

Motivation
This project was initially created for the Austin Animal Center to allow employees to better keep track of their animals. Hopefully, this will allow them to spend less time on data analysis and more time on taking care of their animals. 

Later is was developed to allow rescue animal companies to find animals that fit their criteria. This would allow for dog who had no home to be trained as rescue animals.

Getting Started
This project is based on Linux OS. To run this project, you will need Jupyter Notebook running with Python 3.  Create a database in MongoDB as well as a user.  The __init__ fields should be update accordingly.

Installation

You will need to upload the appropriate .csv file, in this case it’s the aac_shelter_outcomes.csv. This will need to be done as a mongo import in the terminal.
 
You will then need to create a admin profile to allow for limited access to the proper table in MongoDB.
 
For the test field you will need to install pip by using the following code:

pip install import-ipynb

Usage

Code Example
When using this application a call to crud method is called, after which a dictionary needs to be created with all the aspects of the animal desired. Once completed the system will upload the dictionary with the following commands:

 crud.create(DICTIONARY) function.

 You can call it back to read to you with:

crud.read(DICTIONARY) command. 

Once created, if a specific entry needs to be updated you will set the variable ‘query’ equal to whatever the id is as well as sett ‘update_vals’ equal to whatever you want changed.

query = {‘animal_id’: ‘A000001’}
update_vals = {‘color’: ‘Red’}
crud.update(query, update_vals)

When deleting an entry you establish which is your query that will be deleted and call the delete crud method. 

query = {‘animal_id’: ‘A000001’}
crud.delete(query)



Tests
	To test whether the system worked correctly, I started by making sure that the CRUD methods worked with additional information. 



Analysis

MongoDB offers a database in which large quantities of information can be stored and recalled. The system I built was to capitalize on the database’s information and recall them in a way that users could easily understand. Below the systems output is a map next to a pie graph showing the overall percentage of dog breeds per filter.

Completing this project required me to build the system in small increments like the database in MongoDB then build a CRUD methos in python, then implement the system’s call back. The challenges were connecting the databases to the code in the correct manner. I also had some difficulties figuring out how to correctly apply the filtering options. To overcome these issues, I used forums like Stack overflow.



Contact
Cory Graham:
Cory.graham@snhu.edu

