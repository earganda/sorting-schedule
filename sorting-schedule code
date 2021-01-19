def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array


menu_choice = input("""Menu: 
1. View Sched
2. Add Sched 

Answer: """)

if menu_choice == '2':
    sched_q = input('How many subjects will you add? ')

    # this line should run n times (depending sa input sa sched_q)
    subject_time = input('Enter time: ')
    subject_name = input('Enter subject name: ')

    print('\nSubject added!\n', subject_name, '—', subject_time)

    add_choice = input("""Select:
    1 - Sort
    2 - Return to Menu
    
    Answer: """)

    if add_choice == '1':
        sorting_choice = input("""Choose a sorting method: 
        A. Bubble Sort
        B. Selection Sort
        C. Insertion Sort
        D. Shell Sort
        E. Merge Sort
        
        Answer: """)

        if sorting_choice.upper() == 'A':
            print('Kayo bahala here')

        elif sorting_choice.upper() == 'B':
            print('Kayo bahala here')    

        elif sorting_choice.upper() == 'C':
            print('Kayo bahala here')

        elif sorting_choice.upper() == 'D':
            print('Kayo bahala here')

        elif sorting_choice.upper() == 'E':
            print('Kayo bahala here')

        return_menu = input('Return menu?')

    elif add_choice == '2':
        print('Dapat magback to menu.')

