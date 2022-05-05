from time import time
import speedtest
import subprocess
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"1 The error '{e}' occurred")
    
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"2 The error '{e}' occurred")

connection = create_connection("history.sqlite")

create_tests_table = """
CREATE TABLE IF NOT EXISTS tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isp TEXT NOT NULL,
    server TEXT,
    ping INTEGER,
    server_id INTEGER,
    download INTEGER,
    upload INTEGER,
    timestamp TEXT
);
"""
execute_query(connection, create_tests_table)

test = speedtest.Speedtest()

print("Loading server list...")
test.get_servers() # Get list of servers
print("Choosing best server...")
best = test.get_best_server() # Choose best server
print(f"Found: {best['host']} located in {best['country']}.")

# print("Performing download test...")
# download_result = test.download()
# print("Performing upload test...")
# upload_result = test.upload()
# ping_result = test.results.ping
# results = test.results.dict()
# client_results = results['client']
# server_info = results['server']
# server_id = server_info['id']
# timestamp = results['timestamp']
# # isp = client_results['isp']
# server_url = server_info['url']

print("Performing download test...")
download_result = 73
print("Performing upload test...")
upload_result = 10
ping_result = 22
results = test.results.dict()
# client_results = results['client']
# server_info = results['server']
server_id = 8008
timestamp = "05/05/2022"
isp = "Cox"
server_url = "google.com"



print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping: {ping_result} ms")
print(results)

# print("isp: " + str(type(isp)))
# print("server_url: " + server_url)
# print("ping_result: " + str(ping_result))
# print("server_id: " + server_id)
# print("download_result: " + str(download_result))
# print("upload_result: " + str(upload_result))
# print("timestamp: " + timestamp)

updateDatabase = f"""
INSERT INTO tests
VALUES ( {isp}, {server_url}, {ping_result}, {server_id}, {download_result / 1024 / 1024:.2f}, {upload_result / 1024 / 1024:.2f}, {timestamp} ); """

execute_query(connection, updateDatabase)