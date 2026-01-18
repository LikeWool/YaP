import configuration
import requests
import data
#
def get_track(body):
    return requests.post(configuration.url + configuration.order,
                         json=body,
                         headers=data.headers)

def get_order_by_track(track):
    return requests.get(configuration.url + configuration.track + "?t=" + f"{track}",
                         headers=data.headers)
response= get_track(data.order_body)
print(response.status_code)
print(response.json())