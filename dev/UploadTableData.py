import requests
import json
import os


class DataUploadToDynamoDB:
    def __init__(self, filename):
        os.chdir('..')
        self.__filename = filename
        self.__tabledata = []
        self.url = 'https://gu0nyc6yrg.execute-api.us-east-1.amazonaws.com/dev'

    def __ScanDataFile(self):
        f = open(os.getcwd() + '/data/' + self.__filename)
        if f:
            data = f.read()
            lines = data.split('\n')
            for i in range(len(lines)):
                self.__tabledata.append(lines[i].split(' \\ '))

    def UploadDataToTable(self):
        self.__ScanDataFile()
        for entry in self.__tabledata:
            response = self.CreateDataEntry(entry[0], entry[1])
            print('key: ' + entry[0] + ' | value: ' + entry[1])

    def CreateDataEntry(self, key, value):
        data = {'id': key, 'run': value}
        response = requests.post(self.url + '/todos', data=json.dumps(data))
        return response
