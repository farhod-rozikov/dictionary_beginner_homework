def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    max_age = {}
    i = 0
    for _dict in data:
        if i < _dict['age']:
            i = _dict['age']
            max_age = _dict
    return max_age['name']