from get_useragents import useragents

# you can change the limit
ua = useragents.UserAgents(limit=500)

# function to get all ua as per limit from GetListUserAgents
user_agents = ua.GetUserAgents()
# function for get random ua from GetListUserAgents
random_ua = ua.RandomUserAgents()

print(random_ua)