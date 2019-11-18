import cgi
import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

head = """  <head>
            <title>Test - My Account</title>
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
email = form.getvalue("email")

cursor.execute("SELECT * FROM user WHERE email='{}'".format(email))
results = cursor.fetchone()

print("Status: 200 OK")
print("Content-Type:text/html")
print()
print("<html>")
print(head)
print("<body>")
if results is None:
    print("<p>Login for {} failed!</p>".format(email))
else:
    print("<h3>Account Details</h3>")
    print("<p>Hello, {}!<br></p>".format(results[0]))
    print("<p>")
    print(
        "{} {}<br>{}<br>Gender: {}".format(
            results[0], results[1], results[2], results[3]
        )
    )
    print("</p>")
print(footer)
print("</body>")
print("</html>")

connection.close()
