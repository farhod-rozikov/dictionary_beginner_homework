def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    min_age = {}
    i = 100
    for _dict in data:
        if i > _dict['age']:
            i = _dict['age']
            min_age = _dict
    return min_age['name']