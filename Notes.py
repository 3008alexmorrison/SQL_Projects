'''
to connect to SQLite first: import sqlite3
then: connection = sqlite3.connect('data')
to use SQL queries use: connection.execute(query)
to close connection: connection.close()
you can open as many connections as you want sqlite connects to files not servers.
only 1 connection can write to the database at a time.
To commit changes: .commit() or with connection:
'''