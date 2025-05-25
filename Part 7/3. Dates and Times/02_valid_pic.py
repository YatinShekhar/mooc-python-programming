import datetime

def is_it_valid(pic):

    if len(pic) == 11:
        pass
    else:
        return False

    if pic[6] in ["+", "-", "A"]:

        if pic[6] == "+":
            y = int(pic[4:6]) + 1800 
        elif pic[6] == "-":
            y = int(pic[4:6]) + 1900 
        else: 
            y = int(pic[4:6]) + 2000

    else:
        return False
        
    d = pic[0:2]
    m = pic[2:4]

    date = f"{y}-{m}-{d}"

    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return False
    
    num = int(pic[0:6] + pic[7:10])
    remainder = num%31 
    string = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    if pic[-1] == string[remainder]:
        return True 
    else:
        return False
    
if __name__ == "__main__":
    print(is_it_valid("081142-720N"))