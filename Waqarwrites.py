import os
try:import httpx
except:os.system('pip install httpx > /dev/null')
try:import requests
except:os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('xdg-open https://whatsapp.com/channel/0029VbByxsO1dAwCpYtLJ71Z')
os.system('git pull')
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
  os.system('chmod 777 New;./New')
else:
  exit(' Sorry Device Not Support ')
