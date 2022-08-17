from get_useragents import *

# you can change the limit
ua = UserAgents(limit=100)

# fungsi untuk mendapatkan semua ua sesuai limit dari GetListUserAgents
user_agents = ua.GetUserAgents()
# function for get random ua from GetListUserAgents
random_ua = ua.RandomUserAgents()

print(random_ua)
