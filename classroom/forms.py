

from django import forms
from django.db import transaction
from django.forms.utils import ValidationError
from django.utils.translation import gettext_lazy as _
from classroom.models import (Process, Activity,Technologie, Task, Type_actors, Actor, Output, Skill, Decision,  Input)




#Add activityForm

class ActivityAddForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields  = '__all__'






# AddTask
class TaskAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'definition']








# AddTask
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'definition','activety_id']






class ActorForm_add(forms.ModelForm):

    task_id  = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Task List ',
    

    )
    

    class Meta:
          model = Actor
          fields = ['task_id','actor_name',  'prenom', 'presentation', 'adress', 'contact',  'type_actor', 'partenair_nam1', 'partenair_nam2', 'partenair_nam3', 'partenair_nam4']
         

   

# AddInput
class InputForm_add(forms.ModelForm):
    class Meta:
        model = Input
        fields = ['input_name', 'definition','task_id']




# AddOutput
class OutputForm_add(forms.ModelForm):
    class Meta:
        model = Output
        fields = ['output_name', 'definition','task_id']



# AddTechnologie
class TechForm_add(forms.ModelForm):
    class Meta:
        model = Technologie
        fields = ['technologie_name', 'technology_maturity','definition','task_id']

 



# AddSkill
class SkillForm_add(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skills_name', 'skills_maturity','definition','task_id']




# AddDec
class DecForm_add(forms.ModelForm):
    class Meta:
        model = Decision
        fields = ['decision_name', 'definition','task_id']




# Process
class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ['process_name', 'definition']




# Activity
class ActivityForm(forms.ModelForm):

    

    class Meta:
          model = Activity
          fields = ['activity_name', 'definition','process_id']




# Actor
class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'


# Skill


class SkillForm(forms.ModelForm):


    class Meta:
          model = Skill
          fields ='__all__'
         



# Skill


class DecisionForm(forms.ModelForm):


    class Meta:
          model = Decision
          fields ='__all__'

 
 
 
class FinalProductForm(forms.ModelForm):


    class Meta:
          model = Output
          fields = '__all__'





 
class InputForm(forms.ModelForm):


    class Meta:
          model = Input
          fields = '__all__'



class EquipeForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'definition']
 


 
class Type_actorForm(forms.ModelForm):


    class Meta:
          model = Type_actors
          fields = '__all__'
 

