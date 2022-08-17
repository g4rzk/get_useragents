## GET-USERAGENTS

This library is used to make it easier for developers or users to get random user agents from [https://useragents.io.](https://useragents.io)

### Installation
You can install get-useragents by running the following command:
```
pip install get-useragents
```
Or you can download direct from [Github](https://github.com/g4rzk/get_useragents/archive/get_useragents.tar.gz) and install it manually.

### Usage
```python
from get_useragents import *

# you can change the limit
ua = UserAgents(limit=100)

# fungsi untuk mendapatkan semua ua sesuai limit dari GetListUserAgents
user_agents = ua.GetUserAgents()
# function for get random ua from GetListUserAgents
random_ua = ua.RandomUserAgents()

print(random_ua)
```

### Function
1. Get more than 100+ user agents 
2. Get a random user agent

### License
The MIT License (MIT). Please see [License File](https://github.com/g4rzk/get_useragents/blob/main/LICENSE) for more information.

## User Agent Source
special thanks to [useragents.io](https://useragents.io) for providing real user agents.