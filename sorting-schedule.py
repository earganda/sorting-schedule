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


#Shell Sort
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






menu_choice = input("""Menu: 
1. View Sched
2. Add Sched 

Answer: """)

# View Sched
if menu_choice == '1':
    print('')

# Add Sched
elif menu_choice == '2':
    sched_q = input('How many subjects will you add? ')

    # This line should run n times (depending sa input of sched_q) or bahala ka
    # if you thought of something else 
    subject_time = input('Enter time: ')
    subject_name = input('Enter subject name: ')

    print('\nSubject added!\n', subject_name, '—', subject_time)

    # Sort or Main Menu
    add_choice = input("""Select:
    1 - Sort
    2 - Return to Menu
    
    Answer: """)

    # Sorting Methods
    didSelect = 0
    while (didSelect == 0):
        sorting_choice = input("""Choose a sorting method: 
        A. Bubble Sort
        B. Selection Sort
        C. Insertion Sort
        D. Shell Sort
        E. Merge Sort
        
        Answer: """)

        #NOTE: Change "variablename" to variable holding unsorted schedules

        if sorting_choice.upper() == 'A':
            bubble_sort(variablename)
            didSelect = 1

        elif sorting_choice.upper() == 'B':
            selection_sort(variablename) 
            didSelect = 1

        elif sorting_choice.upper() == 'C':
             insertion_sort(variablename)
             didSelect = 1

        elif sorting_choice.upper() == 'D':
             size = len(variablename)
             shellSort(variablename, size)
             didSelect = 1

        elif sorting_choice.upper() == 'E':
              merge_sort(variablename)
              didSelect = 1

    elif add_choice == '2':
        print('Dapat magback to menu.')

