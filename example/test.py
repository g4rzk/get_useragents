from get_useragents import useragents

# you can change string limit '100' to max limit which is '1000'
# to see available devices, check: https://github.com/g4rzk/get_useragents#list-device
ua = useragents.Get_UA(device="chrome", limit=100)

# to get all user agents according to the limit
all_ua = ua.GetUserAgents()
# to get a random user agent from limit
random_ua = ua.RandomUserAgents()

print(random_ua)