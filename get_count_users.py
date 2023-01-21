from webbrowser import get
import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    r=data['results']
    l=[]
    for user in r:
        n=user['name']
    l+=n['first']
    count=len(l)
    return count