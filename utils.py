from os import path

def get_default_config():
    data = ""
    
    data += "# Api key" + "\n"
    data += "API_KEY=YOUR_API_KEY_HERE" + "\n"
    data += "\n"
    
    data += "# Secret key" + "\n"
    data += "SECRET_KEY=YOUR_SECRET_KEY_HERE" + "\n"
    data += "\n"
    
    return data
    

def file_exists(filename):
    if path.exists(filename):
        return True
        
    return False

def write_file(filename, data, append):

    if append:
        f = open(filename, 'a')
        
    else:
        f = open(filename, '+w')
    
    f.write(data)
    f.close()
    
def read_file(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data