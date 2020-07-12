import unittest
import app
import json

class BasicTest(unittest.TestCase):
    def setUp(self):
        app.app.config['TESTING'] = True
        app.app.config['WTF_CSRF_ENABLED'] = False
        app.app.config['DEBUG'] = False
        self.app = app.app.test_client()
    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code,200)
    
    def test_status_web3(self):
        response = self.app.get('/web3/status')
        data = response.get_json()
        self.assertEqual(data['aktif'],True)
    
    def test_create_account(self):
        response = self.app.post('/web3/create/account',json={
            'password':'yafiabiyyu'
        })
        self.assertEqual(response.status_code,200)
    
    def test_send_ether(self):
        response = self.app.post('/web3/send/ether',json={
            'address_to':'0xd8175A41e257e0705A1D1089DDF6A060904c3090',
            'amount':float(0.002)
        })
        self.assertEqual(response.status_code,200)

if __name__ == "__main__":
    unittest.main()