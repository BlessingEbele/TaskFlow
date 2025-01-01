from django.test import TestCase

# Create your tests here.
# from rest_framework.test import APITestCase, APIClient
# from rest_framework import status
# from django.contrib.auth.models import User
# from tasks.models import Task
# from django.utils.timezone import now

# class TaskEndpointTests(APITestCase):
#     def setUp(self):
#         # Create a user and authenticate
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.client = APIClient()
#         self.client.login(username='testuser', password='testpassword')

#         # Create sample task
#         self.task = Task.objects.create(
#             title="Sample Task",
#             description="This is a test task",
#             due_date=now().date(),
#             priority="medium",
#             status="pending",
#             owner=self.user,
#         )
#         self.task_url = f"/tasks/{self.task.id}/"

#     def test_create_task(self):
#         data = {
#             "title": "New Task",
#             "description": "Test task creation",
#             "due_date": now().date(),
#             "priority": "high",
#             "status": "pending"
#         }
#         response = self.client.post("/tasks/", data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data["title"], "New Task")

#     def test_list_tasks(self):
#         response = self.client.get("/tasks/")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)  # One task created in setUp

#     def test_retrieve_task(self):
#         response = self.client.get(self.task_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["title"], self.task.title)

#     def test_update_task(self):
#         data = {"title": "Updated Task Title"}
#         response = self.client.put(self.task_url, data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["title"], "Updated Task Title")

#     def test_delete_task(self):
#         response = self.client.delete(self.task_url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Task.objects.filter(id=self.task.id).exists())

#     def test_mark_task_complete(self):
#         response = self.client.post(f"/tasks/{self.task.id}/mark-complete/")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.task.refresh_from_db()
#         self.assertEqual(self.task.status, "completed")

#     def test_mark_task_incomplete(self):
#         self.task.status = "completed"
#         self.task.save()
#         response = self.client.post(f"/tasks/{self.task.id}/mark-incomplete/")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.task.refresh_from_db()
#         self.assertEqual(self.task.status, "pending")
