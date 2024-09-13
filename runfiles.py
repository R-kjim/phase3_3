from config import db_connection,db_cursor
from venue import Venue
from concert import Concert
from band import Band

def run():
    Band.drop_table()
    Band.create_table()
    Venue.drop_table()
    Venue.create_table()
    

run()
