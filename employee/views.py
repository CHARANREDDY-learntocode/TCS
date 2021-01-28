from django.views.generic import ListView, DetailView, View
from .models import Employee
from django.shortcuts import get_object_or_404


class EmployeeListView(ListView):
	model = Employee
	template_name = 'employee_list.html'
	context_object_name = 'employees'


class EmployeeDetailView(DetailView):
	model = Employee
	template_name = 'employee_detail.html'
	context_object_name = 'employee'


class EmployeeDetailAPIView(DetailView):
	model = Employee
	template_name = 'employee_api_detail.html'
	context_object_name = 'employee'

