from django.test import TestCase
from .models import Employee


class EmployeeModelTest(TestCase):

    def test_create_employee(self):
        emp = Employee.objects.create(
            full_name='ทดสอบ ระบบ',
            email='test@test.com',
            position='Staff',
            phone='0812345678',
        )
        self.assertEqual(str(emp), 'ทดสอบ ระบบ (Staff)')

    def test_employee_position_choices(self):
        choices = [c[0] for c in Employee.POSITION_CHOICES]
        self.assertIn('Manager', choices)
        self.assertIn('Staff', choices)
