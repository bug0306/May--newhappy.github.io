#!"D:\python files\demo\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'pyppeteer==0.0.25','console_scripts','pyppeteer-install'
__requires__ = 'pyppeteer==0.0.25'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyppeteer==0.0.25', 'console_scripts', 'pyppeteer-install')()
    )
