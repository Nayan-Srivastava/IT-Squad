import pandas as pd

data = {'SEATS': ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13',
                  'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20']}
df = pd.DataFrame(data, columns=['SEATS'])
data1 = {'SEATS': ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13',
                   'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20']}
df1 = pd.DataFrame(data1, columns=['SEATS'])
data2 = {'SEATS': ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13',
                   'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20']}
df2 = pd.DataFrame(data2, columns=['SEATS'])

f = 0


def movies():
    global f
    f = f + 1
    print("which movie do you want to watch?")
    Movie_dict = {"1": "TENET",
                  "2": "COOLIE NO.1",
                  "3": "EXTRACTION",
                  "4": "WONDER WOMAN 1984",
                  "5": "DIL BECHARA",
                  "6": "Back"}
    for key, value in Movie_dict.items():
        print(key, ':', value)

    movie = int(input("Choose Your Movie: "))
    Movie_dict.pop(str(movie))
    if movie == 6:
        theater()
        return 0
    if movie > 6:
        print("Wrong choice!!! Please Choose Movie from the given List...\n Thank You!")
    if f == 1:
        theater()


def theater():
    print("In Which Screen Do You wish to Watch the Movie: ")
    theatre_dict = {"1": "SCREEN 1",
                    "2": "SCREEN 2",
                    "3": "SCREEN 3"}
    for key, value in theatre_dict.items():
        print(key, ':', value)
    a = int(input("Choose a Screen: "))
    if(a==1):
        print("Available Seats")
        print(df)
    if (a == 2):
        print("Available Seats")
        print(df1)
    if (a == 3):
        print("Available Seats")
        print(df2)
    ticket = int(input("How many Seats You want To Book?: "))
    if (ticket > 5):
        print("You can book only 5 tickets at a time")
    else:
        timing(a,ticket)

def timing(a,ticket):
    time1 = {"1": "10.00AM-01:00PM ",
             "2": "01:10PM-04:10PM ",
             "3": "04:20PM-07:20PM ",
             "4": "07:30PM-10:30PM "}
    time2 = {"1": "10:15AM-01:15PM ",
             "2": "01:25PM-04:25PM ",
             "3": "04:35PM-07:35PM ",
             "4": "07:45PM-10:45PM "}
    time3 = {"1": "10:30AM-01:30PM ",
             "2": "01:40PM-04:40PM ",
             "3": "04:50PM-07:50PM ",
             "4": "08:00PM-10:45PM"}
    if a == 1:

        df.drop(df.head(ticket).index, inplace=True)
        print("Available Timings:")
        for key, value in time1.items():
            print(key, ':', value)
        t = input("Select Your Time:")
        x = time1[t]
        print("Successfull!!!\nEnjoy Movie At " + x)

    elif a == 2:
        df.drop(df1.head(ticket).index, inplace=True)
        print("Available Timings:")
        for key, value in time2.items():
            print(key, ':', value)
        t = input("Select Your Time:")
        x = time2[t]
        print("Successfull!!!\nEnjoy Movie At " + x)

    elif a == 3:
        df.drop(df2.head(ticket).index, inplace=True)
        print("Available Timings:")
        for key, value in time3.items():
            print(key, ':', value)
        t = input("Select Your Time:")
        x = time3[t]
        print("Successfull!!! \nEnjoy Movie At " + x)

    return 0


def movie(theater):
    if theater == 1:
        movies()
    elif theater == 2:
        movies()
    elif theater == 3:
        movies()
    elif theater == 4:
        movies()
    elif theater == 5:
        movies()
    elif theater == 6:
        city()
    else:
        print("Wrong choice!!! Please choose the Theater from the given list...\n Thank You")


def center1():
    print("Which Theater Do You Wish to Watch the Movie? ")
    center1_dict = {"1": "PVR Phoenix",
                    "2": "PVR Saharaganj",
                    "3": "INOX",
                    "4": "Cinepolis",
                    "5": "Wave Cinema",
                    "6": "Back"}
    for key, value in center1_dict.items():
        print(key, ':', value)
    a = int(input("Choose your Theater: "))
    movie(a)
    return 0


def center2():
    print("Which Theater Do You Wish to Watch the Movie? ")
    center2_dict = {"1": "INOX",
                    "2": "Carnival Cinema",
                    "3": "Novelty Cinema",
                    "4": "Cinepolis",
                    "5": "Sangam Cinema Hall",
                    "6": "Back"}
    for key, value in center2_dict.items():
        print(key, ':', value)
    a = int(input("Choose your Theater: "))
    movie(a)
    return 0


def center3():
    print("Which Theater Do You Wish to Watch the Movie? ")
    center3_dict = {"1": "Chandralok Cinema Hall",
                    "2": "Avtar Talkies",
                    "3": "PVR Vinayak",
                    "4": "The Palace",
                    "5": "PVR Mall",
                    "6": "Back"}
    for key, value in center3_dict.items():
        print(key, ':', value)
    a = int(input("Choose your Theater: "))
    movie(a)
    return 0

def city():
    print("Hello, Welcome To Movie Ticket Booking System: ")
    print("where you want to watch movie?:")
    city_dict = {"1": "Lucknow",
                 "2": "Kanpur",
                 "3": "Prayagraj",}
    for key, value in city_dict.items():
        print(key, ':', value)
    place = int(input("Choose your City: "))
    if place == 1:
        center1()
    elif place == 2:
        center2()
    elif place == 3:
        center3()
    else:
        print("Wrong choice!!! Please choose the city from the given list...\n Thank You")

while(df.empty!=True and df1.empty!=True and df2.empty!=True):
    print("Do You Wish to Watch a Movie ?\nY/N")
    ans=input()
    if(ans=='Y'):
        city()
    else:
        break
