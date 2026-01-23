# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

"""
Program that reads reservation details from a file
and prints them to the console:

Reservation number: 123
Booker: Anna Virtanen
Date: 31.10.2025
Start time: 10.00
Number of hours: 2
Hourly price: 19,95 €
Total price: 39,90 €
Paid: Yes
Location: Meeting Room A
Phone: 0401234567
Email: anna.virtanen@example.com
"""

from datetime import datetime

def main():
    # Define the file name directly in the code
    reservations = "reservations.txt"

    # Open the file and read its contents
    with open(reservations, "r", encoding="utf-8") as f:
        reservation = f.read().strip()

    # Print the reservation to the console
    reservation_number = int(reservation.split('|')[0])
    print("Reservation number:", reservation_number)
    booker = reservation.split('|')[1]
    print("Booker:", booker)
    date = datetime.strptime(reservation.split('|')[2], "%Y-%m-%d").date()
    print("Date:", date.strftime("%d.%m.%Y"))
    start_time = datetime.strptime(reservation.split('|')[3], "%H:%M").time()
    print("Start time:", start_time.strftime("%H.%M"))
    number_of_hours = int(reservation.split('|')[4])
    print("Number of hours:", number_of_hours)
    hourly_price = float(reservation.split('|')[5])
    print("Hourly price:", f"{hourly_price:.2f}".replace('.', ','), "€")
    total_price = hourly_price*number_of_hours
    print("Total price:", f"{total_price:.2f}".replace('.', ','), "€")
    paid = reservation.split('|')[6]
    print(f"Paid: {'Yes' if paid else 'No'}")
    location = reservation.split('|')[7]
    print("Location:", location)
    phone = reservation.split('|')[8]
    print("Phone:", phone)
    email = reservation.split('|')[9]
    print("Email:", email)

if __name__ == "__main__":
    main()