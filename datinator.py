#!/usr/bin/env python3
from datetime import date, timedelta

print("Start Date")
sm = int(input("Start Month: "))
sd = int(input("Start Day: "))
sy = int(input("Start Year: "))
start = date(sy, sm, sd)

print("End Date")
em = int(input("End Month: "))
ed = int(input("End Day: "))
ey = int(input("Start Year: "))
end = date(ey, em, ed)

print("Monday=0, Sunday=6")
days = eval("[" + input("Days: ") + "]") 

delta = timedelta(days=1)

d = start
while d <= end:
  if d.weekday() in days:
    print(d.strftime("%a %B %e"))
  d += delta
