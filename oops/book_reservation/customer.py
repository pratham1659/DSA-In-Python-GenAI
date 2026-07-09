"""
===========================================================
File Name : customer.py

THEORY - CLASS AND OBJECT

Class:
------
A class is a blueprint or template used to create objects.
It defines the properties (attributes) and behaviors (methods)
that an object will have.

Object:
-------
An object is a real-world instance of a class.

Example:
Car -> Class
BMW -> Object

Here,
Customer is a class.
Every customer who books a ticket becomes an object of this class.

OOP Concepts Used
-----------------
1. Class
2. Object
3. Constructor (__init__)
4. Encapsulation

===========================================================
"""


class Customer:

    def __init__(self, customer_name):
        """
        Constructor

        __init__() is automatically called whenever an object
        is created.

        It initializes the object variables.
        """

        self.customer_name = customer_name