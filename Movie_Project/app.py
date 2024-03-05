import psycopg2

url = "postgres://gdebcbmi:esLXBF9L1qHAhLDJhAqGohIGMen1SKEb@bubble.db.elephantsql.com/gdebcbmi"
connection = psycopg2.connect(url)
cursor = connection.cursor()

cursor.execute("SELECT * FROM users;")
first_user = cursor.fetchone()

print(first_user)

connection.close()