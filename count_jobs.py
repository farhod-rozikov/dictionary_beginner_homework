def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    count = 0
    for _dict in data:
        if _dict['job'] == job:
            count += 1 
    return count