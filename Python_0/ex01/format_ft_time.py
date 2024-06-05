from datetime import datetime

current_date = datetime.now()
timestamp = datetime.timestamp(current_date)
#timestamp represents the number of seconds that have elapsed since the Unix epoch (January 1, 1970, at 00:00:00 UTC).

print(f"Seconds since January 1, 1970: {timestamp:,} or {timestamp:.2e} in scientific notation")
print(current_date.strftime("%b %d %Y"))
