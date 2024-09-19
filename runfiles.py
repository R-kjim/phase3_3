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
    
    band1=Band.create("Downtown","Thika")
    band2=Band.create("All Stars","Msambweni")
    venue1=Venue.create("City Hall","Nairobi")
    venue2=Venue.create("Aboretum","Thika")
    concert1=Concert.create("2020",band1,venue2)
    concert2=Concert.create("2021",band2,venue1)
    concert3=Concert.create("2021",band2,venue1)
    concert4=Concert.create("2020",band2,venue2)
    band1.play_in_venue("Aboretum","2025") 
    
    ##Practical examples
    print("The band instance for a concert(concert1): ",concert1.band())
    print("The venue instance for a concert(concert1): ",concert1.venue())
    print("All concerts for a venue(venue2)", venue2.concerts())
    print("All bands that performed in a venue(venue2)",venue2.bands())
    print("Collections of all concerts by a band(band1)",band1.concerts())
    print("All venues a band has performed(band2)",band2.venues())
    print("Did the band in this concertperform in its hometown?(band1):",concert1.hometown_show())
    print("Bands introduction for a concert(concert2):", concert2.introduction())
    print("Creates a concert for a band given a date and venue:", band2.play_in_venue("City Hall","2024-10-01"))
    print("All introductions for a band(band2):\n", band2.all_introductions())
    print("Band with most performances:", Band.most_perfomances())
    print("First concert at a venue(venue2) on a given date:", venue2.concert_on("2020"))
    print("Band with most performances on a venue(venue1):", venue1.most_frequent_band())
   
run()
