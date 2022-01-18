import os
from datetime import datetime

os.system('git add .')

commit = 'git commit -m "' + datetime.now().strftime("%A %d %B %Y %I:%M:%S %p") +' IST"'
os.system(commit)

os.system('git push -u origin main')
