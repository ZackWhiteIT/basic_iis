import cgi
import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE user (firstname, lastname, email, gender)")
cursor.execute("INSERT INTO user VALUES ('John', 'Smith', 'jsmith@email.com', 'male')")
connection.commit()
connection.close()

head = """  <head>
            <title>Test - Admin</title>
            <meta name="viewport" conent="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" type="text/css" href="style.css">
            <ul class="breadcrumb">
                <li><a href="index.html">Home</a></li>
                <li><a href="register.html">Register</a></li>
                <li><a href="account.html">My Account</a></li>
                <li><a href="admin.html">Admin</a></li>
            </ul>
            </head>"""

footer = """<div class="footer">
                <p>&copy; 2019 Zack White. All rights reserved.</p>
            </div>"""

print("Status: 200 OK")
print("Content-Type:text/html")
print()
print("<html>")
print(head)
print("<body>")
print("<p>Database created successfully.</p>")
print(footer)
print("</body>")
print("</html>")

connection.close()
