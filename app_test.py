# test_app.py
import unittest
from app import app  # Importing the Flask app
from models.models import db

class FlaskAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the testing environment
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
        app.config['SECRET_KEY'] = '1q2w3e4r'
        app.config['SESSION_PERMANENT'] = False
        cls.client = app.test_client()
        with app.app_context():
            db.create_all()  # Create tables in the test database

    # @classmethod
    # def tearDownClass(cls):
    #     # Clean up the database after all tests
    #     with app.app_context():
    #         db.drop_all()

    def test_home_redirects_if_not_logged_in(self):
        # Test that the home page redirects to login if user not signed in.
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'signin', response.data)

    def test_signin_invalid_credentials(self):
        # Test that invalid login credentials return an error.
        response = self.client.post('/signin', data={
            'email': 'fakeuser@test.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid Credentials', response.data)

    def test_signup_existing_user(self):
        # Test that trying to sign up with an existing user returns an error.
        response = self.client.post('/signup', data={
            'emailSignup': 'testuser@example.com',
            'passwordSignup': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error when signing up', response.data)

    def test_add_new_patient_redirects_if_not_logged_in(self):
        # Test add new patient redirects to login if user not signed in.
        response = self.client.post('/add_new_patient_clicked', data={
            'genderOptions': 'Male',
            'age': '30',
            'hypertensionOptions': '0',
            'heartDiseaseOptions': '0',
            'everMarriedOptions': '1',
            'workTypeOptions': 'Private',
            'residence_type': '1',
            'avg_glucose_level': '120.5',
            'bmi': '24.5',
            'smoking_status': 'never smoked',
            'strokeOptions': '0'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to login

if __name__ == "__main__":
    unittest.main()
