# Python program for writing
# to file


f = open('C:/cal.txt', 'w')

# Data to be written
data = '10\n 20'

# Writing to file
f.write(data)

# Closing file
f.close()
