from datetime import date
from Person import Client,Provider
from Service import Service
from Book import Booking



if __name__ == "main":

    client = Client("Omolola", "+48-881278182")
    provider = Provider("Tola", "+48-123456789")
    service = Service("Haircut", 100)
    booking_date = date(2023, 10, 1)
    time_slot = "10:00 AM - 11:00 AM"

    Omolola_booking = Booking(client, provider, service, booking_date, time_slot)
    print(Omolola_booking.booking_confirmation())