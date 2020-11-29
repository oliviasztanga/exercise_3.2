## Summary
You will be creating models and seed models for our zoo schema using SQLAlchemy.

## Installation
```
# in your postgres cluster, create a database named "zoo"
createdb zoo

# clone this repo
git clone <this repo's remote url>

# enter directory
cd demo_3.2

# create a virtual environment for this project & activate
virtualenv env
source env/bin/activate

# install the requirments
pip install -r requirements.txt

# run application
python app.py
```

## Instructions

**Table Definition**
In `models.py`, add the following properties to the `Task` and `User` tables:

Task
- Id: Integer, Primary Key
- Name: String, Required
- Description: String
- Priority: Integer
- Due Date: Date

User
- Id: Integer, Primary Key
- Name: String, Required

Optional: Project
- Id: Integer, Primary Key
- Name: String, Required

**Relationships**
In `models.py`, create the following relationships:

Users and Tasks should have a one-to-many relationship.
Optional: Projects and Tasks may have a one-to-many or many-to-many relationship.

**Seeding**
In `seed.py`, create at least five entries for every table and make sure to set relationships.

**Demoing**
- Make sure to show changes to the tables in Postico.
