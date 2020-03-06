from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateEmployee.as_view(), name='employee_insert'),
     path('<int:pk>/', views.Employee_Form.as_view(), name='employee_update'),
    path('list/<int:pk>', views.EmployeeList.as_view(), name='employee_list')
]