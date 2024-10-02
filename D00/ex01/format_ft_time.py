import time
import datetime

#objet time et datetime avec le meme time stamp
time_stamp = time.time() #temps ecoule depuis le 1er janvier 1970 
datetime_objet= datetime.datetime.fromtimestamp(time_stamp) #date equivalente a ce timestamp 

#output
print(f"Seconds since January 1, 1970: {time_stamp:,.4f} or {time_stamp:.2e} in scientific notation")
print(f"{datetime_objet.strftime('%b %d %Y')}")