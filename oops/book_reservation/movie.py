"""
===========================================================
File Name : movie.py

THEORY - ENCAPSULATION

Encapsulation means binding data and methods together
inside a class.

The class controls how the data is accessed.

Here,

Data
----
movie_name
total_seats
booked_seats

Methods
-------
book_ticket()
cancel_ticket()
show_available_seats()
show_bookings()

Everything is packed together inside MovieReservation class.

===========================================================
"""

from booking import Booking
from customer import Customer


class MovieReservation:

    def __init__(self, movie_name, total_seats):
        """
        Constructor

        Initializes movie details.
        """

        self.movie_name = movie_name
        self.total_seats = total_seats
        self.booked_seats = {}

    def show_available_seats(self):

        print("\nAvailable Seats")

        available = []

        for seat in range(1, self.total_seats + 1):

            if seat not in self.booked_seats:
                available.append(seat)

        print(available)

    def book_ticket(self, customer_name, seat_number):

        """
        Validation

        Prevent duplicate bookings.
        """

        if seat_number < 1 or seat_number > self.total_seats:
            print("Invalid Seat Number")
            return

        if seat_number in self.booked_seats:
            print("Seat Already Booked")
            return

        customer = Customer(customer_name)

        booking_id = Booking.generate_booking_id()

        self.booked_seats[seat_number] = {
            "Booking ID": booking_id,
            "Customer": customer.customer_name,
            "Seat": seat_number
        }

        print("\nBooking Successful")
        print("Booking ID :", booking_id)
        print("Customer :", customer.customer_name)
        print("Seat :", seat_number)

    def cancel_ticket(self, booking_id):

        for seat, details in list(self.booked_seats.items()):

            if details["Booking ID"] == booking_id:

                del self.booked_seats[seat]

                print("Booking Cancelled Successfully")
                return

        print("Booking ID Not Found")

    def show_bookings(self):

        if not self.booked_seats:

            print("No Bookings")
            return

        print("\nBooked Tickets")

        for booking in self.booked_seats.values():

            print("----------------------------")
            print("Booking ID :", booking["Booking ID"])
            print("Customer :", booking["Customer"])
            print("Seat :", booking["Seat"])