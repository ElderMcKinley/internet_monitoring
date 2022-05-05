import mysql
from mysql import connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Database!",
    database="testdatabase"
)

mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("julie", datetime.now(), "F"))

#mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")

#mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)") change column name and type

# users = [("tim", "techwithtim"), ("jackson", "peepee"), ("brennan", "poopoo")]

# user_scores = [
#     (45, 100),
#     (30, 200),
#     (46, 124)
# ]

# Q1 = """CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"""

# Q2 = """CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"""

# #mycursor.execute(Q1)
# #mycursor.execute(Q2)

# Q3 = """INSERT INTO Users (name, passwd) VALUES (%s, %s)"""
# Q4 = """INSERT INTO Scores (userId, game1, game2) VALUES (%s, %s, %s)"""

# for x, user in enumerate(users):
#     mycursor.execute(Q3, user)
#     last_id = mycursor.lastrowid
#     mycursor.execute(Q4, (last_id,) + user_scores[x])

# db.commit()

# mycursor.execute("SELECT * FROM Scores")
# for x in mycursor:
#     print(x)