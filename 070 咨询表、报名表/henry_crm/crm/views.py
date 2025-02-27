import hashlib

from django.db.models import F, Q
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views import View

from crm import models
from crm.forms import RegForm, CustomerForm, ConsultRecord, EnrollmentForm
from utils.pagenation import Pagenation


def reg(request):
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            obj = form_obj.save()
            models.Department.objects.filter(pk=obj.department.pk).update(count=F('count') + 1)
            return redirect(reverse('login'))
    return render(request, 'reg.html', {'form_obj': form_obj})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md = hashlib.md5(b'sajdfkh')
        md.update(password.encode('utf-8'))
        md.hexdigest()
        obj = models.UserProfile.objects.filter(username=username, password=md.hexdigest(), is_active=True).first()
        if obj:
            url = request.GET.get('return_url')
            if url: ret = redirect(url)
            ret = redirect('customer')
            request.session['user_id'] = obj.pk
            request.session['is_login'] = True
            return ret
        return render(request, 'login.html', {'error': '用户名或密码错误'})
    return render(request, 'login.html')


def logout(request):
    request.session['is_login'] = ''
    ret = redirect('login')
    return ret


def customer_list(request):
    url = request.path
    if request.method == 'GET':
        if url == reverse('customer'):
            all_item = models.Customer.objects.filter(consultant__isnull=True)
        else:
            all_item = models.Customer.objects.filter(consultant_id=request.user_obj.pk)
    else:
        key = request.POST.get('key_words')
        search_url = request.POST.get('search_url')
        if key:
            if search_url == reverse('list_customer'):
                all_item = models.Customer.objects.filter(
                    Q(qq__contains=key) | Q(name__contains=key) | Q(phone__contains=key),
                    Q(consultant=request.user_obj))
            else:
                all_item = models.Customer.objects.filter(
                    Q(qq__contains=key) | Q(name__contains=key) | Q(phone__contains=key), Q(consultant__isnull=True))
        else:
            all_item = []
    obj = Pagenation(request, len(all_item))
    return render(request, 'list_customer.html', {'all_item': all_item[obj.start:obj.end], 'all_page': obj.show})

    # """使用django的分页器"""
    # from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    # items = models.Customer.objects.all()
    # paginator = Paginator(items, 10, orphans=3)
    # page = request.GET.get('page')
    # try:
    #     all_item = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     all_item = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     all_item = paginator.page(paginator.num_pages)
    # return render(request, 'list_customer.html', {'all_item': all_item})


class CustomerList(View):

    def get(self, request):
        q = self.search(['qq', 'name', 'phone'])
        if request.path == reverse('customer'):
            all_item = models.Customer.objects.filter(q, consultant__isnull=True)
        else:
            all_item = models.Customer.objects.filter(q, consultant=request.user_obj)
        obj = Pagenation(request, all_item.count(), request.GET.copy(), 3)
        return render(request, 'list_customer.html', {'all_item': all_item[obj.start:obj.end], 'all_page': obj.show})

    def post(self, request):
        action = request.POST.get('action', '')
        if not hasattr(self, action):
            return HttpResponse('非法操作')
        getattr(self, action)()
        return self.get(request)

    def ctp(self):
        """common to public: 公户转私户"""
        li = self.request.POST.getlist('edit_name')
        models.Customer.objects.filter(pk__in=li).update(consultant=self.request.user_obj)

    def ptc(self):
        """public to common: 私户转公户"""
        li = self.request.POST.getlist('edit_name')
        models.Customer.objects.filter(pk__in=li).update(consultant='')

    def search(self, field_list):
        """根据关键词，进行模糊查询"""
        query = self.request.GET.get('query', '')
        q = Q()
        q.connector = 'OR'
        for i in field_list:
            q.children.append(Q(('{}__contains'.format(i), query)))
        # (OR: (AND: ('qq__contains', '')), (AND: ('name__contains', '')), (AND: ('phone__contains', '')))
        return q


def modify_customer(request, pk=None):
    user_obj = models.Customer.objects.filter(pk=pk).first()
    obj = CustomerForm(instance=user_obj)
    if request.method == 'POST':
        obj = CustomerForm(data=request.POST, instance=user_obj)
        if obj.is_valid():
            obj.save()
            url = request.GET.get('next', '')
            if url:
                return redirect(url)
            else:
                return redirect('list_customer')
    title = '修改客户' if pk else '新增客户'
    return render(request, 'form.html', {'obj': obj, 'title': title})


# 跟进记录
class ConsultRecordList(View):

    def get(self, request, pk=0):
        all_item = models.ConsultRecord.objects.filter(consultant=request.user_obj)
        if pk:
            # if request.path == reverse('consult_record', args=(pk,)):
            all_item = models.ConsultRecord.objects.filter(consultant=request.user_obj, customer_id=pk)
        obj = Pagenation(request, all_item.count(), per_page=3)
        return render(request, 'list_consult.html',
                      {'all_item': all_item[obj.start:obj.end], 'all_page': obj.show, 'customer_id': pk})


# def modify_consult(request, pk=None, customer_id=None):
#     user_obj = models.ConsultRecord.objects.filter(pk=pk).first()
#     obj = ConsultRecord(request, customer_id, instance=user_obj)
#     if request.method == 'POST':
#         obj = ConsultRecord(request, customer_id, data=request.POST, instance=user_obj)
#         if obj.is_valid():
#             obj.save()
#             url = request.GET.get('next', '')
#             return redirect(url if url else 'consult_record')
#     return render(request, 'form.html', {'obj': obj})


def modify_consult(request, pk=None, customer_id=None):
    user_obj = models.ConsultRecord(consultant=request.user_obj,
                                    customer_id=customer_id) if customer_id else models.ConsultRecord.objects.filter(
        pk=pk).first()
    obj = ConsultRecord(instance=user_obj)
    if request.method == 'POST':
        obj = ConsultRecord(data=request.POST, instance=user_obj)
        if obj.is_valid():
            obj.save()
            url = request.GET.get('next', '')
            return redirect(url if url else 'consult_record')
    return render(request, 'form.html', {'obj': obj})


class EnrollmentList(View):

    def get(self, request, customer_id=None):
        if not customer_id:
            all_item = models.Enrollment.objects.filter(customer__in=request.user_obj.customers.all())
        else:
            all_item = models.Enrollment.objects.filter(customer_id=customer_id)
        obj = Pagenation(request, all_item.count(), per_page=2)
        return render(request, 'list_enrollment.html',
                      {'all_item': all_item[obj.start:obj.end], 'all_page': obj.show, 'customer_id': customer_id})


def modify_enrollment(request, pk=None, customer_id=None):
    user_obj = models.Enrollment(customer_id=customer_id) if customer_id else models.Enrollment.objects.filter(
        customer_id=pk).first()
    obj = EnrollmentForm(instance=user_obj)
    if request.method == 'POST':
        obj = EnrollmentForm(data=request.POST, instance=user_obj)
        if obj.is_valid():
            obj.save()
            url = request.GET.get('next', '')
            return redirect(url if url else 'list_enrollment')
    return render(request, 'form.html', {'obj': obj})
