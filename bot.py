import requests, json
import utils

# Configs
CONFIG_FILE = "config"
API_KEY = utils.DEFAULT_API_KEY
SECRET_KEY = utils.DEFAULT_SECRET_KEY

# API endpoints
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
ASSETS_URL = "{}/v2/assets".format(BASE_URL)
HEADERS={'APCA-API-KEY-ID':API_KEY, 'APCA-API-SECRET-KEY':SECRET_KEY}

ASSETS_FILE = "assets.txt"
ASSETS = {}
TRADEABLE_ASSETS = []

def load_config():
    global API_KEY, SECRET_KEY, HEADERS
    data = utils.read_file(CONFIG_FILE)
    splitted = data.split('\n')
    
    # Load API KEY
    key = utils.get_value_from_config(CONFIG_FILE, "API_KEY")
    if key != "" and key != utils.DEFAULT_API_KEY:
        API_KEY = key
    else:
        print("Failed to load API KEY!")
        
    # Load Secret key
    key = utils.get_value_from_config(CONFIG_FILE, "SECRET_KEY")
    if key != "" and key != utils.DEFAULT_SECRET_KEY:
        SECRET_KEY = key
    else:
        print("Failed to load SECRET KEY!")
    
    # Set config info to headers
    HEADERS={'APCA-API-KEY-ID':API_KEY, 'APCA-API-SECRET-KEY':SECRET_KEY}

def load_assets():
    global ASSETS
    
    data = utils.read_file(ASSETS_FILE)
    print(data)
    ASSETS = data
    

def check_config():
    if not utils.file_exists(CONFIG_FILE):
        
        print("Creating a new config file!")
        configData = utils.get_default_config()
        
        utils.write_file(CONFIG_FILE, configData, False)
        print("Default config file created!")
    else:
        print("Config file OK")
        load_config()

def print_all_stock_names():
    global ASSETS
    '''
    for item in ASSETS:
        print(item["symbol"])
    '''
    print("All assets: " + str(len(ASSETS)))
    
def print_tradeable_stock_names():
    global TRADEABLE_ASSETS, ASSETS
    
    for item in ASSETS:
        if item["tradable"]:
            TRADEABLE_ASSETS.append(item)
        
    print("Tradeable assets: " + str(len(TRADEABLE_ASSETS)))

def save_assets():
    global ASSETS
    
    assets = get_assets()
    ASSETS = assets;
    
    '''
    if not utils.file_exists(ASSETS_FILE):
    
        print("Fetching trading assets.")
        assets = get_assets()
        
        ASSETS = assets;
        print("Saving trading assets.")
        utils.write_file("assets.txt", str(assets), False)
        
        print("Trading assets saved to " + ASSETS_FILE)
    else:
        print("Loading trading assets from the file system")
        load_assets()
        print("Trading assets OK")
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

def init():
    check_config()
    save_assets()

#response = create_order("MSFT", 1000, "buy", "market", "gtc")
#response = create_order("AAPL", 100, "buy", "market", "gtc")

#print(response)

#orders = get_orders()
#print(orders)

#print(str(assets))
init()
print_all_stock_names()
print_tradeable_stock_names()
