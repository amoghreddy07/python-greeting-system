import time

timestamp = time.strftime('%H:%M:%S')#%H - Hour (24-hour clock) as a zero-padded decimal number.
print(timestamp)
timestamp = time.strftime('%H')#%H - Hour (24-hour clock) as a zero-padded decimal number.
print(timestamp)
timestamp = time.strftime('%M')#%M - Minute as a zero-padded decimal number.
print(timestamp)
timestamp = time.strftime('%S')#%S - Second as a zero-padded decimal number.
print(timestamp)

hour = int(time.strftime('%H'))
if hour < 12:
    print("Good Morning ☀️")
elif hour < 16:
    print("Good Afternoon 🌤️")
elif hour < 20:
    print("Good Evening 🌆")
else:
    print("Good Night 🌙")