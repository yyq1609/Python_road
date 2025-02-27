#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib

from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import DateField, BooleanField
from multiselectfield.forms.fields import MultiSelectFormField

from crm import models


class BSForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields.values():
            if not isinstance(i, (MultiSelectFormField, DateField, BooleanField)):
                i.widget.attrs['class'] = 'form-control'
            if isinstance(i, DateField):
                i.widget = forms.TextInput(attrs={'placeholder': "YYYY-MM-DD", 'autocomplete': "off", 'type': 'date'})


class RegForm(forms.ModelForm):
    password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': "您的密码", 'autocomplete': "off", }))
    re_password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': "确认您的密码", 'autocomplete': "off", }))

    class Meta:
        model = models.UserProfile
        fields = '__all__'
        exclude = ['is_active']
        widgets = {
            'username': forms.EmailInput(attrs={'placeholder': "您的用户名", 'autocomplete': "off", }),
            'name': forms.TextInput(attrs={'placeholder': "您的名字", 'autocomplete': "off", }),
            'mobile': forms.TextInput(attrs={'placeholder': "您的手机号", 'autocomplete': "off", }),
        }
        error_messages = {
            'username': {
                'required': '信息不能为空',
                'invalid': '邮箱格式不正确',
            }
        }

    def clean(self):
        # self._validate_unique = True
        super().clean()
        password = self.cleaned_data.get('password', '')
        re_password = self.cleaned_data.get('re_password')
        if password == re_password:
            md = hashlib.md5(b'sajdfkh')
            md.update(password.encode('utf-8'))
            self.cleaned_data['password'] = md.hexdigest()
            return self.cleaned_data
        self.add_error('re_password', '两次密码不一致')
        raise ValidationError('两次密码不一致')


class CustomerForm(BSForm):
    class Meta:
        model = models.Customer
        fields = '__all__'
        widgets = {
            #     'qq': forms.TextInput(attrs={'placeholder': "QQ号", 'autocomplete': "off", 'label': 'QQ号码', }),
            #     'qq_name': forms.TextInput(attrs={'placeholder': "QQ昵称", 'autocomplete': "off", }),
            #     'name': forms.TextInput(attrs={'placeholder': "客户姓名", 'autocomplete': "off", }),
            #     'phone': forms.TextInput(attrs={'placeholder': '手机号', 'autocomplete': "off", }),
            #     'source': forms.Select(attrs={'placeholder': '来源渠道', 'autocomplete': "off", }),
            #     'customer_note': forms.Textarea(attrs={'placeholder': '备注', 'autocomplete': "off", }),
            #     'class_list': forms.SelectMultiple(attrs={'placeholder': '已报班级', 'autocomplete': "off", }),
        }


class ConsultRecord(BSForm):
    class Meta:
        model = models.ConsultRecord
        fields = '__all__'

    # def __init__(self, request, customer_id, *args, **kwargs):
    #     super(ConsultRecord, self).__init__(*args, **kwargs)
    #     if customer_id and customer_id != '0':
    #         self.fields['customer'].choices = [(i, str(i)) for i in models.Customer.objects.filter(pk=customer_id)]
    #     else:
    #         self.fields['customer'].choices = [('', '-------------')] + [(i.pk, str(i)) for i in request.user_obj.customers.all()]
    #     self.fields['consultant'].choices = [(request.user_obj.pk, request.user_obj)]

    def __init__(self, *args, **kwargs):
        super(ConsultRecord, self).__init__(*args, **kwargs)
        if self.instance.customer_id != '0':
            self.fields['customer'].choices = [(self.instance.customer.name, self.instance.customer.name)]
        else:
            self.fields['customer'].choices = [('', '-------------')] + [(i.pk, str(i)) for i in
                                                                         self.instance.consultant.customers.all()]
        # 限制为当前销售
        self.fields['consultant'].choices = [(self.instance.consultant.pk, self.instance.consultant)]


class EnrollmentForm(BSForm):
    class Meta:
        model = models.Enrollment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EnrollmentForm, self).__init__(*args, **kwargs)
        # self.instance  models.Enrollment(customer_id=customer_id)
        self.fields['customer'].choices = [(self.instance.customer_id, self.instance.customer)]
        print(self.fields['customer'].choices)
        self.fields['enrolment_class'].choices = [(i.pk, str(i)) for i in self.instance.customer.class_list.all()]
        print(self.fields['enrolment_class'].choices)
