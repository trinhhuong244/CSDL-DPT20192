from django import forms
from .models import *


KV = [('Thanh Xuan', 'Thanh Xuan'), ('Hai Ba Trung', 'Hai Ba Trung'),
      ('Cau Giay', 'Cau Giay'), ('Ba Dinh', 'Ba Dinh'), ('Tay Ho', 'Tay Ho'), ]
PK = [('Khong', 'Khong'), ('Vong co', 'Vong co'),
      ('Xich', 'Xich'), ('Ro mom', 'Ro mom')]


class DogInfo(forms.ModelForm):
    class Meta:
        model = Image_db
        fields = ['tag', 'image']


class Post(forms.Form):
    specie = forms.CharField(label="Giong cho: ", max_length=100)
    weight = forms.CharField(label="Can nang: ", max_length=100)
    height = forms.CharField(label="Chieu cao: ", max_length=100)
    color = forms.CharField(label="Mau sac: ", max_length=100)
    access = forms.ChoiceField(label="Phu kien: ", choices=PK)
    area = forms.ChoiceField(label="Khu vuc: ", choices=KV)
    time = forms.CharField(label="Thoi gian: ", max_length=100)
    status = forms.CharField(label="Trang thai: ", max_length=100)
    image = forms.ImageField(label="Hinh anh: ")


class SearchDogForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SearchDogForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    dogType = forms.CharField(label='Loại chó', max_length=100)
    dogImage = forms.ImageField()


class SearchLostDogForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SearchLostDogForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    dogImage = forms.ImageField()
    species = forms.CharField(label='Chủng loại', max_length=100)
    weight = forms.CharField(label='Cân nặng', max_length=100)
    height = forms.CharField(label='Chiều cao', max_length=100)
    color = forms.CharField(label='Màu lông', max_length=100)
    accessory = forms.CharField(label='Phụ kiện', max_length=100)
    location = forms.CharField(label='Địa điểm', max_length=100)
    time = forms.CharField(label='Thời gian', max_length=100)
    status = forms.CharField(label='Trạng thái', max_length=100)


class PostForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    dogImage = forms.ImageField()
    species = forms.CharField(label='Chủng loại', max_length=100)
    weight = forms.CharField(label='Cân nặng', max_length=100)
    height = forms.CharField(label='Chiều cao', max_length=100)
    color = forms.CharField(label='Màu lông', max_length=100)
    accessory = forms.CharField(label='Phụ kiện', max_length=100)
    location = forms.CharField(label='Địa điểm', max_length=100)
    time = forms.CharField(label='Thời gian', max_length=100)
    status = forms.CharField(label='Trạng thái', max_length=100)