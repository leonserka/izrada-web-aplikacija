# 🌐 Web Application Development Labs (Python + XAMPP)

This repository contains a series of **laboratory exercises** for the course **Web Application Development**, focusing on building **dynamic web applications** using **Python, HTML, CSS, and MySQL** through the **XAMPP (Apache)** environment.

---

## 📘 Overview

These labs demonstrate how Python can be used as a **server-side scripting language (CGI)** for creating interactive web applications that communicate with a **MySQL database**.  
Each lab introduces new concepts, gradually progressing from static web pages to dynamic database-driven systems.

---

## 🧩 Topics Covered

- 🧱 **HTML & CSS Basics** – Structure and styling of web pages  
- 🐍 **Python CGI Scripting** – Form handling, GET/POST requests, and dynamic page generation  
- 💾 **MySQL Integration** – Connecting to a database, executing SQL queries, and managing data  
- 🔐 **Sessions and Cookies** – User session tracking and authentication management  
- 🧠 **CRUD Operations** – Creating, reading, updating, and deleting database records  
- 📄 **Dynamic Content Rendering** – Displaying database data via Python and HTML templates  
- ⚙️ **XAMPP Configuration** – Setting up Apache, MySQL, and Python for local web development  

---

## 🗂️ Example Project Structure

```
izrada-web-aplikacija/
├── lab1_html_intro/
│   ├── index.html             # Basic HTML structure
│   └── style.css              # Simple CSS styling
│
├── lab2_python_cgi/
│   ├── form.html              # HTML form to submit user data
│   └── process.py             # CGI script to handle form input
│
├── lab3_mysql_integration/
│   ├── connect.py             # Connect to MySQL and execute queries
│   ├── create_table.py        # Example for creating tables
│   └── show_data.py           # Display retrieved data dynamically
│
├── lab4_sessions/
│   ├── login.py               # Login form handling and session creation
│   ├── logout.py              # Ending session and cookie removal
│   └── profile.py             # Display user information via session
│
├── lab5_crud/
│   ├── insert.py              # Insert records into the database
│   ├── update.py              # Modify existing entries
│   ├── delete.py              # Delete records
│   └── view.py                # List and display all database entries
│
├── assets/
│   ├── style.css              # Shared styles
│   └── logo.png               # Optional images
│
└── README.md                  # This file
```

*(Folder names are illustrative — your actual structure may differ slightly.)*

---

## ⚙️ How to Run Locally

1️⃣ **Install and Configure XAMPP**
- Start **Apache** and **MySQL** from the XAMPP Control Panel.  
- Place this project folder inside your XAMPP `htdocs` directory:  
  `C:\xampp\htdocs\izrada-web-aplikacija`

2️⃣ **Set Up the Database**
- Open **phpMyAdmin** at: [http://localhost/phpmyadmin](http://localhost/phpmyadmin)  
- Create a new database (e.g. `web_lab`) and import `.sql` files if available.

3️⃣ **Access the Application**
- Visit: [http://localhost/izrada-web-aplikacija/](http://localhost/izrada-web-aplikacija/)  

4️⃣ **Run Python CGI Scripts**
- Make sure Python is installed and configured with Apache.  
- Ensure `.py` files in the `cgi-bin` directory are executable.  
- You can also run them manually via terminal for testing:
  ```bash
  python lab2_python_cgi/process.py
  ```

---

## 🧠 Learning Outcomes

By completing these labs, students will:  
- Understand how **web servers** and **CGI** interact  
- Learn to connect **Python** with **MySQL databases**  
- Implement **session management**, **cookies**, and **form handling**  
- Develop skills to build **interactive and data-driven web applications**  

---

## 🧰 Technologies Used

- 🐍 **Python (CGI)**  
- 🧱 **HTML5 / CSS3**  
- 💾 **MySQL (via XAMPP)**  
- ⚙️ **Apache Server**  
- 🖥️ **XAMPP Local Environment**  

---

## 🚧 Future Improvements

- Transition from CGI to **Flask or Django** for more advanced functionality  
- Add **JavaScript** and **AJAX** for dynamic content updates  
- Include user authentication and roles (Admin / User)  
- Expand CRUD functionality with additional validation and feedback  

---

## 📄 License

This project is open-source and available for educational use.  
You are free to use and modify it for learning purposes.

---

## ✍️ Author

**Leon Serka**  
[https://github.com/leonserka](https://github.com/leonserka)
