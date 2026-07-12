"""
===========================================================
File Name : booking.py

THEORY - CLASS VARIABLE

A Class Variable belongs to the class rather than individual
objects.

It is shared among all objects.

Example

Booking Counter

Customer 1 -> BK1001

Customer 2 -> BK1002

Customer 3 -> BK1003

All objects share the same counter.

===========================================================
"""


class Booking:

    booking_counter = 1001

    @classmethod
    def generate_booking_id(cls):
        """
        Class Method

        A class method works with class variables.

        cls refers to the class itself.
        """

        booking_id = "BK" + str(cls.booking_counter)

        cls.booking_counter += 1

        return booking_id
    