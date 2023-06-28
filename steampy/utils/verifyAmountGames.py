def verify_amount(amount) -> int:
    """ Check whether the amount parameter is valid or not.

    Parameters
    ----------
    amount: :class:`str`
        amount of something.
    

    Returns
    -------
    :class:`int`
    """
    
    if (amount > 50 or amount <= 0):
        amount = 50

    return amount