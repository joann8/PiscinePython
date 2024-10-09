import time
import datetime

# objet time et datetime avec le meme time stamp
# --> temps ecoule depuis le 1er janvier 1970
time_stamp = time.time()
# ---> date equivalente a ce timestamp
datetime_objet = datetime.datetime.fromtimestamp(time_stamp)

# output
print(f"Seconds since January 1, 1970: {time_stamp:,.4f} or {time_stamp:.2e} in scientific notation")
print(f"{datetime_objet.strftime('%b %d %Y')}")
