from get_useragents import useragents

# you can change the limit
ua = useragents.UserAgents(limit=500)

user_agents = ua.GetUserAgents()
random_ua = ua.RandomUserAgents()

print(random_ua)