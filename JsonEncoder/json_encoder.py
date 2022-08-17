import json

def encode_bool(elem):
    if (elem == True):
        return "\"" + "true" "\""
    else:
        return "\"" + "false" "\""
    
def encode_float(elem):
    return "\"" + str(elem) + "\""

def encode_str(elem):
    return "\"" + elem + "\""
    
def encode_list(elem):
    op_string = "\"["
    for i in elem:
        op_string += check_and_encode(i)
    return op_string + "]\""

def encode_dict(elem):
    op_string = "\"{"
    for i in elem:
        op_string += check_and_encode(i)
        op_string += check_and_encode(elem[i])
    return op_string + "}\""

def encode_int(elem):
    return "\"" + str(elem) + "\"" #","

def encode_none(elem):
    return "\"" + "null" + "\""

def print_json(op_string):
    for i in op_string:
        print(i)

def check_and_encode(elem):
    if (isinstance(elem, bool)):
        op_string = encode_bool(elem) + "\n"
    elif (isinstance(elem, float)):
        op_string = encode_float(elem) + "\n"
    elif (isinstance(elem, str)):
        op_string = encode_str(elem) #+ "\n"
    elif (isinstance(elem, list)):
        op_string = encode_list(elem) + "\n"
    elif (isinstance(elem, dict)):
        op_string = encode_dict(elem) + "\n"
    elif (isinstance(elem, int)):
        op_string = encode_int(elem) #+ "\n"
    elif (elem == None):
        op_string = encode_none(elem) + "\n"
    else:
        print("Unsupported Data type encountered\n")

    return op_string

def encode_json(ip_string):
    op_string = ""
    op_string += check_and_encode(ip_string)
    print_json(op_string)
    print(json.loads(op_string))

def main():
    ip_string = [23]#, 'welcome'], 45.45, True, False, None, {'message' : 'welcome', 'count' : 2}, [23, 24]]
    encode_json(ip_string)
                   
if __name__ == "__main__":
    main()