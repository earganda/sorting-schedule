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

