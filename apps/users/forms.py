# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/5/11 15:25'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, max_length=5)