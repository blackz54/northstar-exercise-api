import unittest
import requests
import json


class APIEndpointTestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'https://gu0nyc6yrg.execute-api.us-east-1.amazonaws.com/dev'



    def test_create_success(self):
        data = {'id': 'Advanced', 'run': 'Backdoor'}
        result = requests.post(self.url + '/todos', data=json.dumps(data))
        self.assertEqual(result.status_code, 200)

    def test_get_success(self):
        result = requests.get(self.url + '/todos/Advanced/Backdoor')
        self.assertEqual(result.status_code, 200)

    def test_get_fail(self):
        result = requests.get(self.url + '/todos/User-Does-Not-Exist/DNE')
        self.assertEqual(result.status_code, 502)

    def test_list_success(self):
        result = requests.get(self.url + '/todos')
        self.assertEqual(result.status_code, 200)

    def test_update(self):
        data = {'id': 'Advanced', 'run': 'Frontdoor'}
        result = requests.put(self.url + '/todos/Advanced/Backdoor', data)
        self.assertEqual(result.status_code, 200)
    def test_delete_success(self):
        id = 'NEW-USER-1234'
        run = '/challenger/'
        data = {'id': 'NEW-USER-1234', 'run': 'challenger'}
        create_result = requests.post(self.url + '/todos', data=json.dumps(data))
        delete_result = requests.delete(self.url + '/todos/' + id + run,
                                        data=json.dumps(data))
        self.assertEqual(create_result.status_code, 200)
        self.assertEqual(delete_result.status_code, 200)

    def test_ids_unique_run_creation(self):
        id = 'USER-SUB-1234'
        run1 = '/copenhaggen/'
        run2 = '/powderbowl/'
        data1 = {'id': 'USER-SUB-1234', 'run': 'copenhaggen'}
        data2 = {'id': 'USER-SUB-1234', 'run': 'powderbowl'}
        delete_result1 = requests.delete(self.url + '/todos/' + id + run1,
                                         data=json.dumps(data1))
        self.assertEqual(delete_result1.status_code, 200)
        create_result1 = requests.post(self.url + '/todos', data=json.dumps(data1))
        create_result2 = requests.post(self.url + '/todos', data=json.dumps(data2))
        delete_result1 = requests.delete(self.url + '/todos/' + id + run1,
                                         data=json.dumps(data1))
        delete_result2 = requests.delete(self.url + '/todos/' + id + run2,
                                         data=json.dumps(data2))

        self.assertEqual(delete_result1.status_code, 200)
        self.assertEqual(create_result1.status_code, 200)
        self.assertEqual(create_result2.status_code, 200)
        self.assertEqual(delete_result1.status_code, 200)
        self.assertEqual(delete_result2.status_code, 200)

    def test_get_id_runs(self):
        data1 = {'id': 'USER-SUB-1234', 'run': 'copenhaggen'}
        data2 = {'id': 'USER-SUB-1234', 'run': 'powderbowl'}
        data3 = {'id': 'ANOTHER-SUB-1234', 'run': 'challenger'}
        create_result1 = requests.post(self.url + '/todos', data=json.dumps(data1))
        create_result2 = requests.post(self.url + '/todos', data=json.dumps(data2))
        create_result3 = requests.post(self.url + '/todos', data=json.dumps(data3))
        result = requests.get(self.url + '/todos/' + 'USER-SUB-1234')
        del_result = requests.delete(self.url + '/todos/' + 'ANOTHER-SUB-1234/' + 'challenger',
                                     data=data3)
        self.assertEqual(create_result1.status_code, 200)
        self.assertEqual(create_result2.status_code, 200)
        self.assertEqual(create_result3.status_code, 200)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(del_result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
