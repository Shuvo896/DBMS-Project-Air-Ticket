# ✈️ Air Ticket Management System

A web-based **Air Ticket Management System** built using **Django** and **MySQL**.  
This project is developed as part of a DBMS course project. It allows users to manage flights, tickets, and bookings with a simple and user-friendly interface.

---

## 🚀 Getting Started

Follow the steps below to set up and run the project on your local machine.

# 1. Clone the Repository
Open **Git Bash** in your desired folder and run:
```
git clone https://github.com/Shuvo896/DBMS-Project-Air-Ticket
```
# 2.Open a new terminal and navigate to the Project Directory

```
cd DBMS-Project-Air-Ticket
```
# 3. Set Up the Virtual Environment
Open a new CMD or restart your IDE, then run (make sure you are at directory DBMS-Project-Air-Ticket):
```
pipenv shell
pipenv install
```
# 4. Set Up the Database
Start MySQL from XAMPP

Open the MySQL console and create the database:
```
CREATE DATABASE bookinfly_db_test;
```
# 5. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```
# 6. Run the Development Server
```
python manage.py runserver
```
Now, open your browser and go to 👉 http://127.0.0.1:8000/

📂 Tech Stack
Backend: Django (Python)

Database: MySQL

Frontend: HTML, CSS, Bootstrap

Tools: XAMPP, Pipenv

💡 Features
User authentication (Signup/Login)

Flight and ticket management

Booking system with price management

Database-driven architecture

