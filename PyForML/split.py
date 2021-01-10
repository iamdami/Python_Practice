# Split string by space 
items = 'zero one two three'.split() 
print(items) 


# Split string by ","
example = 'python,jquery,javascript' 
print(example.split(",")) 


# Unpacking each value of list into a, b, c, variable 
example = 'python,jquery,javascript' 
a, b, c = example.split(",") 


# Split string by "." and unpacking 
example = 'damio.tistory.com' 
subdomain, domain, tld = example.split(".")
