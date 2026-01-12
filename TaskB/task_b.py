# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

"""
A program that reads reservation data from a file
and prints them to the console using functions:

Reservation number: 123
Booker: Anna Virtanen
Date: 31.10.2025
Start time: 10.00
Number of hours: 2
Hourly rate: 19,95 €
Total price: 39,90 €
Paid: Yes
Venue: Meeting Room A
Phone: 0401234567
Email: anna.virtanen@example.com

"""
from datetime import datetime

def print_reservation_number(reservation: list) -> None:
    """
    Prints the reservation number

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    reservation_number = reservation[0]
    print(f"Reservation number: {reservation_number}")

def print_booker(reservation: list) -> None:
    """
    Prints the booker's name

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    booker = reservation[1]
    print(f"Booker: {booker}")

def print_date(reservation: list) -> None:
    """
    Prints the reservation date in Finnish format.

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    date = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    finnish_date = date.strftime("%d.%m.%Y")
    print(f"Date: {finnish_date}")

def print_start_time(reservation: list) -> None:
    """
    Prints the reservation start time in Finnish format.

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    start_time = datetime.strptime(reservation[3], "%H:%M").time()
    finnish_time = start_time.strftime("%H.%M")
    print(f"Start time: {finnish_time}")

def print_hours(reservation: list) -> None:
    """
    Prints the reservation start time in Finnish format.

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    hours = int(reservation[4])
    print(f"Number of hours: {hours}")

def print_hourly_rate(reservation: list) -> None:
    """
    Prints the hourly rate for the reservation

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    hourly_rate = float(reservation[5])
    print(f"Hourly rate: {hourly_rate:.2f}".replace('.', ','), "€")

def print_total_price(reservation: list) -> None:
    """
    Prints the total price of the reservation in Finnish format.

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    total_price = int(reservation[4]) * float(reservation[5])
    print(f"Total price: {total_price:.2f}".replace('.', ','), "€")

def print_paid(reservation: list) -> None:
    """
    Prints whether the reservation has been paid

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    paid = reservation[6]
    print(f"Paid: {'Yes' if paid else 'No'}")

def print_venue(reservation: list) -> None:
    """
    Prints the venue of the reservation

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    venue = reservation[7]
    print(f"Venue: {venue}")

def print_phone(reservation: list) -> None:
    """
    Prints the booker's phone number

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    phone = reservation[8]
    print(f"Phone: {phone}")

def print_email(reservation: list) -> None:
    """
    Prints the booker's email address

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    email = reservation[9]
    print(f"Email: {email}")

def main():
    """
    Reads reservation data from a file and
    prints them to the console using functions
    """
    reservations = "reservations.txt"
    with open(reservations, "r", encoding="utf-8") as f:
        reservation = f.read().strip()
        reservation = reservation.split('|')

    print_reservation_number(reservation)
    print_booker(reservation)
    print_date(reservation)
    print_start_time(reservation)
    print_hours(reservation)
    print_hourly_rate(reservation)
    print_total_price(reservation)
    print_paid(reservation)
    print_venue(reservation)
    print_phone(reservation)
    print_email(reservation)

if __name__ == "__main__":
    main()