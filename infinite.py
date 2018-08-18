from time import sleep
a = raw_input("enter a value less than 10")
a = int(a)
while a<=20:
    print a
    if a == 10:
      print "continue executed"
      sleep(5)
      continue
    a += 1
    print "continue not executed"
print "outside while"