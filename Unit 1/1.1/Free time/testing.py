import requests as req

api = "https://api.wynncraft.com/public_api.php?action=onlinePlayers"
data = req.get(api).json()
print(data)