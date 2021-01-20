import time

list_of_schedules = []
header = "+================================================="


def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:

            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1


def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


def input_subjects(not_first_recursion=False):
    if not_first_recursion:
        print("|| -------- Notice: Subject name shouldn't be empty")
    ans = input("|| Enter subject name: ")
    return ans if ans != "" else input_subjects(True)


def input_time():
    while True:
        try:
            num = input('|| Enter Time (HH:MM) : ')
            time.strptime(num, '%H:%M')
        except:
            print("|| -------- Notice: Wrong input! Please follow the correct time format")
            continue
        break
    return num


def num_of_subjects(not_first_recursion=False):
    if not_first_recursion:
        print("|| -------- Notice: Please enter value greater than 0")
    while True:
        try:
            num = int(input('|| How many subjects will you add? '))
        except:
            print("|| -------- Notice: Respond with a number, please!")
            continue
        break
    return num if num > 0 else num_of_subjects(True)


def ask_to_add_more(ans):
    if ans.upper() == 'Y':
        add_sched()
    elif ans.upper() == 'N':
        print(header)
    else:
        print("|| -------- Notice: please answer Y or N only")
        ask_to_add_more(input('|| Would you like to add more to your schedule? \n|| Y or N: ').upper())


def add_sched():
    print(header)
    for _ in range(num_of_subjects()):
        print("||------------------------------------------------")
        list_of_schedules.append({
            "subject": input_subjects(),
            "time": input_time(),
        })
    print("||------------------------------------------------")
    print(f"|| Here's a list of schedules you added: ")
    for sched in list_of_schedules:
        print(f"|| {sched['subject']} : {sched['time']}")
    print("||------------------------------------------------")

    ask_to_add_more(input('|| Would you like to add more to your schedule? \n|| Y or N: ').upper())


def convert_and_sort(ls, choice):
    converted_time = []
    converted_name = []
    for x in list_of_schedules:
        converted_time.append(x['time'].replace(":",""))
        converted_name.append(x['subject'])
    for i in range(0, len(converted_time)): 
        converted_time[i] = int(converted_time[i])
    if choice == "A":
        print('|| You chose: Bubble Sort\n|| ')
        bubble_sort(converted_time)
    if choice == "B":
        print('|| You chose: Selection Sort\n|| ')
        selection_sort(converted_time)
    if choice == "C":
        print('|| You chose: Insertion Sort\n|| ')
        insertion_sort(converted_time)
    if choice == "D":
        print('|| You chose: Shell Sort\n|| ')
        shellSort(converted_time, len(ls))
    if choice == "E":
        print('|| You chose: Merge Sort\n|| ')
        mergeSort(converted_time)
    convert_to_list_of_schedules(ls, converted_time, converted_name)


def convert_to_list_of_schedules(ls, ict, cn):
    global list_of_schedules
    temsched = []
    ct = [str(x) for x in ict]
    for i in range(len(ct)):
        index = 0
        a = ""
        if len(ct[i]) == 4:
                a = ct[i]
                a = a[:2] + ':' + a[2:]
        if len(ct[i]) == 3:
                a = ct[i]
                a = a[:1] + ':' + a[1:]
        for x in ls:
            if x['time'] == a:
                temsched.append({
                "subject": cn[index],
                "time": a,
                })
                break;
            else:
                index += 1
    list_of_schedules = temsched
    

def main_menu():
    while True:
        print(header)
        menu_choice = input('|| Menu: \n|| 1 - View Sched\n|| 2 - Add Sched \n|| Answer: ')

        # View Sched
        if menu_choice == '1':
            print('')

        # Add Sched
        elif menu_choice == '2':
            add_sched()

            # Sort or Main Menu
            add_choice = input('|| Select: \n|| 1 - Sort \n|| 2 - Return to Menu \n|| Answer: ')

            # Sorting Methods
            if add_choice == '1':
                didSelect = 0
                while (didSelect == 0):
                    print(header)
                    sorting_choice = input('|| Choose a sorting method: \n|| A. Bubble Sort \n|| B. Selection Sort \n|| C. Insertion Sort \n|| D. Shell Sort \n|| E. Merge Sort \n|| Answer: ')

                    if sorting_choice.upper() == 'A' or sorting_choice.upper() == 'B' or sorting_choice.upper() == 'C' or sorting_choice.upper() == 'D' or sorting_choice.upper() == 'E':
                        didSelect = 1
                        convert_and_sort(list_of_schedules, sorting_choice.upper())
                        for x in list_of_schedules:
                            print('|| ', x['time'], ' — ', x['subject'])
                        print("|| \n|| Sorting done!\n|| ")
                    else:
                        print("|| -------- Command not found! ")

                    return_menu = input('|| Return to menu? Press Y or N: ')
                    if return_menu.upper() == "Y":
                        main_menu()
                    else:
                        print('|| Exiting...')
                        exit()

            elif add_choice == '2':
                main_menu()


main_menu()

