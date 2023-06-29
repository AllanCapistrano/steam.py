from typing import List

def sanitize_srcset(srcset: str) -> List[str]:
    """ Sanitize the srcset of an image tag.

    Parameters
    ----------
    srcset: :class:`str`
        srcset content to be sanitized.

    Returns
    -------
    :class:`List[str]`
    """
    
    sanitized: List[str] = []
    
    for temp in srcset.split(", "):
        sanitized.append(temp[0:len(temp) - 3])

    return sanitized

