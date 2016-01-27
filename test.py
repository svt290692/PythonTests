import os



try:
    print str(var)
    print "sure, it was defined."
except:
  print "well, it WASN'T defined after all!"

if(os.getenv("PATH") == "yes"):
    print "no"
else:
    print "yes"

hello = "hello"
hello = hello.upper()
print hello