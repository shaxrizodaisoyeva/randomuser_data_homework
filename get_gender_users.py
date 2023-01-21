import get_data

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    a=[]
    for i in range(len(data['results'])):
        c=data['results'][i]['gender']
        if c=='male':
            a.append({"Male":1})
        if c=="female":
            a.append({"Female":0})
    return a