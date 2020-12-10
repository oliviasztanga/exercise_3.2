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
Relational Databases are one of the most common types of databases in operation today. A relational database utilizes tables to structure information. Within a table, columns represent fields or properties we want to store about a type of a data and rows represent entries or instances about a piece of that data type.

For example, if we were to create a relational database to manage data for a school system, we might create a `Student` table with columns for `Name` and `Grade`. Then we can store information about a student named Laura Jean in 10th Grade as a row like this:

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
As software engineers, we don't want to reinvent the wheel. The wheel in this case is software that creates and manages a relational database on a computer system. There are many relational database management systems that already exist and many of them are open source! The one that we have chosen for this workshop is PostgreSQL. PostgreSQL is "a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads." If you are interested, you can read more about Postgres [here](https://www.postgresql.org/about/).

### Postgres is Server-Based
Postgres is particularly useful because it is server-based, meaning that it operates a server that is run either locally on your computer or optionally on a cloud. You can then write applications that connect to a Postgres instance by connecting to a Postgres server via an IP address and port number.

<hr>
</details><br>

### 🖥 Create a new database in your Postgres cluster
We want to create a database named `todo`. There are several ways to create a new database:
1. When you installed Postgres, you probably also installed some command line tools, like `psql`. If you run `psql`, you will enter an interactive terminal for Postgres. There are more docs about how to use this interactive terminal [here](https://www.postgresql.org/docs/9.2/app-psql.html) but something you should know is that you can run SQL commands within this interactive terminal. The SQL command for creating a new database is `CREATE DATABASE <database name>`.
2. Another command line utility you installed with Postgres was `createdb`. You can find more docs on this command [here](https://www.postgresql.org/docs/9.1/app-createdb.html). To create a new database using this utility, you can run `createdb <database name>` in your **main** terminal.
3. You can create a datbase in a GUI, like Postico or pgAdmin.
<br>





# Object Relational Mappers

<details><summary>💡 What is an Object Relational Mapper?</summary>
<hr>

### Object Relational Mappers (ORM)

### Pros

### Cons

<hr>
</details><br>


<details><summary>💡 What is SQL-Alchemy?</summary>
<hr>

### SQL-Alchemy

### How to Use SQL-Alchemy with Postgres

<hr>
</details><br>

### 🖥 Connect your SQL-Alchemy app to your Postgres database
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
