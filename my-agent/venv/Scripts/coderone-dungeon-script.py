#!d:\programming\workspace\my-agent\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'coderone-challenge-dungeon==0.1.4','console_scripts','coderone-dungeon'
__requires__ = 'coderone-challenge-dungeon==0.1.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('coderone-challenge-dungeon==0.1.4', 'console_scripts', 'coderone-dungeon')()
    )
