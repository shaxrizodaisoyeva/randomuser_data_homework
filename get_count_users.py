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
    count=0
    for user in range(len(data['results'])):
        count=user+1
    return count 