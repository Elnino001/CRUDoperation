from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.views.generic import ListView, DateDetailView, UpdateView, CreateView

# Create your views here.
# def employee_list(request):
#     context = {'employee_list': Employee.objects.all()}
#     return render(request, 'employerR/employee_list.html', context)

class EmployeeList(ListView):
    context_object_name = 'employee_list'
    template_name = 'employerR/employee_list.html'

    def get_queryset(self):
        return Employee.objects.all()


class CreateEmployee(CreateView):
    fields = ('fullname','mobile', 'pmp_code', 'position')
    model = Employee
# def employee_form(request, id=0):
#     #if the id is not zero, the request will be a get request
#     if request.method == "GET":
#         if id ==0:#since di==0, we have an insert operation
#             form = EmployeeForm()
#         else:#update operation
#             employee = Employee.objects.get(pk=id)
#             form = EmployeeForm(instance=employee)
#         context = {
#             'form': form
#         }
#         return render(request, 'employerR/employee_form.html', context)
#     else:
#         if id == 0:
#             form = EmployeeForm(request.POST)
#         else:
#             employee = Employee.objects.get(pk=id)
#             form = EmployeeForm(request.POST, instance=employee)
#         if form.is_valid():
#              form.save()
#              return redirect('/list')
class Employee_Form(UpdateView):
    fields = ('fullname','mobile', 'pmp_code', 'position')
    model = Employee

def employee_delete(request):
    return