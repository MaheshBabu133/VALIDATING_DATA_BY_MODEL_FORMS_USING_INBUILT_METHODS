from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'
        help_texts={"topic_name":'topic_name contains only lessthen or equal to 10 only'}

class WebpageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        help_texts={'name':'name characters between 4 to 10 only'}
class AccessRecordForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'
        help_texts={'author':'name characters between 4 to 6 only'}