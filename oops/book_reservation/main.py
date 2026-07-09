"""
===========================================================
File Name : main.py

THEORY

main.py is called the Driver Program.

It is responsible for

1. Creating Objects

2. Calling Methods

3. Taking User Input

4. Running the Program

The business logic remains inside the classes.

This follows the OOP principle of Separation of Concerns.

===========================================================
"""

from movie import MovieReservation


movie = MovieReservation("Avengers Endgame", 10)

while True:

    print("\n========== MOVIE RESERVATION ==========")
    print("1. Show Available Seats")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Show Bookings")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        movie.show_available_seats()

    elif choice == "2":

        name = input("Customer Name : ")

        seat = int(input("Seat Number : "))

        movie.book_ticket(name, seat)

    elif choice == "3":

        booking_id = input("Booking ID : ")

        movie.cancel_ticket(booking_id)

    elif choice == "4":

        movie.show_bookings()

    elif choice == "5":

        print("Thank You")
        break

    else:

        print("Invalid Choice")