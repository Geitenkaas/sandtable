#Sandtable Script v1.0
#Last edit: 12/03/26
#Author: Ross Popovs
import decimal

#Script Config

#Default starting cash (in million)
DEFAULT_CASH = 50.0

#Cost per one 1cm^3 of sand (in million)
VOLUME_COST = 0.1

#Name of Text DAT node to hold text for UI
CASH_TEXT_NODE = "Cash"

#Script variables
acceptTransformRequests = False
cash = 50.0



def start_game():
    global acceptTransformRequests
    acceptTransformRequests = True
    print("Game Started - now accepting transform requests")

def request_transform(displacedVolume):
    global cash
    cost = VOLUME_COST * displacedVolume
    if cost <= cash:
        decrease_cash(cost)
        return True
    else:
        print(f"Not enough cash for requested transform. Cash: {cash}m, Cost: {cost}m")
        return False

def decrease_cash(amount):
    global cash
    cash = max(cash-amount,0)
    print(f'Cash decreased by {amount}m. New cash is {cash}m')

def reset_cash():
    global cash
    cash = DEFAULT_CASH
    print(f'Cash reset to {cash}m')

def update_TD_var():
    #Sets the 'text' property of a Text DAT node
    op(CASH_TEXT_NODE).text = f'£{cash}m'

def game_over():
    print('Game over')
    global acceptTransformRequests
    acceptTransformRequests = False
    reset_cash()

def start():
    print("Script Loaded")
    reset_cash()

