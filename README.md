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
from get_useragents import useragents 

# you can change the limit
ua = useragents.UserAgents(limit=500)

# function to get all ua as per limit from GetListUserAgents
user_agents = ua.GetUserAgents()
# function for get random ua from GetListUserAgents
random_ua = ua.RandomUserAgents()

print(random_ua)
```

### Function
1. Get more than 100+ user agents 
2. Get a random user agent

### List All Directory
```
.get_useragents
├── LICENSE
├── README.md                                                   
├── cache                                                       
│   ├── browser.txt
│   └── useragents.txt                                          
├── example                                                     
│   └── test.py
├── get_useragents                                            
│   ├── __init__.py
│   ├── settings.py
│   └── useragents.py                                           
├── setup.cfg
├── setup.py                                                    
└── ua.py
```
This tree is to make it easier for you to see the files in all directories. 

### Change Log
- **Version 0.6**
  - Fix Index Error
  - Re-upload

- **Version 0.7**
  - Using cloudscraper (tested)
  - Re-upload

### Stats
[![Downloads](https://static.pepy.tech/personalized-badge/get-useragents?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/get-useragents)

### License
The MIT License (MIT). Please see [License File](https://github.com/g4rzk/get_useragents/blob/main/LICENSE) for more information.

### User Agent Source
special thanks to [useragents.io](https://useragents.io) for providing real user agents.