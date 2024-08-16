import time
timestemp = time.strftime('%H:%M:%S')
print(timestemp)
hour = time.strftime('%H')
minute = time.strftime('%M')
second = time.strftime('%S')
if (hour >= '00' and minute >= '00' and second >= '00' and hour <= '11' and minute <= '59' and second <= '59'):
  print("Good Morning")
elif (hour >= '12' and minute >= '00' and second >= '00' and hour <= '15' and minute <= '59' and second <= '59'):
  print("Good Afternoon")
elif (hour >= '16' and minute >= '00' and second >= '00' and hour <= '20' and minute <= '59' and second <= '59'):
  print("Good Evening")
else:
  print("Good Night")
