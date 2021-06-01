#!/usr/bin/python3

import requests
import json

def get_subscriber_count(channel_id):
    part = "statistics"
    key= "AIzaSyBr9Zl8yA1l4qXKg9MayoYb__NlrtIt7no"

    request="https://www.googleapis.com/youtube/v3/channels?part=" + part + \
            "&id=" + channel_id + "&key=" + key

    #print("Requesting " + request)

    response = requests.get(request)
    data = json.loads(response.content)

    return data["items"][0]["statistics"] ["subscriberCount"]





