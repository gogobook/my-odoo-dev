from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.
from django.shortcuts import render
import logging
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Task
# Create your views here.

@csrf_exempt
def create_project(request):
    # 這裡要新增一個判斷，只特定位址來的資料才會進資料庫
    if request.POST:
        logging.warning(request.POST)
        order_id = request.POST.get('order_id')
        partner_id = request.POST.get('partner_id')
        email = request.POST.get('email_from')
        name = request.POST.get('name')
        data_of_manufacture = date.today() # TODO: NOT NULL constraint failed: project_project.data_of_manufacture
        data = locals()
        del data["request"]
        Task.objects.create(**data) 
        return HttpResponse("1|ok")
    else:
        return HttpResponse("Hello, world. You're at the polls index.")

@login_required
def upload_files(request, name):
    '這裡處理上傳功能'
    if request.method == 'GET':
        pass

@login_required
def index(request):
    '在這個頁面可查詢可以上傳檔案的專案'
    if request.method == 'GET':
        pass

@login_required(login_url='/app/accounts/login/')
def tasks_list(request):
    groups_list = request.user.odoo_groups.split(',')
    email = request.user.username
    check_task = Task.objects.filter(email_from=email).exists()
    logging.warning(groups_list)
    if '1' in groups_list:
        tasks_list = request.user.odoo_tasks
        tasks_list = Task.objects.filter(task_is__in=tasks_list)
        return HttpResponse(tasks_list)
    elif check_task:
        tasks_list = Task.objects.filter(email_from=email)
        return HttpResponse(tasks_list)
    else:
        return HttpResponse('No task')
    # staff_queryset = Project.object.filter()
    # if project_queryset.count() >= 1:
        # return render('project_list.html',{'list':project_queryset})
    # return HttpResponse()

    # elif staff_queryset.count() >=1:
        # return HttpResponse(odoo_env.uid)