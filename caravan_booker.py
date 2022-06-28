#NAME : Evan Mulcare  #ID: R00211686
import sys


def main():
    accommodation_type, accommodation_cost, number_of_bookings = read_file_data()
    extra_type, extra_bookings = extras()
    opening_menu(accommodation_type, accommodation_cost, number_of_bookings, extra_type, extra_bookings)
    #closing_menu(accommodation_type, accommodation_cost, number_of_bookings, extra_type, extra_bookings)


def read_file_data():
    accommodation_type = []
    accommodation_cost = []
    number_of_bookings = []

    file = "bookings_2022.txt"
    connect = open(file)
    for line in connect:
        line_data = line.split(',')
        accommodation_type.append(line_data[0])
        cost = int(line_data[1])
        accommodation_cost.append(cost)
        bookings = int(line_data[2])
        number_of_bookings.append(bookings)

    return accommodation_type, accommodation_cost, number_of_bookings


def add_one_accommodation(number_of_bookings, x, y):
    for i in range(x, y):
        number_of_bookings[i] += 1


def extras():
    extra_type = []
    extra_bookings = []

    file = "extras.txt"
    connect = open(file)
    for line in connect:
        line_data = line.split(',')
        extra_type.append(line_data[0])
        bookings = int(line_data[1])
        extra_bookings.append(bookings)

    return extra_type, extra_bookings


def opening_menu(accommodation_type, accommodation_cost, number_of_bookings, extra_type, extra_bookings):
    print("-----------LONG ISLAND RESORT---------------")

    ok = False
    while not ok:
        try:
            menu1 = "\n\t1: Make a booking" \
                    "\n\t2: Review Bookings" \
                    "\n\t3: Exit" \
                    "\n==> "

            pick = int(input(menu1))

            if pick == 1:
                new_booking(accommodation_type, accommodation_cost, number_of_bookings, extra_type, extra_bookings)

            elif pick == 2:
                review_bookings(accommodation_type, number_of_bookings, extra_bookings)

            elif pick == 3:
                exit_booking()

            else:
                print("Invalid Request")

            if 1 <= pick <= 3:
                ok = True
        except ValueError:
            print("Invalid, TRY AGAIN!!")


def new_booking(accommodation_type, accommodation_cost, number_of_bookings, extra_type, extra_bookings):
    while True:
        user_name = str(input("Please enter your Surname:"))
        while not user_name.isalpha():
            user_name = str(input("Please enter your Surname:"))
        if len(user_name) >= 1:
            break

    while True:
        user_phone = str(input("Please enter your Phone number:"))
        while not user_phone.isnumeric():
            user_phone = str(input("Please enter your Phone number:"))
        if len(user_phone) < 12:
            break

    print("Choose your accommodation type:")
    ok = False
    while not ok:
        try:
            menu2 = f"\n\t1: Deluxe Caravan    (€2000.0) {number_of_bookings[0]} booked" \
                    f"\n\t2: Standard Caravan  (€1600.0) {number_of_bookings[1]} booked" \
                    f"\n\t3: Camp Site         (€200.0)  {number_of_bookings[2]} booked" \
                    "\n\t4: No Booking" \
                    "\n==> "

            pick = int(input(menu2))

            if pick == 1:
                accommodation = accommodation_type[0]
                accommodation_price = accommodation_cost[0]
                add_one_accommodation(number_of_bookings, 0, 1)

            elif pick == 2:
                accommodation = accommodation_type[1]
                accommodation_price = accommodation_cost[1]
                add_one_accommodation(number_of_bookings, 1, 2)

            elif pick == 3:
                accommodation = accommodation_type[2]
                accommodation_price = accommodation_cost[2]
                number_of_bookings[2] += 1
                add_one_accommodation(number_of_bookings, 2, 3)

            elif pick == 4:
                print("No booking selected. Returning to opening menu.")
                opening_menu(accommodation_type, accommodation_cost, number_of_bookings, extra_type, extra_bookings)
                sys.exit()

            else:
                print("Invalid Request")

            if 1 <= pick <= 4:
                ok = True
        except ValueError:
            print("Invalid, TRY AGAIN!!")

    while True:
        user_group_amount = int(input("Please enter the total number of people in your group:"))
        if user_group_amount > 0:
            break

    while True:
        user_kids_club = int(input("How many kids will attend kids club?"))
        if 0 <= user_kids_club < user_group_amount:
            break

    valid_answers = ['yes', 'no']
    while True:
        user_pool_pass = str(input("Do you require a family pool pass (Yes/No)?").lower())
        if user_pool_pass in valid_answers:
            break

    for i in range(0, 1):
        extra_bookings[i] += user_kids_club

    total_cost_kids_club = user_kids_club * 100

    if user_pool_pass in ['y', 'yes']:
        pool_pass_price = 150
        for i in range(1, 2):
            extra_bookings[i] += 1
    else:
        pool_pass_price = 0

    total_cost_booking = accommodation_price + total_cost_kids_club + pool_pass_price

    user_info = \
        [user_name, user_phone, user_group_amount, user_kids_club, user_pool_pass, accommodation, accommodation_price,
         total_cost_booking]

    max = 3
    total_bookings = (number_of_bookings[0] + number_of_bookings[1] + number_of_bookings[2])

    if max < total_bookings:
        print("SORRY!! we are fully booked")
    else:
        print("-----------BOOKING DETAILS---------------")
        print(f"Booking ID:               {total_bookings}")
        print(f"Name:                     {user_info[0]}")
        print(f"Phone Number:             {user_info[1]}")
        print(f"Amount in Group:          {user_info[2]}")
        print(f"Kids in Kids Club:        {user_info[3]}")
        print(f"Pool Pass:                {user_info[4]}")
        print(f"Accommodation Type:       {user_info[5]}")
        print(f"Accommodation Cost:       {user_info[6]}")
        print(f"Total Cost:               {total_cost_booking}")

        with open(f"{total_bookings}.{user_name.lower()}.txt", "w") as u:
            u.write(str(user_info))

        with open("bookings_2022.txt", "w") as bookings:
            for i in range(len(accommodation_type)):
                print(f"{accommodation_type[i]},{accommodation_cost[i]},{number_of_bookings[i]}", file=bookings)

        with open("extras.txt", "w") as extras_stuff:
            for i in range(len(extra_type)):
                print(f"{extra_type[i]},{extra_bookings[i]}", file=extras_stuff)


