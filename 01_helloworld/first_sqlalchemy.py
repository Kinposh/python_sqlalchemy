import sqlalchemy


engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:kinposh@8.136.221.2/study')
conn = engine.connect()

query = sqlalchemy.text('SELECT * FROM students')

result_set = conn.execute(query)

for row in result_set:
    print(row)

conn.close()

engine.dispose()
