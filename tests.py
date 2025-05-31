import unittest
from main import app

class FaultAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_fault(self):
        response = self.client.post('/api/faults/', json={
            "student_id": 1,
            "description": "Test fault",
            "date_reported": "2025-05-30",
            "resolved": False
        })
        self.assertEqual(response.status_code, 201)

    def test_get_faults(self):
        response = self.client.get('/api/faults/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_update_invalid_fault(self):
        response = self.client.put('/api/faults/9999', json={
            "resolved": True
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_invalid_fault(self):
        response = self.client.delete('/api/faults/9999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
