"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE

# Get the user name

# Greet the user

# Show the menu and ask to pick a choice

# If they pick 1
#
# Else, if they pick 2
#
# Else, if they pick 3
#
# Else

# Thank the user for the visit

def greet(name):
    return f'Hello, {name}'

def print_lst(lst_1, lst_2):
    
    print()
    print('Items in warehouse 1:')
    print()
    for ware in lst_1:
        
        print(f'- {ware}')
        
    print()
    print('Items in warehouse 2:')
    print()
    
    for ware in lst_2:
        
        print(f'- {ware}')
        
def get_integer(prompt):
    
    while True:
        value = input(prompt)
        
        try:
            return int(value)
        
        except ValueError:
            print('Invalid value. please enter integer.')

def query_options(name):
    
    Turn_on_and_off_2 = True
    Turn_on_and_off = True
    
    while Turn_on_and_off:
        
        options_three = input(f'What would you like to do?\n1. List items by warehouse\n2. Search an item and place an order\n3. Quit\nType the number of the operation(1 \\2 \\3): ')
        
        if options_three == '3':
            
            print(f'Thank you for your visit, {name}!')
            Turn_on_and_off = False
        
        if options_three not in ['1', '2', '3' ]:
            
            print('**************************************************')
            print(f'{options_three} is not a valid operation. ')
            print('**************************************************')
            print()
            print(f'Thank you for your visit, {name}!')
            Turn_on_and_off = False
        
        if options_three == '1':
            
            print_lst(warehouse1, warehouse2)
            break
        
        elif options_three == '2':
            
            ask_for_item_name = input('What is the name of the item?: ')
            
            count_warehouse1 = warehouse1.count(ask_for_item_name)
            count_warehouse2 = warehouse2.count(ask_for_item_name)
            
            if count_warehouse1 > 0 and count_warehouse2 > 0:
                
                print(f'Amount available:{count_warehouse1 + count_warehouse2}\nLocation: Both warehouses')
                
                if count_warehouse1 > count_warehouse2:
                    
                    print(f'Maximum availability: {count_warehouse1} in Warehouse 1')
                    
                elif count_warehouse2 > count_warehouse2:
                    
                    print(f'Maximum availability: {count_warehouse2} in Warehouse 2')
                    
                else:
                    
                    print(f'Maximum availability: {count_warehouse1} in Warehouse 1\nMaximum availability: {count_warehouse2} in Warehouse 2')
                
                
                ask_for_placing_order = input('Would you like to order this item?(y/n): ')
                
                while Turn_on_and_off_2:
                    
                    if ask_for_placing_order == 'n':
                        print(f'Thank you for your visit, {name}!')
                        Turn_on_and_off = False
                        Turn_on_and_off_2 = False
                    
                    if ask_for_placing_order not in ['y', 'n']:
                        print('Invalid choice. Try again.')
                        ask_for_placing_order = input('Would you like to order this item?(y/n): ')
                        continue
                    
                    if ask_for_placing_order == 'y':
                        
                        ask_for_amount = get_integer('How many would you like? :')
                        
                        if ask_for_amount > count_warehouse1 + count_warehouse2:
                            print('**************************************************')
                            print(f'There are not this many available.\nThe maximum amount that can be ordered is {count_warehouse1 + count_warehouse2}')
                            print('**************************************************')
                            ask_again = input('Would you like to order the maximum available?(y/n): ')
                            while True:
                                if ask_again == 'n':
                                    print(f'Thank you for your visit, {name}!')
                                    Turn_on_and_off = False
                                    Turn_on_and_off_2 = False
                                    break
                                if ask_again not in ['y', 'n']:
                                    print('Invalid choice. Try again.')
                                    ask_again = input('Would you like to order the maximum available?(y/n): ')

                                    continue
                                if ask_again == 'y':
                                    print(f'{count_warehouse1 + count_warehouse2} {ask_for_item_name} have been ordered')
                                    print(f'Thank you for your visit, {name}!')
                                    Turn_on_and_off = False
                                    Turn_on_and_off_2 = False
                                    break
                        else:
                            print(f'{ask_for_amount} {ask_for_item_name} have been ordered')
                            print(f'Thank you for your visit, {name}!')
                            Turn_on_and_off = False
                            Turn_on_and_off_2 = False
                            
            elif count_warehouse1 > 0 and count_warehouse2 == 0:
                
                print(f'Amount available:{count_warehouse1}\nLocation: Warehouse 1')
                ask_for_placing_order = input('Would you like to order this item?(y/n): ')
                
                while Turn_on_and_off_2:
                    
                    if ask_for_placing_order == 'n':
                        print(f'Thank you for your visit, {name}!')
                        Turn_on_and_off = False
                        Turn_on_and_off_2 = False
                    
                    if ask_for_placing_order not in ['y', 'n']:
                        print('Invalid choice. Try again.')
                        ask_for_placing_order = input('Would you like to order this item?(y/n): ')
                        continue
                    
                    if ask_for_placing_order == 'y':
                        
                        ask_for_amount = get_integer('How many would you like? :')
                        
                        if ask_for_amount > count_warehouse1 + count_warehouse2:
                            print('**************************************************')
                            print(f'There are not this many available.\nThe maximum amount that can be ordered is {count_warehouse1 + count_warehouse2}')
                            print('**************************************************')
                            ask_again = input('Would you like to order the maximum available?(y/n): ')
                            while True:
                                if ask_again == 'n':
                                    print(f'Thank you for your visit, {name}!')
                                    Turn_on_and_off = False
                                    Turn_on_and_off_2 = False
                                    break
                                if ask_again not in ['y', 'n']:
                                    print('Invalid choice. Try again.')
                                    ask_again = input('Would you like to order the maximum available?(y/n): ')

                                    continue
                                if ask_again == 'y':
                                    print(f'{count_warehouse1 + count_warehouse2} {ask_for_item_name} have been ordered')
                                    print(f'Thank you for your visit, {name}!')
                                    Turn_on_and_off = False
                                    Turn_on_and_off_2 = False
                                    break
                        else:
                            print(f'{ask_for_amount} {ask_for_item_name} have been ordered')
                            print(f'Thank you for your visit, {name}!')
                            Turn_on_and_off = False
                            Turn_on_and_off_2 = False
                
            elif count_warehouse1 == 0 and count_warehouse2 > 0:
                
                print(f'Amount available:{count_warehouse2}\nLocation: Warehouse 2')
                ask_for_placing_order = input('Would you like to order this item?(y/n): ')
                while Turn_on_and_off_2:
                    
                    if ask_for_placing_order == 'n':
                        print(f'Thank you for your visit, {name}!')
                        Turn_on_and_off = False
                        Turn_on_and_off_2 = False
                    
                    if ask_for_placing_order not in ['y', 'n']:
                        print('Invalid choice. Try again.')
                        ask_for_placing_order = input('Would you like to order this item?(y/n): ')
                        continue
                    
                    if ask_for_placing_order == 'y':
                        
                        ask_for_amount = get_integer('How many would you like? :')
                        
                        if ask_for_amount > count_warehouse1 + count_warehouse2:
                            print('**************************************************')
                            print(f'There are not this many available.\nThe maximum amount that can be ordered is {count_warehouse1 + count_warehouse2}')
                            print('**************************************************')
                            ask_again = input('Would you like to order the maximum available?(y/n): ')
                            while True:
                                if ask_again == 'n':
                                    print(f'Thank you for your visit, {name}!')
                                    Turn_on_and_off = False
                                    Turn_on_and_off_2 = False
                                    break
                                if ask_again not in ['y', 'n']:
                                    print('Invalid choice. Try again.')
                                    ask_again = input('Would you like to order the maximum available?(y/n): ')

                                    continue
                                if ask_again == 'y':
                                    print(f'{count_warehouse1 + count_warehouse2} {ask_for_item_name} have been ordered')
                                    print(f'Thank you for your visit, {name}!')
                                    Turn_on_and_off = False
                                    Turn_on_and_off_2 = False
                                    break
                        else:
                            print(f'{ask_for_amount} {ask_for_item_name} have been ordered')
                            print(f'Thank you for your visit, {name}!')
                            Turn_on_and_off = False
                            Turn_on_and_off_2 = False
            else:
                print(f'Amount available: 0\nLocation: Not in stock')
                print(f'Thank you for your visit, {name}!')
                Turn_on_and_off = False
                Turn_on_and_off_2 = False
                


            
            
def get_user_name():
    
    name = input('What is your user name?: ')
    
    return name



def main():
    user_name = get_user_name()
    print(greet(user_name))
    query_options(user_name)
    
    
main()


