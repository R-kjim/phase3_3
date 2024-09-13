from config import db_connection,db_cursor
class Band:
    all={}
    def __init__(self,name,hometown) -> None:
        self.name=name
        self.hometown=hometown

    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS bands(id INTEGER PRIMARY KEY,name TEXT,hometown TEXT)
            """
        db_cursor.execute(sql)
        db_connection.commit()

    @classmethod
    def drop_table(cls):
        sql="""
            DROP TABLE IF EXISTS bands;
            """
        db_cursor.execute(sql)
        db_connection.commit()

    def save(self):
        sql="""
            INSERT INTO bands (name,hometown) VALUES(?,?)
            """
        db_cursor.execute(sql,(self.name,self.hometown,self.id))
        db_connection.commit()

        self.id=db_cursor.lastrowid
        Band.all[self.id]=self