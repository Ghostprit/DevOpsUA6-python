import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///example.db')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
books = sqlalchemy.Table("books", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("author", sqlalchemy.String)
)

metadata.create_all(engine)

userInput = input("Which operation would you like to perform? (insert, select, update, delete): ").strip().lower()

if userInput == "insert":
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    ins = books.insert().values(title=title, author=author)
    connection.execute(ins)
elif userInput == "select":
    result = connection.execute(sqlalchemy.select(books))
    for row in result:
        print(row)
elif userInput == "update":
    book_id = int(input("Enter the book ID to update: "))
    new_title = input("Enter the new title: ")
    new_author = input("Enter the new author: ")
    update_stmt = books.update().where(books.c.id == book_id).values(title=new_title, author=new_author)
    connection.execute(update_stmt)
elif userInput == "delete":
    book_id = int(input("Enter the book ID to delete: "))
    delete_stmt = books.delete().where(books.c.id == book_id)
    connection.execute(delete_stmt)