# def compare(user_in,)
# def check_resources(user_in):
#    if user_in == "espresso":
#        compare()
def resources_check(juice, resource):
    for i in juice:
        if juice[i] > resource[i]:
            print(f"sorry there is not enough {i}")
            return False
    return True


def check_coins():
    print("enter the coins to proceed further!!")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_transaction(coins_gets, cost):
    if coins_gets >= cost:
        balance = round(coins_gets-cost, 2)
        print(f"here is your balance {balance} ")
        global profit
        profit += cost
        return True
    else:
        print("inserted amount is insufficient to make a coffee !!")
        return False


def coffee_making(choice, ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here is your {choice} ☕️. Enjoy!")


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit=0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
should_continue = True
while should_continue:
    user_in = input("what would you like? (espresso/latte/cappuccino)")
    if user_in == "off":
        should_continue = False
    elif user_in == "report":
        print("Water :", resources["water"])
        print("Milk : ", resources["milk"])
        print("Coffee : ", resources["coffee"])
    else:
        drink = MENU[user_in]
        if resources_check(drink["ingredients"], resources):
            coins_get = check_coins()
            if check_transaction(coins_get, drink["cost"]):
                coffee_making(user_in,drink["ingredients"])
