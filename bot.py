import requests, json
import utils

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
ASSETS_URL = "{}/v2/assets".format(BASE_URL)
#HEADERS={'APCA-API-KEY-ID':API_KEY, 'APCA-API-SECRET-KEY':SECRET_KEY}

ASSETS_FILE = "assets.txt"
CONFIG_FILE = "config"

API_KEY = "default"
SECRET_KEY = "default"

def load_config():
    print(utils.read_file(CONFIG_FILE))

def load_assets():
    pass

def check_config():
    if not utils.file_exists(CONFIG_FILE):
        
        print("Creating a new config file!")
        configData = utils.get_default_config()
        
        utils.write_file(CONFIG_FILE, configData, False)
        print("Default config file created!")
    else:
        print("Config file OK")
        load_config()

def save_assets():
    if not utils.file_exists(ASSETS_FILE):
    
        print("Fetching trading assets.")
        assets = get_assets()
        
        print("Saving trading assets.")
        utils.write_file("assets.txt", str(assets), False)
        
        print("Trading assets saved to " + ASSETS_FILE)
    else:
        print("Trading assets OK")
        load_assets()

'''
def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    
    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': time_in_force
    }
    
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    
    return json.loads(r.content)
    
def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)
    
    return json.loads(r.content)

def get_assets():
    r = requests.get(ASSETS_URL, headers=HEADERS)
    
    return json.loads(r.content)
'''
#response = create_order("MSFT", 1000, "buy", "market", "gtc")
#response = create_order("AAPL", 100, "buy", "market", "gtc")

#print(response)

#orders = get_orders()
#print(orders)

#print(str(assets))

check_config()
save_assets()