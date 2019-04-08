from django import forms

class searchForm(forms.ModelForm):
    searchForm=forms.CharField(label='搜索',max_length=40)



