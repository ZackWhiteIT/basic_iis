import cgi
import sqlite3
import os

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

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

cursor.execute("SELECT * FROM user")
results = cursor.fetchall()

print("Status: 200 OK")
print("Content-Type:text/html")
print()
print("<html>")
print(head)
print("<body>")
print("<table name=users caption='All Users' style='width=100%'>")
print("<tr>")
print("<th>First Name</th>")
print("<th>Last Name</th>")
print("<th>Email</th>")
print("<th>Gender</th>")
print("</tr>")
for row in results:
    print("<tr>")
    for item in row:
        print("<td>{}</td>".format(item))
    print("</tr>")
print("</table>")
print(footer)
print("</body>")
print("</html>")

connection.close()
