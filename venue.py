from config import db_connection,db_cursor
class Venue:

    def __init__(self,title,city) -> None:
        self.title=title
        self.city=city

    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS venues (id INTEGER PRIMARY KEY,title TEXT,city TEXT)
            """
        db_cursor.execute(sql)
        db_connection.commit()

    @classmethod
    def drop_table(cls):
        sql="""
            DROP TABLE IF EXISTS venues;
            """
        db_cursor.execute(sql)
        db_connection.commit()