import get_data

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    a=[]
    for i in range(len(data['results'])):
        a.append({"first_name": str(data['results'][i]['name']['first']), "last_name":str(data['results'][i]['name']['last']), "phone_number":str(data['results'][i]['phone'])})
    return a