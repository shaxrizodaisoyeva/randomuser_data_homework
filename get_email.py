import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    a=[]
    for i in range(len(data['results'])):
        a.append(data['results'][i]['email'])
    return a