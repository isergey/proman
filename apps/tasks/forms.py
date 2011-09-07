# encoding: utf-8
from django import forms
from models import Project, Milestone, Task

class TaskForm(forms.ModelForm):
    def __init__(self, milestone=None,  *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        if milestone:
            self.fields['depends_from'].queryset = Task.objects.filter(milestone=milestone)
    class Meta:
        model = Task
        widgets = {
            'milestone': forms.HiddenInput(),
            'responsible': forms.SelectMultiple(attrs={'class':'multiple'}),
            'depends_from': forms.CheckboxSelectMultiple(attrs={'class':'checkboxes'}),
        }


#class _TaskForm(forms.Form):
#    milestone = forms.HiddenInput()
#    name = forms.TextInput()

