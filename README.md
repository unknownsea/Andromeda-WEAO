# Andromeda-WEAO 🌌
Andromeda-WEAO is a python package that allows you to access WhatExploitsAreOnline easier if you want to integrate it into a python project

## Documentation
### Usage (these all return response from api)
```py
from andromeda_weao import Client; client = Client()

client._get_current_version()
client._get_future_version()
client._get_current_android_version()
client._get_exploit_statuses()
client._get_exploit_status("synapse z")
```
**The names explain it fully, I will probably not put this on pypi for it to be a downloadable package so just download the folder from this repo**
