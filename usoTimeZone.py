import pytz
from datetime import datetime

tz = pytz.timezone('Europe/Madrid')
dt = datetime.now(tz)
print(dt)
