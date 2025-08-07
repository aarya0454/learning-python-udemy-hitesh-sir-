chai_menu = {"masala":30,"ginger":40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("they key that you're looking for is not there ")