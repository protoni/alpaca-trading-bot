from os import path

DEFAULT_API_KEY = "YOUR_API_KEY_HERE"
DEFAULT_SECRET_KEY = "YOUR_SECRET_KEY_HERE"

def get_default_config():
    data = ""
    
    data += "# Api key" + "\n"
    data += "API_KEY=" + DEFAULT_API_KEY + "\n"
    data += "\n"
    
    data += "# Secret key" + "\n"
    data += "SECRET_KEY="+ DEFAULT_SECRET_KEY + "\n"
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
    
def get_lines_in_file(filename):
    lines = []
    
    f = open(filename, "r")
    
    for line in f:
        line = line.rstrip("\n\r")
        if len(line) > 0:
            if line[0] != '#':
                lines.append(line)
    
    f.close()
    
    return lines
    
def get_value_from_config(filename, param):
    lines = get_lines_in_file(filename)
    
    for line in lines:
        if param in line:
            return line.split(param + "=", 1)[1]
            
    return ""



