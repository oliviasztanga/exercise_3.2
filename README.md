# the \<wit\> project workshop: "databases & sql-alchemy"


_Anytime you see a 🖥, follow the instructions below. Anytime you see a 💡, click the toggles to find more information._
<br><br>


### 🖥 Install this project locally
1. Clone this repo: `git clone <this repo's remote url>`
2. Change directories: `cd workshop_databases_sqlalchemy`
3. Create a virtual environment for this project and activate it:
```
mkdir env
python3 -m venv env
source env/bin/activate
```
4. Install the requirements: `pip install -r requirements.txt`
5. Run the application as needed: `python app.py`
<br>





# Databases

<details><summary>💡 What is a database?</summary>
<hr>

### Databases
A database is a collection of information typically stored on a computer system. Furthermore, this information is structured, meaning that its order and constraints are specifically defined, in order to make this information queryable. There are many types of databases, but we will be focusing on relational databases for now.

### Relational Databases
Relational databases are one of the most common types of databases in operation today. A relational database utilizes tables to structure information. Within a table, columns represent fields or properties we want to store about a type of a data and rows represent entries or instances about a piece of that data type.

For example, if we were to create a relational database to manage data for a school system, we might create a `Student` table with columns for `Name` and `Grade`. Then we can store information about a student named Laura Jean as a row like this:

**Students Table:**
| Name  | Grade |
| ------------- | ------------- |
| Laura Jean  | 10  |

