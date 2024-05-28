from datetime import datetime

current_date = datetime.now()
timestamp = datetime.timestamp(current_date)

print(f"Seconds since January 1, 1970: {timestamp:,} or {timestamp:.2e} in scientific notation")
print(current_date.strftime("%b %d %Y"))
