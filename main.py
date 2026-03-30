SOURCE CODE: 

import mysql.connector as mys
mycon = mys.connect( host="localhost", user="root", password="srijita@123" )
cur = mycon.cursor()
cur.execute("create database if not exists moviebooking_db")
cur.execute("use moviebooking_db")
cur.execute(" create table if not exists movies(id INT PRIMARY KEY, name VARCHAR(50), timing VARCHAR(20), language VARCHAR(20), seats INT) ")
mycon.commit()
cur.execute("SELECT * FROM movies")

if cur.rowcount == 0:
    cur.execute("insert into movies (id,name,timing,language,seats) VALUES (1,'3 IDIOTS','4PM','Hindi',50)")
    cur.execute("INSERT INTO movies (id,name,timing,language,seats) VALUES (2,'ANABELLE','1AM','English',40)")
    cur.execute("INSERT INTO movies (id,name,timing,language,seats) VALUES (3,'KGF','6PM','Telugu',35)")
    mycon.commit()

def show_movies():
    print("\n--- LIST OF ALL THE MOVIES GIVEN BELOW---")
    cur.execute("SELECT * FROM movies")
    for i in cur.fetchall():
        print("ID:", i[0], " Name:", i[1], " Time:", i[2], "Language:", i[3], "Seats:", i[4])


def book_ticket():
    name = input("Enter your name")
    show_movies()
    movie_id = int(input("Enter movie ID: "))
    seats = int(input("Enter number of seats: "))

    cur.execute("SELECT seats,name FROM movies WHERE id=%s", (movie_id,))
    data = cur.fetchone()

    if data is None:
        print("Invalid movie ID")
        return

    totalseats = data[0]
    chosenmovie = data[1]

    if seats > totalseats:
        print(" Sorry! Not enough seats available!")
        return

    # update seats
    cur.execute("update movies set seats = seats - %s where id=%s", (seats, movie_id))

    # insert booking
    cur.execute("insert into bookings (user_name , movie_name , seats_booked) VALUES (%s,%s,%s)", (name, movie_name, seats))
    mycon.commit()
    print("\n Ticket booked !")
    movies_recommendation(movie_name):


def movies_recommendation(movie_name):
    print("\n Recommended Movies which is an implementation of AI ")
    cur.execute("select name from movies where name != %s", (movie_name,))
    for j in cur.fetchall():
        print("-", m[0])


def view_bookings():
    print("\n--- All Bookings to be viewed ---")
    cur.execute("select * from bookings")
    for i in cur.fetchall():
        print(i)


def search_movie():
    name = input("Enter movie name to search: ")
    cur.execute("select * from movies where name LIKE %s", ("%{}%".format(name),))
    results = cur.fetchall()

    if len(results)>0:
        for i in results:
            print(i)
    else:
        print("No movie found ")


def cancel_booking():
    user = input("Enter your name: ")
    cur.execute("select * from bookings where user_name = %s", (user,))
    data = cur.fetchall()

    if not data:
        print("No booking found")
        return

    for i in data:
        print(i)

    booking_id = int(input("Enter booking ID to cancel your booking : "))
    cur.execute("select movie_name, seats_booked from bookings where id=%s", (booking_id,))
    record = cur.fetchone()

    if record:
        movie_name, seats = record

        # return seats
        cur.execute("update movies set seats = seats + %s where name=%s", (seats, movie_name))

        # delete booking
        cur.execute("delete from bookings where id=%s", (booking_id,))

        mycon.commit()
        print("Booking cancelled")
    else:
        print("Invalid booking ID")


# ---------------- MAIN MENU ----------------

while True:
    print("\n----- MOVIE TICKET SYSTEM -----")
    print("1. View Movies")
    print("2. Book Ticket")
    print("3. View Bookings")
    print("4. Search Movie")
    print("5. Cancel Booking")
    print("0. Exit")

    c = int(input("Enter choice "))

    if c == 1:
        show_movies()

    elif c == 2:
        book_ticket()

    elif c == 3:
        view_bookings()

    elif c == 4:
        search_movie()

    elif c == 5:
        cancel_booking()

    elif c == 0:
        break

    else:
        print("Invalid choice")

mycon.close()
 
