import csv

records = []
headings = []

def load_data(file_path):
    print("Loading data...")

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)

        for i in csv_reader:
            records.append(i)

    print("Done!")

def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")


def display_menu():
    print(
    """
    
Please select one of the following options:
[1] Display the names of all passengers
[2] Display the number of passengers that survived
[3] Display the number of passengers per gender
[4] Display the number of passengers per age group
    
""")
    return int(input())


def display_passenger_names():
    print("The names of the passengers are...")


    for i in records:
        passenger_name = i[3]
        print(passenger_name)

def display_num_survivors():
    num_survived = 0
    for i in records:
        survival = int(i[1])
        if survival == 1:
            num_survived += 1

    print(f"{num_survived} passengers survived")


def display_passengers_per_gender():
    females = 0
    males = 0
    for i in records:
        gender = i[4]
        if gender == 'male':
            males += 1
        elif gender == 'female':
            females += 1

    print(f"females:{females}, males:{males}")

def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    for i in records:
        if i[5] != "":
            age = float(i[5])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1
    print(f"children:{children}, adults:{adults}, elderly:{elderly}")


if __name__ == "__main__":
    run()
    select_option = display_menu()
    print(f"You have selected option: {select_option}")
    if select_option == 1:
        display_passenger_names()
    elif select_option == 2:
        display_num_survivors()
    elif select_option == 3:
        display_passengers_per_gender()
    elif select_option == 4:
        display_passengers_per_age_group()
    else:
        print("Error! Option not recognised!")



