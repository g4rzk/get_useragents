## GET-USERAGENTS

This library is used to make it easier for developers or users to get random user agents

### Installation
You can install get-useragents by running the following command:
```
pip install get-useragents
```
Or you can download direct from [Github](https://github.com/g4rzk/get_useragents/archive/get_useragents.tar.gz) and install it manually.

### Upgrade packages
You can upgrade get-useragents by running the following command:
```
pip install get-useragents --upgrade
```

### Usage
```python
from get_useragents import useragents

# to see available devices, check: https://github.com/g4rzk/get_useragents#list-device
ua = useragents.Get_UA(device="chrome")

# to get all user agents according to the limit
all_ua = ua.GetUserAgents()
# to get a random user agent from limit
random_ua = ua.RandomUserAgents()

print(random_ua)
```

### List Device
| List Device  | Total User Agent |
| ----- | --- |
| Apple   | 500+  |
| Chrome | 500+  |
| Desktop   | 500+  |
| Facebook | 500+  |
| iOS   | 500+  |
| iPhone | 500+  |
| Linux   | 500+  |
| MiUi | 500+  |
| Mozilla   | 500+  |
| Opera | 500+  |
| Samsung   | 500+  |
| Xiaomi | 500  |
| Yandex   | 500+  |
| Mac OS | 500+  |

### Function
1. Get 100+ user agent from existing devices
2. Get a random user agent from all existing devices

### List All Directory
```
.get_useragents
├── AUTHORS
├── LICENSE
├── README.md
├── cache
│   └── dump
│       └── get_useragents.json
├── example
│   └── testing
│       └── ua.py
├── get_useragents
│   ├── data
│   │   └── get_useragents.json
│   ├── settings.py
│   └── useragents.py
├── setup.cfg
├── setup.py
└── ua.py
```
This tree is to make it easier for you to see the files in all directories. 

### Change Log
- **Version 1.6 and 1.7 2022/11/29 18:22**
  - Fix Error
  - Done Test All Function
  - BETA

- **Version 1.1 to 1.5 2022/11/28 22:01:49**
  - Fast Get User Agents
  - Add New List Device
  - Simple Method
  - No Need Installed Module
  - BETA

- **Version 0.8**
  - New list device user agent
  - Fixed Bug and Re-Upload

- **Version 0.7**
  - Using cloudscraper
  - Re-upload

- **Version 0.6**
  - Fix Index Error
  - Re-upload

### Stats
[![Downloads](https://static.pepy.tech/personalized-badge/get-useragents?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/get-useragents)

### License
The MIT License (MIT). Please see [License File](https://github.com/g4rzk/get_useragents/blob/main/LICENSE) for more information.

## Authors
You can visit [authors page](https://github.com/g4rzk/get_useragents/blob/main/AUTHORS) 
