
#父类
from django import forms


class BootStrapModelForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            #字段中有属性则保留原来的属性，没属性加属性
            if field.widget.attrs:
                field.widget.attrs["class"] = 'form-control'
                field.widget.attrs["placeholder"] = f'请输入:{field.label}'
            else:
                field.widget.attrs= {'class': 'form-control',
                    'placeholder':f'请输入:{field.label}'
                }

class BootStrapForm(forms.Form):
    bootstrp_exclud_fields = []
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            #移除不需要加样bootstrap样式的字段
            if name in self.bootstrp_exclud_fields:
                continue
            #字段中有属性则保留原来的属性，没属性加属性
            if field.widget.attrs:
                field.widget.attrs["class"] = 'form-control'
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs= {'class': 'form-control',
                    'placeholder':field.label
                }