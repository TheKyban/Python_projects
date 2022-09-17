import requests

USERNAME = "kyban"
TOKEN = "jdsfasdiendjskljfa3242zn"
GRAPH_ID = "graph1"
DATE = "20220824"
QUANTITY = "5.0"

pixela_endpoint = "https://pixe.la/v1/users"
Graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
check_graphs = "https://pixe.la/v1/users/kyban/graphs/graph1.html"

headers = {
    "X-USER-TOKEN": TOKEN
}

# for account Creation______________________
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# _________________________________________

# for graph creation************************
graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
# ******************************************

# for pixel creation------------------------
pixel_creation_params = {
    "date": DATE,
    "quantity": QUANTITY
}
# ------------------------------------------

# for update pixel>>>>>>>>>>>>>>>>>>>>>>>>>>
pixel_update_params = {
    "quantity": QUANTITY
}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# POST
# account = requests.post(url=pixela_endpoint, json=user_params)
# print(account.text)
# response = requests.post(url=Graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# post_pixel = requests.post(url=pixel_creation_endpoint, json=pixel_creation_params, headers=headers)
# print(post_pixel.text)

# pixel_update = requests.put(url=pixel_update_endpoint, headers=headers, json=pixel_update_params)
# print(pixel_update.text)

pixel_delete = requests.delete(url=pixel_update_endpoint, headers=headers)
print(pixel_delete.text)