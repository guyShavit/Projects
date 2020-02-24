import random

# this function returns the menu
def menu():
        choose = input("Please choose from the Menu:\n1. Manual filling\n2. auto filling\n3. Exit\n")
        return choose


def manual():
        columns = input("a column cost 3 NIS, how many columns do you want to to fill?\n")
        while not columns.isdigit():
            print("enter only integers!")
            columns = input("a column cost 3 NIS, how many columns do you want to to fill?\n")
        paid = columns * 3
        big_list = []
        for i in range(int(columns)):
            print("please provide 6 numbers in a row")
            string = []
            for x in range(6):
                user_num = int(input("please enter number: "))
                while user_num < 1 or user_num > 37 or user_num in string:
                    print("please enter number between 1-37 only and do not repeat on the same number.")
                    user_num = int(input("please enter number: "))
                string.append(user_num)
            big_list.append(string)
        print("my list is" + str(big_list))
        is_double = False
        choose1 = input("A column cost 6 NIS if doubled. Do you want to double? y/n\n")
        while choose1 != 'y' and choose1 != 'n':
            print("press y or n only!")
            choose1 = input("A column cost 6 NIS if doubled. Do you want to double? y/n\n")
        if choose1 == 'y':
            is_double = True
            double(big_list, is_double, columns)
        else:
            choose = input("Do you want to check winning? y/n\n")
            while choose != 'y' and choose != 'n':
                print("press y or n only!")
                choose = input("Do you want to check winning? y/n\n")
            if choose == 'y':
                check(big_list, is_double, paid)
            else:
                print("your numbers are:\n" + str(big_list) + "\nBye Bye")
                return big_list


def auto():
        columns = input("a column cost 3 NIS, how many columns do you want to to fill?\n")
        while not columns.isdigit():
            print("enter only integers!")
            columns = input("a column cost 3 NIS, how many columns do you want to to fill?\n")
        paid = columns * 3
        big_list = []
        for i in range(int(columns)):
            string = []
            for x in range(6):
                user_num = random.randint(1, 37)
                if user_num in string:
                    user_num = random.randint(1, 37)
                    string.append(user_num)
                else:
                    string.append(user_num)
            big_list.append(string)
        print("my list is" + str(big_list))
        is_double = False
        choose1 = input("A column cost 6 NIS if doubled. Do you want to double? y/n\n")
        while choose1 != 'y' and choose1 != 'n':
            print("press y or n only!")
            choose1 = input("A column cost 6 NIS if doubled. Do you want to double? y/n\n")
        if choose1 == 'y':
            is_double = True
            double(big_list, is_double, columns)
        else:
            choose = input("Do you want to check winning? y/n\n")
            while choose != 'y' and choose != 'n':
                print("press y or n only!")
                choose = input("Do you want to check winning? y/n\n")
            if choose == 'y':
                check(big_list, is_double, paid)
            else:
                print("your numbers are:\n" + str(big_list) + "\nBye Bye")
                return big_list


def check(big_list, is_double, paid):
    win = []
    for x in range(6):
        num = random.randint(1, 37)
        while num in win:
            num = random.randint(1, 37)
        win.append(num)
    total = 0
    for i in range(len(big_list)):
        counter = 0
        for j in range(len(big_list[i])):
            for x in range(len(win)):
                if win[x] == big_list[i][j]:
                    counter += 1
        if is_double:
            if counter == 3:
                total = total + 20
            if counter == 4:
                total = total + 400
            if counter == 5:
                total = total + 20000
            if counter == 6:
                total = total + 2000000
        else:
            if counter == 3:
                total = total + 10
            if counter == 4:
                total = total + 200
            if counter == 5:
                total = total + 10000
            if counter == 6:
                total = total + 1000000
    print("the winning numbers are " + str(win))
    print("you have won " + str(total) + " NIS and you paid " + str(paid) + " NIS.\n")


def double(big_list, is_double, columns):
    paid = columns * 6
    choose2 = input("Do you want to check winning? y/n\n")
    if choose2 == 'y':
        check(big_list, is_double, paid)
    else:
        return big_list


# def double():

# main code
choose = menu()
while choose != '1' and choose != '2' and choose!= '3':
    print("press 1-3 only")
    choose = input("Please choose from the Menu:\n1. Manual filling\n2. auto filling\n3. Exit\n")
if choose == '1':
    manual()
elif choose == '2':
    auto()
else:
    print("bye bye")





# counter = 0
    # prize =[]
    # for i in big_list:
    #     if big_list[i][i] == win[x]:
    #         prize.append(win[x])
    #     else:
    #         continue

# print(win)
# print(big_list)
# print(prize)

