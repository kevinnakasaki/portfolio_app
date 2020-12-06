from django.test import TestCase
from django.urls import reverse

from .models import Project


class ProjectTests(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Projeto Teste 01",
            description="Projeto de teste"
        )


    def test_project_listing(self):
        self.assertEqual(f'{self.project.title}', "Projeto Teste 01")
        self.assertEqual(f'{self.project.description}', "Projeto de teste")


    def test_project_list_view(self):
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Projeto Teste 01")
        self.assertTemplateUsed(response, "home.html")


    def test_project_detail_view(self):
        response = self.client.get(self.project.get_absolute_url())
        no_response = self.client.get('/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Projeto Teste 01")
        self.assertTemplateUsed(response, "project_detail.html")
