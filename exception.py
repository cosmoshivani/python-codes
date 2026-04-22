#error and exception handling

try:
    f = open('testfile', 'r')
    f.write("Write a test line")
except:
    print('All other exceptions!')
finally:
    print("I always run!")
