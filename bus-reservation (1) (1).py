# Bus Reservation System

# Total seats (example: 20 seats)
seats = [0] * 20   # 0 = available, 1 = booked

def show_seats():
    print("\nSeat Status:")
    for i in range(len(seats)):
        status = "Available" if seats[i] == 0 else "Booked"
        print(f"Seat {i+1}: {status}")
    print()

def book_seat():
    show_seats()
    try:
        seat_no = int(input("Enter seat number to book: "))
        if seat_no < 1 or seat_no > len(seats):
            print("Invalid seat number!")
        elif seats[seat_no - 1] == 1:
            print("Seat already booked!")
        else:
            seats[seat_no - 1] = 1
            print(f"Seat {seat_no} booked successfully!")
    except:
        print("Invalid input!")

def cancel_seat():
    try:
        seat_no = int(input("Enter seat number to cancel: "))
        if seat_no < 1 or seat_no > len(seats):
            print("Invalid seat number!")
        elif seats[seat_no - 1] == 0:
            print("Seat already available!")
        else:
            seats[seat_no - 1] = 0
            print(f"Seat {seat_no} booking cancelled!")
    except:
        print("Invalid input!")

def main():
    while True:
        print("\n--- Bus Reservation System ---")
        print("1. View Seats")
        print("2. Book Seat")
        print("3. Cancel Seat")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_seats()
        elif choice == '2':
            book_seat()
        elif choice == '3':
            cancel_seat()
        elif choice == '4':
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

# Run the program
main()