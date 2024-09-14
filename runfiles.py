from config import db_connection,db_cursor
from venue import Venue
from concert import Concert
from band import Band

def run():
    Band.drop_table()
    Band.create_table()
    Venue.drop_table()
    Venue.create_table()
    Concert.drop_table()
    Concert.create_table()
    
    band1=Band.create("kimana","Thika")
    band2=Band.create("Karainga","Kangema")
    venue1=Venue.create("City Hall","Nairobi")
    venue2=Venue.create("Aboretum","Thika")
    concert1=Concert.create("2020",band1,venue2)
    concert2=Concert.create("2021",band2,venue1)
    concert3=Concert.create("2021",band2,venue1)
    concert4=Concert.create("2020",band2,venue2)
    band1.play_in_venue("Aboretum","2025") #
    print(venue2.most_frequent_band())    
  
run()
