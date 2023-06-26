from typing import List

def is_available_language(language: str) -> bool:
    """ Checks if the language is available on Steam.

    Parameters
    ----------
    language: :class:`str`
        Language to be checked.

    Returns
    -------
    :class:`bool`
    """
    
    available_languages: List[str] = [
        schinese, # Simplified Chinese
        tchinese, # Traditional Chinese
        japanese,
        koreana,
        thai,
        bulgarian,
        czech,
        danish,
        german,
        spanish,
        latam,
        greek,
        french,
        italian,
        hungarian,
        dutch,
        norwegian,
        polish,
        portuguese,
        brazilian,
        romanian,
        russian,
        finnish,
        swedish,
        turkish,
        vietnamese,
        ukrainian,
    ]

    for available_language in available_languages:
        if (available_language == language):
            return True

    return False