import cgi
import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

head = """  <head>
            <title>Test - Registration Confirmation</title>
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

form = cgi.FieldStorage()
firstname = form.getvalue("firstname")
lastname = form.getvalue("lastname")
email = form.getvalue("email")
gender = form.getvalue("gender")

cursor.execute("SELECT * FROM user WHERE email='{}'".format(email))
results = cursor.fetchone()
if results is None:
    cursor.execute(
        "INSERT INTO user VALUES('{}', '{}', '{}', '{}')".format(
            firstname, lastname, email, gender
        )
    )
    connection.commit()

cursor.execute("SELECT * FROM user WHERE email='{}'".format(email))
results = cursor.fetchone()

print("Status: 200 OK")
print("Content-Type:text/html")
print()
print("<html>")
print(head)
print("<body>")
print("<p>Registration confirmed.<br></p>")
print("<p>")
print(
    "{} {}<br>{}<br>Gender: {}".format(results[0], results[1], results[2], results[3])
)
print("</p>")
print(footer)
print("</body>")
print("</html>")

connection.close()
