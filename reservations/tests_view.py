import unittest
from django.test import Client, TestCase
from datetime import date
from .models import Date, Reservation, Review



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.comment = Review.objects.create(body='Test comment')

    def test_get_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        
    def test_get_book_page(self):
        response = self.client.get('/reservations')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_sho_dates_get(self):
        response = self.client.get('/reservations')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('dates', response.context)
        self.assertIn('reservations', response.context)
        self.assertIn('today', response.context)

    def test_sho_dates_post_valid_data(self):
        responsee = self.client.get('/reservations')
        data = {
            'reservation_date': '2023-05-18',
            'Table': '1',
            'name': 'John',
            'email': 'john@example.com',
            'phone': '123456789',
            'comment': 'Test comment'
        }
        response = self.client.post('/reservations', data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(), 1)
        self.assertEqual(Date.objects.count(), 1)
        self.assertRedirects(response, '/')

    def test_sho_dates_post_invalid_data(self):
        responsee = self.client.get('/reservations')
        data = {
            'reservation_date': '2023-05-18',
            'Table': '1',
            'name': '',
            'email': 'john@example.com',
            'phone': '123456789',
            'comment': 'Test comment'
        }
        response = self.client.post('/reservations', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_comments_post_valid_data(self):
        data = {
            'comment': 'Test comment'
        }
        response = self.client.post('', data=data)
        self.assertEqual(response.status_code, 200)
        
    def test_delete_comment(self):
        comment_id = self.comment.id
        url = f'/delete_comment/{comment_id}'  # Replace with your actual URL pattern
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Adjust the expected status code based on your application's behavior
        self.assertEqual(Review.objects.filter(id=comment_id).exists(), False)
        # Additional assertions can be added to check the behavior after deleting the comment.

if __name__ == '__main__':
    unittest.main()