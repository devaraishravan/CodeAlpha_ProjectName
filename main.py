import mysql.connector
from rapidfuzz import fuzz

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="shravan",
    database="redundancy_db"
)

cursor = db.cursor()

name = input("Enter Name: ")
email = input("Enter Email: ")
phone = input("Enter Phone: ")

# Check duplicate email or phone
cursor.execute(
    "SELECT * FROM users WHERE email=%s OR phone=%s",
    (email, phone)
)

duplicate = cursor.fetchall()

if duplicate:
    print("Redundant Data Found")

else:
    cursor.execute("SELECT name FROM users")
    names = cursor.fetchall()

    false_positive = False

    for row in names:
        existing_name = row[0]

        similarity = fuzz.ratio(
            name.lower(),
            existing_name.lower()
        )

        if similarity >= 80:
            false_positive = True
            print("False Positive Detected")
            print("Similar Name Found:", existing_name)
            break

    if not false_positive:
        cursor.execute(
            "INSERT INTO users(name,email,phone) VALUES(%s,%s,%s)",
            (name,email,phone)
        )

        db.commit()
        print("Unique Data Inserted")