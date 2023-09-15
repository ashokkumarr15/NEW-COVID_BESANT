COVID-19 MANAGEMENT

Source code :

import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="covid19_data"
)
cursor = db.cursor()

def insert_record(name, status):
    try:
        sql = "INSERT INTO covid19_records (name, status) VALUES (%s, %s)"
        values = (name, status)
        cursor.execute(sql, values)
        db.commit()
        print("Record inserted successfully.")
    except Exception as e:
        db.rollback()
        print("Error:", e)

def get_records_by_status(status):
    try:
        sql = "SELECT * FROM covid19_records WHERE status = %s"
        cursor.execute(sql, (status,))
        records = cursor.fetchall()
        print(f"List of {status} individuals:")
        for record in records:
            print(f"ID: {record[0]}, Name: {record[1]}")
    except Exception as e:
        print("Error:", e)

while True:
    print("\nOptions:")
    print("1. Insert a new record")
    print("2. View vaccinated individuals")
    print("3. View recovered individuals")
    print("4. View deceased individuals")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name: ")
        status = input("Enter the status (vaccinated/recovered/dead): ")
        insert_record(name, status)
    elif choice == "2":
        get_records_by_status("vaccinated")
    elif choice == "3":
        get_records_by_status("recovered")
    elif choice == "4":
        get_records_by_status("dead")
    elif choice == "5":
        break

# Close the database connection
db.close()x



	



