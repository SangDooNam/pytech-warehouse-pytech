"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

VALID_MENU_CHOICES = ['1', '2', '3']
YES_OR_NO = ['y', 'n']

def get_user_name():
    """Ask the user to provide a name."""
    name = input('What is your user name?: ')
    
    return name

def greet(name):
    """Greet the user."""
    return f'Hello, {name}'

def get_int(prompt):
    """
    Prompt the user for an integer input and validate it.
    
    Parameters:
    - prompt (str): The message displayed to the user.

    Returns:
    int: The validated integer provided by the user.

    Note:
    The function will repeatedly ask the user until a valid integer is provided.
    """
    while True:
        
        value = input(prompt)
        
        try:
            
            return int(value)
        except ValueError:
            print('Please enter integer.')

def lst_of_items(lst1, lst2):
    """
    Print items from two given lists, typically representing warehouse inventories.
    
    Parameters:
    - lst1 (list): Items in warehouse 1.
    - lst2 (list): Items in warehouse 2.
    
    Note:
    The items from each warehouse are printed separately.
    """
    print()
    print('Items in warehouse 1:')
    print()
    for item in lst1:
        
        print(f'- {item}')
    print()
    print('Items in warehouse 2:')
    print()
    for item in lst2:
        
        print(f'- {item}')

def ask_for_max(name, total, item_name):
    """
    Prompt to order up to the maximum quantity available.
        
    Parameters:
    - name (str): The name of the user.
    - total (int): The total available quantity of the item.
    - item_name (str): The name of the item user is interested in.
    
    Note:
    This function is following the function 'ask_for_placing_order()'.
    This function is executed when user types in more amount than the 'total' parameter. 
    """
    while True:
        ask_again = input('Would you like to order the maximum available?(y/n): ')
                            
        if ask_again not in YES_OR_NO:
            
            print(f'{ask_again} is not a valid operation. please try again.')
            continue
        
        if ask_again == 'n':
            
            print(f'Thank you for your visit, {name}!')
            
            break
        elif ask_again == 'y':
            
            print(f'{total} {item_name} have been ordered')
            print()
            print(f'Thank you for your visit, {name}')
            break
                        


def ask_for_placing_order(name, total, item_name):
    """
    Prompt the user to place an order for a specific item.

    Parameters:
    - name (str): The name of the user.
    - total (int): The total available quantity of the item.
    - item_name (str): The name of the item user is interested in.

    Returns:
    None. This function only interacts with the user via print statements and input prompts.

    Note:
    The function loops until the user provides a valid input or decides not to order.
    If the user wishes to order, they're prompted for the desired quantity. 
    Various messages are shown based on the available stock and desired quantity.
    """
    continue_loop = True
    
    while continue_loop:
        
        ask_for_order = input('Would you like to order this item?(y/n): ')
        
        if ask_for_order not in YES_OR_NO:
            
            print(f'{ask_for_order} is not a valid operation. please try again.')
            continue
        
        if ask_for_order == 'n':
            
            print(f'Thank you for your visit, {name}!')
            
            continue_loop = False
        
        elif ask_for_order == 'y':
            
            while True:
                
                ask_for_amount = get_int('How many would you like?: ')
                
                if ask_for_amount <= 0:
                    print('Nothing has been ordered')
                    print()
                    print(f'Thank you for your visit, {name}!')
                    continue_loop = False
                    break
                
                if ask_for_amount > total:
                    
                    print('**************************************************')
                    print(f'There are not this many available. The maximum amount that can be ordered is {total}')
                    print('**************************************************')
                    ask_for_max(name, total, item_name)

                        
                
                elif total >= ask_for_amount > 0:
                    
                    print(f'{ask_for_amount} {item_name} have been ordered')
                    print()
                    print(f'Thank you for your visit, {name}')
                    continue_loop = False
                    break
                
                return
                
def searching_for_item(name):
    """
    Search item and validate the amount of the item in each warehouse.

    Parameters:
    - name (str): The name of the user.

    Returns:
    None. This function only interacts with the user via print statements and input prompts.

    Note:
    The function is following the function 'option()'.
    This function is executed if the user selects number 2 in option().
    This function compares the amount of the searched item in each warehouse . 
    If there is no searched item it will quit the process.
    This function makes use of two lists, warehouse1 and warehouse2, from data module
    """
    
    while True:
        looking_for_item = input('What is the name of the item?: ')
        
        item_in_warehouse1 = warehouse1.count(looking_for_item)
        item_in_warehouse2 = warehouse2.count(looking_for_item)
        
        total_amount = item_in_warehouse1 + item_in_warehouse2
        
        if total_amount == 0:
            
            print(f'Amount available: {total_amount}')
            print('Location: Not in stock')
            print()
            print(f'Thank you for your visit, {name}!')
            break
        
        if item_in_warehouse1 > 0 and item_in_warehouse2 > 0:
            
            print(f'Amount available: {total_amount}')
            print(f'Location: Both warehouses')
            print(f'Maximum availability: {item_in_warehouse1} in Warehouse 1')
            print(f'Maximum availability: {item_in_warehouse2} in Warehouse 2')
            ask_for_placing_order(name, total_amount,looking_for_item)
        elif item_in_warehouse1 > 0 and item_in_warehouse2 == 0:
            
            print(f'Amount available: {item_in_warehouse1}')
            print(f'Location: Warehouse 1')
            print(f'Maximum availability: {item_in_warehouse1} in Warehouse 1')
            ask_for_placing_order(name, total_amount,looking_for_item)
        elif item_in_warehouse2 > 0 and item_in_warehouse1 == 0:
            
            print(f'Amount available: {item_in_warehouse2}')
            print(f'Location: Warehouse 2')
            print(f'Maximum availability: {item_in_warehouse2} in Warehouse 2')
            ask_for_placing_order(name, total_amount,looking_for_item)
        return
    
def options(name):
    """
    Prompt the user to continuously select one of three options:
    1. List items by warehouse
    2. Search an item and place an order
    3. Quit

    Parameters:
    - name (str): The name of the user.

    Returns:
    None. This function only interacts with the user via print statements and input prompts.

    Note:
    This function orchestrates the user's main interactions with the program, 
    delegating to other functions based on user choice. The function runs in a loop until 
    the user decides to quit.
    """
    while True:
    
        query_for_options = input('What would you like to do?\n1. List items by warehouse\n2. Search an item and place an order\n3. Quit\nType the number of the operation(1\\2\\3): ')

        if query_for_options == '3':
            print(f'Thank you for your visit, {name}!')
            break
        
        if query_for_options not in VALID_MENU_CHOICES:
            print('**************************************************')
            print(f'{query_for_options} is not valid operation')
            print('**************************************************')
            print()
            print(f'Thank you for your visit, {name}!')
            
        if query_for_options == '1':
            
            lst_of_items(warehouse1, warehouse2)
            
        elif query_for_options == '2':
            
            searching_for_item(name)
        return
        


def main():
    """
    Entry point for the warehouse management program.
    
    This function performs the following steps:
    1. Fetches the user's name.
    2. Greets the user.
    3. Presents options for interacting with the warehouse system.
    
    Returns:
    None. The function interacts with the user via print statements and input prompts.
    """
    user_name = get_user_name()
    print(greet(user_name))
    options(user_name)

main()