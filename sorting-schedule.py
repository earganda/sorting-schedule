import time

list_of_schedules = []


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


def merge_sort(nums):

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)


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
    if ans == 'Y':
        add_sched()
    elif ans == 'N':
        print("+=================================================")
    else:
        print("|| -------- NOTICE: please answer y or n only")
        ask_to_add_more(input("|| would you like to add more to your schedule? y or n: ").upper())


def add_sched():
    print("+=================================================")
    for _ in range(num_of_subjects()):
        print("||------------------------------------------------")
        list_of_schedules.append({
            "subject": input_subjects(),
            "time": input_time(),
        })
    print("||------------------------------------------------")
    print(f"|| Here's a list of the schedules you added: ")
    for sched in list_of_schedules:
        print(f"|| {sched['subject']} : {sched['time']}")
    print("||------------------------------------------------")

    ask_to_add_more(input("|| would you like to add more to your schedule? Y or N: ").upper())


menu_choice = input("""Menu: 
1. View Sched
2. Add Sched

Answer: """)


# View Sched
if menu_choice == '1':
    print('')

# Add Sched
elif menu_choice == '2':
    add_sched()

    # Sort or Main Menu
    add_choice = input("""Select:
    1 - Sort
    2 - Return to Menu
    
    Answer: """)

    # Sorting Methods
    if add_choice == '1':
        didSelect = 0
        while (didSelect == 0):
            sorting_choice = input("""Choose a sorting method: 
            A. Bubble Sort
            B. Selection Sort
            C. Insertion Sort
            D. Shell Sort
            E. Merge Sort
        
            Answer: """)

            # Change "variablename" to variable holding unsorted schedules

            if sorting_choice.upper() == 'A':
                bubble_sort(list_of_schedules)
                didSelect = 1

            elif sorting_choice.upper() == 'B':
                selection_sort(list_of_schedules) 
                didSelect = 1

            elif sorting_choice.upper() == 'C':
                insertion_sort(list_of_schedules)
                didSelect = 1

            elif sorting_choice.upper() == 'D':
                size = len(list_of_schedules)
                shellSort(list_of_schedules, size)
                didSelect = 1

            elif sorting_choice.upper() == 'E':
                merge_sort(list_of_schedules)
                didSelect = 1

            return_menu = input('Return menu?')

    elif add_choice == '2':
        print('Dapat magback to menu.')

