
pcs = ["10.203.10.1", "10.203.10.2"]

# enumerate start at 0 by default. 
# You can change it to start=1 if you want to count from 1.
for i, ip in enumerate(pcs):
    print("All the IP's are " + ip)
    # You must wrap numbers in str() to combine them with text
    print("current num is " + str(i))
name = "gosho"

print(f"Hello bate {name}")