def review_bookings(accommodation_type, number_of_bookings, extra_bookings):
    expected_income = number_of_bookings[0] * 2000 + number_of_bookings[1] * 1600 + number_of_bookings[2] * 200 \
                      + extra_bookings[0] * 100 + extra_bookings[1] * 150

    total_bookings = (number_of_bookings[0] + number_of_bookings[1] + number_of_bookings[2])
    remaining_sites = 30 - total_bookings
    if remaining_sites < 0:
        remaining_sites = 0

    if total_bookings > 0:
        average_booking = expected_income // total_bookings
    else:
        average_booking = 0

    if total_bookings >= 3:
        pop = max(number_of_bookings)
        i = number_of_bookings.index(pop)
        most_popular = accommodation_type[i]
    else:
        most_popular = "Not enough Data"

    print("-----------BOOKING REVIEW---------------")
    print(f"Deluxe Caravan:                     {number_of_bookings[0]}")
    print(f"Standard Caravan:                   {number_of_bookings[1]}")
    print(f"Camp Site:                          {number_of_bookings[2]}")

    print(f"No. for Kids Club:                  {extra_bookings[0]}")
    print(f"Total no. of pool passes:           {extra_bookings[1]}")

    print(f"Most popular accommodation:         {most_popular}")
    print(f"Expected income:                    {expected_income}")
    print(f"Average per booking:                {average_booking}")
    print(f"Number of remaining sites:          {remaining_sites}")


def closing_menu(accommodation_type, accommodation_cost, number_of_bookings, extra_type, extra_bookings):
    print("-----------THANK YOU---------------")
    ok = False
    while not ok:
        try:
            menu3 = "\n\t1: Opening Menu" \
                    "\n\t2: Exit" \
                    "\n==> "

            pick = int(input(menu3))

            if pick == 1:
                opening_menu(accommodation_type, accommodation_cost, number_of_bookings, extra_type, extra_bookings)

            elif pick == 2:
                exit_booking()

            else:
                print("Invalid Request")

            if 1 <= pick <= 2:
                ok = True
        except ValueError:
            print("Invalid, TRY AGAIN!!")


def exit_booking():
    print("-----------FINISHED---------------")
    print("Thank you for visiting the Long Island Resort booking system, return anytime!")
    sys.exit()


main()
