MUSIC_ROOT = 'www\\assets\\audio\\start_sound.mp3'
ASSISTANT_NAME = 'Axel'
EMPTY = ''
SPACE = ' '
OPEN = 'open'
OPENING = 'Opening' + SPACE
PLAYING = 'Playing' + SPACE
ON_YOUTUBE = SPACE + 'on YouTube'
START = 'start'
NOT_FOUND = 'Not found'
SMTH_WENT_WRONG = 'Something went wrong'
DATABASE_NAME = 'assistant.db'
SYS_COMMAND_QUERY = 'SELECT path FROM sys_command WHERE name IN (?)'
WEB_COMMAND_QUERY = 'SELECT url FROM web_command WHERE name IN (?)'
PATTERN = r'play\s+(.*?)\s+on\s+youtube'