import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///example.db')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("age", sqlalchemy.Integer)
)

metadata.create_all(engine)
ins = users.insert().values(name="Alice", age=30)
connection.execute(ins)
upd = users.update().where(users.c.name == "Alice").values(age=31)
connection.execute(upd)
sel = users.select()
result = connection.execute(sel)
for row in result:
    print(row)

connection.close()