### Structured Query Language (SQL)
Structured Query Language is the standard programming language used by relational database systems to define, manipulate, and query data. We will not be teaching SQL in depth but if you are interested in learning more, you can follow tutorials on [SQL Zoo](https://sqlzoo.net/).

<hr>
</details><br>


<details><summary>💡 What is Postgres?</summary>
<hr>

### Postgres
As software engineers, we don't want to reinvent the wheel. The wheel in this case is software that creates and manages a relational database on a computer system. There are many relational database management systems that already exist and many of those are open source! The one that we have chosen for this workshop is PostgreSQL. PostgreSQL is "a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads." If you are interested, you can read more about Postgres [here](https://www.postgresql.org/about/).

### Postgres is Server-Based
Postgres is particularly useful because it is server-based, meaning that it operates a server that is run either locally on your computer or optionally on a cloud. You can then write applications that connect to a Postgres instance by connecting to a Postgres server via an IP address and port number.

<hr>
</details><br>

### 🖥 Create a new database in your Postgres cluster
We want to create a database named `todo`. There are several ways to create a new database:
1. When you installed Postgres, you also installed some command line tools, like `psql`. If you run `psql`, you will enter an interactive terminal for Postgres. There are more docs about how to use this interactive terminal [here](https://www.postgresql.org/docs/9.2/app-psql.html) but something you should know is that you can run SQL commands within this interactive terminal. The SQL command for creating a new database is `CREATE DATABASE <database name>;`.
2. Another command line utility you installed with Postgres was `createdb`. You can find more docs on this command [here](https://www.postgresql.org/docs/9.1/app-createdb.html). To create a new database using this utility, you can run `createdb <database name>` in your **main** terminal.
3. You can create a datbase in a GUI, like Postico or pgAdmin.

Pick one of these methods and create a database named `todo`.
<br>





# Object Relational Mappers

<details><summary>💡 What is an Object Relational Mapper?</summary>
<hr>

### Object Relational Mappers (ORM)
An object relational mapper is a program that automates the transfer of data between a relational database and a programming language by utilizing object oriented design to represent database tables and the relationships between them. This is useful to us as developers because it allows us to work with our database in a language we are more comfortable with. On the other hand, well-written SQL queries are likely more performant than queries written with an ORM.
<hr>
</details><br>


<details><summary>💡 What is SQL-Alchemy?</summary>
<hr>

### SQL-Alchemy
SQL-Alchemy is on ORM that we can use with Python.

### How to Use SQL-Alchemy with Postgres
We can use SQL-Alchemy with Postgres by providing SQL-Alchemy's `engine` with a URI to our Postgres instance. You can think of the `engine` as a black box: you don't need to understand how it works under the hood -- you just need to know that it is what powers the communication process between our Python code and the Postgres database. We also need to use a driver called `psycopg2` to facilitate this communcication. This was already installed locally so we just need to append it to our database URI using the following format: `postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>`.

<hr>
</details><br>

### 🖥 Connect your SQL-Alchemy app to your Postgres database
In `app.py`, connect SQL-Alchemy to your Postgres database by defining the `DATABASE_URI`. Since we are running our Postgres servers locally, the `IP_ADDRESS` is `localhost`. Also, if you installed Postgres using Postgres app (Mac OS users), you probably don't have a username and password so you can skip that part.

<details><summary>Click here for the solution.</summary>
<hr>
  
```py
DATABASE_URI = "postgres+psycopg2://localhost:5432/todo"

# OR

DATABASE_URI = "postgres+psycopg2://postgres:postgres@localhost:5432/todo"
```

<hr>
</details>
<br>



# Defining Models in SQL-Alchemy

<details><summary>💡 How do we define models in SQL-Alchemy?</summary>
<hr>

### Declarative Base
In SQL-Alchemy, we define models by creating classes. Furthermore, the models we define need to branch off of a declarative base in order to register our models with SQL-Alchemy. In `models.py`, you can see that we import the factory function `declarative_base` and then invoke it to create the `Base` class that we extend to create our model classes. Think about this in object-oriented design: our models will inherit all of the functionality from `Base`, which in this case is functionality specific to SQL-Alchemy, and `Base` will likely have some knowledge of the classes that extend it.

Additionally, every model we define as a class will receive an attribute `__tablename__` with a name for that table.


### Column Types
In Postgres, columns are restricted to a specific data type. As a result, we need to define the datatypes for columns in our SQL-Alchemy app as well. To do so, we we use the `Column` object which we have already imported in `models.py`. The `Column` object takes a data type as its first argument and uses it to define the data type for that column. Additionally, every model we define as a class will have a column for the primary key.

For example, if we were creating a table for students in a school system:

```py
class Student(Base):
  __tablename__ = 'students'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  grade = Column(Integer)
```

You can find more docs on defining columns [here](https://docs.sqlalchemy.org/en/13/core/type_basics.html).

### Constraints
Besides the data type, you may want to further constrain a column. To define further constraints, you can provide additional arguments to the `Column`.

For example, students should always have a name and therefore the `Name` column should never be empty. To prevent `null` entries for the `Name` column, we can pass a `nullable` argument to `Column`:

```py
class Student(Base):
  __tablename__ = 'students'
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  grade = Column(Integer)
```

You can find more docs on constraining columns [here](https://docs.sqlalchemy.org/en/13/core/constraints.html).

<hr>
</details><br>

### 🖥 Define models for Person, Task, and Project
In `models.py`, add the following properties to the `Person`, `Task`, and `Project` tables:

**Person**<br>
Id: `Integer, Primary Key`<br>
Name: `String, Required`<br>

**Task**<br>
Id: `Integer, Primary Key`<br>
Name: `String, Required`<br>
Description: `String`<br>
Due Date: `Date`<br>

**Project**<br>
Id: `Integer, Primary Key`<br>
Name: `String, Required`<br>
<br>

<details><summary>Click here for the solution.</summary>
<hr>
  
```py
class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    due_date = Column(Date)
    
class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

```

<hr>
</details>
<br>

<details><summary>💡 How do we define relationships in SQL-Alchemy?</summary>
<hr>
We define relationships using very specific patterns that SQL-Alchemy outlines in great detail [here](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html). For this workshop, let's focus on how to define a one-to-many relationship.
  
In a one-to-many relationship, one class will get a foreign key attribute referencing the primary key of another table and a `relationship` attribute referencing the other class. The other table will just get a `relationship` attribute referencing the first class. Each `relationship` attribute also receives a `back_populates` argument referencing the other class's relationship attribute to ensure this relationship is bidirectional (that updates to one table will be reflected in updates to the other table). That's a mouthful, but here is an example:

```py
class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    tasks = relationship("Task", back_populates="person")
    
    
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    due_date = Column(Date)
    
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship("Person", back_populates="tasks")

```

<hr>
</details><br><br>

### 🖥 Define relationships between your models
In `models.py`, create the following relationships:

- Users and Tasks should have a one-to-many relationship.
- Tasks and Projects should have a one-to-many relationship.

<details><summary>Click here for the solution.</summary>
<hr>
  
```py
class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    tasks = relationship("Task", back_populates="person")
 
 
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    due_date = Column(Date)
    
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship("Person", back_populates="tasks")
    
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship("Project", back_populates="tasks")
  
  
class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    tasks = relationship("Task", back_populates="project")

```

<hr>
</details>
<br>
<br>


### 🖥 Create your tables
You can now run `python app.py` in your terminal. This will run the `refresh_database` function, which uses built in SQL-Alchemy methods to drop all tables and then create all tables. Once this is run, you should be able to see the database tables and columns either using `psql` or your chosen GUI (Postico or pgAdmin).
<br>





# Creating Entries in SQL-Alchemy

<details><summary>💡 How do we create entries in SQL-Alchemy?</summary>
<hr>

### Sessionmaker and Sessions
Technically, we can create models and entries by using methods on the `engine` directly. However, it's better to use sessions because they allow us to group and rollback transactions in case there is an error. Once you have completed your desired set of transactions, you can use the `commit` method off of a session to commit your transactions permanently to your database.

Sessions are created by invoking the `sessionmaker` module, which is already imported and binded to the engine in `app.py`.  The `seed` function in `seed.py` receives a created session when it is invoked in `app.py`.

### Instances
Our models are defined as classes. That means we can create entries in our model by creating instances of those classes. Once it has been created, we `add` it to our session and finally we `commit` our session. See the following example:

```py
person_instance = Person(name="Laura Jean")
session.add(person_instance)
session.commit()
```

We can add multiple instances at one using the `add_all` method.

```py
persons = [ Person(name="Laura Jean"), Person(name="Bilbo Baggins") ]
session.add_all(persons)
session.commit()
```
<hr>
</details><br>

### 🖥 Create entries for each of your models
Go ahead and have some fun creating entries for your databse! When you are ready to seed your database, comment out the `refresh_database` function and uncomment the `seed` function in `app.py`. Then run `python app.py` to seed your tables. You should be able to see the database tables and columns either using `psql` or your chosen GUI (Postico or pgAdmin).
<br>





# That's it! You did it! Great job! 👏
