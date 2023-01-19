import os

from data import MENU , resources

cost = 0
profit = 0
def ask_money():
    global cost
    global profit
    global repeat_again
    print('please insert coins')
    quarters = int(input('how many qaurter? : ')) * 0.25
    dimes = int(input('how many dimes? : ')) * 0.10
    nickels = int(input('how many nickels? :')) * 0.05
    pennies = int(input('how many pennies? : ')) * 0.01

    sum = quarters + dimes + nickels + pennies

    if sum >= cost:
        return_change = round(sum - cost, 2)
        profit += cost
        print(f'here is ${return_change} in change')
        print(f'here is your {customer_order}')
    
    elif sum < cost:
        print('coins inserted is less. money refunded')
        repeat_again = False

def is_resource_sufficiant():
    for i in MENU[customer_order]['ingredients']:
        if resources[i] >= MENU[customer_order]['ingredients'][i]:
            resources[i] -= MENU[customer_order]['ingredients'][i]
            sufficient_resources = 'true'
        else:
            print(f'sorry not enough {i} in machine for {customer_order} ')
            sufficient_resources = 'false'

            
    if sufficient_resources == 'true':
        ask_money()
    else:
        repeat_again = False
        


    
    


def report():
    print(f' water : {resources["water"]} \n milk : {resources["milk"]} \n coffee : {resources["coffee"]}  \n money : ${profit}')

def response_order():
    global cost
    global repeat_again

    if customer_order == 'report':
        report()
        
        
    elif customer_order == 'latte':
        print(f'cost of {customer_order} is $ {MENU["latte"]["cost"]}')
        cost = MENU["latte"]["cost"]
        is_resource_sufficiant()

    elif customer_order == 'espresso':
        print(f'cost of {customer_order} is $ {MENU["espresso"]["cost"]}')
        cost = MENU["latte"]["cost"]
        is_resource_sufficiant()

    elif customer_order == 'cappuccino':
        print(f'cost of {customer_order} is $ {MENU["cappuccino"]["cost"]}')
        cost = MENU["latte"]["cost"]
        is_resource_sufficiant()

    elif customer_order == 'off':
        repeat_again = False
        
    else:
        print('sorry we dont serve this. please try somthing from our menu')
    
        
repeat_again = True

while repeat_again:
    customer_order = input('what woukd you like to have? : (espresso \ latte \ cappuccino)\n')
    response_order()
    new_cust = input()
    
    if new_cust == '1':
        os.system('cls')
    else:
        repeat_again = False



