import requests
import json


class TableEventHandler:
    def __init__(self):
        self.url = 'https://gu0nyc6yrg.execute-api.us-east-1.amazonaws.com/dev'

    def GetIdRuns(self, key):
        result = []
        response = requests.get(self.url + '/todos/' + key)
        if response.status_code == 200:
            response_content = json.loads(response.content.decode())
            result = [item['run'] for item in response_content]
        return result
