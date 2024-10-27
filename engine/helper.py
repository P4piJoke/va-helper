import re

from engine.config import PATTERN

def extractYoutubeTerm(query):
    match = re.search(PATTERN, query, re.IGNORECASE)

    return match.group(1) if match else None