import os

from data import MENU , resources

cost = 0

def ask_money():
    global cost
    print('please insert coins')
    quarters = int(input('how many qaurter? : ')) * 0.25
    dimes = int(input('how many dimes? : ')) * 0.10
    nickels = int(input('how many nickels? :')) * 0.05
    pennies = int(input('how many pennies? : ')) * 0.01

    sum = quarters + dimes + nickels + pennies
    return_change = sum - cost
    print(f'here is ${return_change} in change')
    print(f'here is your {customer_order}')
    
    


def report():
    print(f' water : {resources["water"]} \n milk : {resources["milk"]} \n coffee : {resources["coffee"]} ')

def response_order():
    global cost

    if customer_order == 'report':
        report()
        
    elif customer_order == 'latte':
        print(f'cost of {customer_order} is $ {MENU["latte"]["cost"]}')
        cost = MENU["latte"]["cost"]
    elif customer_order == 'espresso':
        print(f'cost of {customer_order} is $ {MENU["espresso"]["cost"]}')
        cost = MENU["latte"]["cost"]
    elif customer_order == 'cappuccino':
        print(f'cost of {customer_order} is $ {MENU["cappuccino"]["cost"]}')
        cost = MENU["latte"]["cost"]
    elif customer_order == 'turn_off':
        repeat_again = False
    else:
        print('sorry we dont serve this. please try somthing from our menu')
    
        
repeat_again = True

while repeat_again:
    customer_order = input('what woukd you like to have? : (espresso \ latte \ cappuccino)\n')
    response_order()
    print(ask_money())
    print('thank you for visiting, please visit again')
    
    if input('') == '1':
        os.system('cls')



