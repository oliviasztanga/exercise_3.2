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

### Column Types

### Constraints

<hr>
</details><br>

### 🖥 Define models for Person, Task, and Project
<br>

<details><summary>💡 How do we define relationships in SQL-Alchemy?</summary>
<hr>

### One-to-One

### One-to-Many

### Many-to-Many

<hr>
</details><br>

### 🖥 Define relationships between your models
<br>
<br>


### 🖥 Create your tables
<br>
<br>





# Creating Entries in SQL-Alchemy

<details><summary>💡 How do we create entries in SQL-Alchemy?</summary>
<hr>

### Sessionmaker and Sessions

### Instances

<hr>
</details><br>

### 🖥 Create entries for each of your models
<br>

### 🖥 Define relationships between your models
<br>
<br>





# That's it! You did it! Great job! 👏
