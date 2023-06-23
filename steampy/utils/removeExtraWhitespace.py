from re import sub

def remove_extra_whitespace(string: str) -> str:
    """ Remove extra whitespace after the word.

    Parameters
    ----------
    string: :class:`str`
        String with extra whitespace.

    Returns
    -------
    :class:`str`
    """
    
    return sub(r'\s{2,}', '', string)