import unittest
from main import create_app
from config import TestConfig
from exts import db


# create a unit class test case
# test case class inherits from unittest.Testcase

class APITestCase(unittest.TestCase):
    def setUp(self): #setup function helps declare variables to be used during test
        self.app=create_app(TestConfig)
        # test client is an interface that allows for application testing

        self.client=self.app.test_client(self)

        with self.app.app_context():
            # db.init_app(self.app)

            db.create_all()


    # test cases
    # def test_hello_world(self):
    #     hello_response=self.client.get('recipes/hello')

    #     json=hello_response.json
    #     # print(json)
    #     self.assertEqual(json, {"message": "Hello World"})

    
    def test_signup(self):
        signup_response=self.client.post('/auth/signup',
            json={
                "username": "testuser",
                "email": "testuser@test.com",
                "password":"password"
            }
        )
        status_code=signup_response.status_code
        self.assertEqual(status_code, 201)

    def test_login(self):
        signup_response=self.client.post('/auth/signup',
            json={
                "username": "testuser",
                "email": "testuser@test.com",
                "password":"password"
            }
        )

        login_response=self.client.post('/auth/login',
            json={
                "username":"testuser",
                "password": "password"
            }
        )

        status_code=login_response.status_code

        json=login_response.json

        # print(json)

        self.assertEqual(status_code, 200)


    # test the get_all_recipes api
    def test_get_all_recipes(self):
        """TEST TO GET ALL RECIPES"""
        response = self.client.get('/recipes/recipes')

        # print(response.json)

        status_code = response.status_code

        self.assertEqual(status_code, 200)


    def test_get_one_recipe(self):
        id = 1
        response = self.client.get(f'/recipes/recipe/{id}')
        status_code = response.status_code

        self.assertEqual(status_code, 404)


    # test the create recipe route
    # this test needs the authentication
    def test_create_recipe(self):
        signup_response=self.client.post('/auth/signup',
            json={
                "username": "testuser",
                "email": "testuser@test.com",
                "password":"password"
            }
        )

        login_response=self.client.post('/auth/login',
            json={
                "username":"testuser",
                "password": "password"
            }
        )

        access_token = (login_response.json["access_token"])

        create_recipe_response = self.client.post('/recipes/recipes',
            json = {
                "title": "Test Cookie", 
                "description": "Test Description"
            }, 
            headers = {
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = create_recipe_response.status_code

        self.assertEqual(status_code, 201)


    #test the update recipe route
    #Needs authentication to update
    def test_update_recipe(self):
        signup_response=self.client.post('/auth/signup',
            json={
                "username": "testuser",
                "email": "testuser@test.com",
                "password":"password"
            }
        )

        login_response=self.client.post('/auth/login',
            json={
                "username":"testuser",
                "password": "password"
            }
        )

        access_token = (login_response.json["access_token"])

        create_recipe_response = self.client.post('/recipes/recipes',
            json = {
                "title": "Test Cookie", 
                "description": "Test Description"
            }, 
            headers = {
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = create_recipe_response.status_code
        # After creating the recipe, you need to fetch (get) it to update it.
        id=1
        # get_one = self.client.get(f'/recipes/recipe/{id}')

        update_response = self.client.put(f'/recipes/recipe/{id}',
            json = {
                "title": "Test Cookie updated",
                "description": "Test Description updated"
            },
            headers = {
                "Authorization": f"Bearer {access_token}"
            }


        )

        # print(update_response.json)

        status_code = update_response.status_code
        self.assertEqual(status_code, 200)


    def test_delete_recipe(self):
        signup_response=self.client.post('/auth/signup',
            json={
                "username": "testuser",
                "email": "testuser@test.com",
                "password":"password"
            }
        )

        login_response=self.client.post('/auth/login',
            json={
                "username":"testuser",
                "password": "password"
            }
        )

        access_token = (login_response.json["access_token"])

        create_recipe_response = self.client.post('/recipes/recipes',
            json = {
                "title": "Test Cookie", 
                "description": "Test Description"
            }, 
            headers = {
                "Authorization": f"Bearer {access_token}"
            }
        )

        id=1

        delete_response = self.client.delete(
            f'recipes/recipe/{id}',
            headers = {
                "Authorization": f"Bearer {access_token}"
            }
        )

        status_code = delete_response.status_code

        self.assertEqual(status_code, 200)



    # helps us destroy the variables created in our test environment
    def tearDown(self):
        with self.app.app_context():
            db.session.remove() #remove all the sessions

            db.drop_all() # then drop all the table


# test runner
if __name__ == '__main__':
    unittest.main()