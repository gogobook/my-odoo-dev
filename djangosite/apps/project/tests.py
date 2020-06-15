from django.test import TestCase, RequestFactory, Client
from django.contrib import auth
# from .views import create_project
from project.models import Project
import logging
# Create your tests here.

class CreateProjectTest(TestCase):
    
    def test_create_project(self):
        c = Client()
        data = {
            "name": ["S00026: 網站設計"],
            "planned_hours": ["1.0"],
            "partner_id": ["35"],
            "email_from": ["addison.olson28@example.com"],
            "description": [""],
            "project_id": ["2"],
            "sale_line_id": ["55"],
            "company_id": ["1"],
            "user_id": ["False"],
            "message_follower_ids": [
                "0",
                "0",
                "{'res_model': 'project.task', 'partner_id': 3, 'subtype_ids': [(6, 0, [1, 8])]}"
            ],
            "order_id": ["S00026"]
        }
        before_create = Project.objects.all().count()
        rsp = c.post('/project/create_project', data)
        after_create = Project.objects.all().count()
        obj = Project.objects.all()[0]
        logging.warning(obj.__dict__)

        self.assertIs(rsp.status_code, 200)
        self.assertIs(after_create-before_create,1)
        self.assertEqual(obj.order_id, 'S00026')

class LoginTest(TestCase):
    def setUp(self):
        self.user = auth.authenticate(username='demo', password='demo')
        self.factory = RequestFactory()

    def test_login(self):
        self.assertIs(self.user.odoo_env.uid, 6)
