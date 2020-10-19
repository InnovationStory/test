
from django.views.generic import TemplateView
from django.views.generic import  View, CreateView, ListView, UpdateView, DeleteView, DetailView
from ..forms import ProcessForm,InputForm_add,OutputForm_add,TechForm_add,DecForm_add,SkillForm_add, EquipeForm,ActorForm_add, TaskForm, ActivityForm, TaskAddForm, ActivityAddForm, Type_actorForm, ActorForm, SkillForm, DecisionForm,  FinalProductForm, InputForm
from ..models import Process, Activity,Task,  Actor, Skill, Decision,Type_actors, Input, Output, Technologie
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from  classroom.filters import ProcessFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy

def home(request):      
    return render(request, 'Home/index.html')

def elements(request):      
    return render(request, 'Home/elements.html')


def test(request):      
    return render(request, 'Home/elements.html')



#DataBase 


class DataBaseView(ListView):
    model = Process
    ordering=('process_name')
    context_object_name='processes'
    template_name= 'Home/DataBase/process.html'


    def get_queryset(self):
        queryset = Process.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(DataBaseView, self).get_context_data(**kwargs)
        process= Process.objects.all()
        total_sales = {} # create an empty dictionary 
        for day in process:
            # get the sales for that particular day 
            total_sales[day] = Activity.objects.filter(process_id=day.pk)
        context['activities'] = total_sales # pass 'total_sales' dictionary in context
        return context


#Search Items 
    
def Research(request):
    template_name = 'Home/SearchItems/search.html'
    process_list = Process.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(process_list, 10)
    process_filter = ProcessFilter(request.GET, queryset = process_list)
    return render(request, template_name, {'filter' : process_filter, 'process_list': process_list})





#SearchDetails


class SearchDetailView(ListView):
    model = Process
    ordering=('process_name')
    context_object_name='process'
    template_name= 'Home/SearchItems/detail.html'

    def get_queryset(self):
        queryset = get_object_or_404(Process, pk=self.kwargs['pk'])
        return queryset


#Add Items


class AddItemsHomeView(ListView):
    model = Process
    context_object_name = 'process'
    template_name = 'Home/AddItems/home.html'

    def get_queryset(self):
        queryset = Process.objects.all()  
        return queryset



    #add activity

# add activity  
class add_activity(CreateView):
    model =Activity
    form_class = ActivityForm
    template_name = 'Home/AddItems/Activity/add_activity.html'

    def form_valid (self, form):
        activity = form.save(commit=False)
        activity.save()
        return redirect ('activity_change', activity.pk)



class Update_activity_View(UpdateView):
    model = Activity
    fields = '__all__'

    template_name = 'Home/AddItems/Activity/activity_change.html'

    def form_valid(self, form):
        case = form.save(commit=False)
        case.save()
        return redirect('activity_change', case.pk)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Update_activity_View, self).get_context_data(**kwargs)
        context['activity'] = get_object_or_404(Activity, pk=self.kwargs['pk'])
        return context     

class add_activity_second(CreateView):
    model = Activity
    fields = ['activity_name', 'definition']
    template_name = 'Home/AddItems/Activity/add_another_activity.html'

    def form_valid(self, form):
        act=get_object_or_404(Activity, pk=self.kwargs['pk'])
        case = form.save(commit=False)
        case.process_id= act.process_id
        case.save()
        return redirect('activity_change', case.pk)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(add_activity_second, self).get_context_data(**kwargs)
        context['activity'] = get_object_or_404(Activity, pk=self.kwargs['pk'])
        return context     

    



class add_task_view(SuccessMessageMixin, CreateView):
    model = Task
    form_class = EquipeForm
    template_name = 'Home/AddItems/Activity/add_task.html'


    def form_valid(self, form):
        act = get_object_or_404(Activity, pk=self.kwargs['pk'])
        quiz = form.save(commit=False)
        quiz.activety_id = act
        quiz.save()
        form.save_m2m()
        return redirect('task_change', quiz.pk)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(add_task_view, self).get_context_data(**kwargs)
        context['activity'] = get_object_or_404(Activity, pk=self.kwargs['pk'])
        return context      





class Update_Task_View(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'Home/AddItems/Activity/task_change.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        return redirect('task_change', quiz.pk)


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Update_Task_View, self).get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=self.kwargs['pk'])
        return context       




class activityDeleteView(DeleteView):
    model = Activity
    context_object_name = 'activity'
    template_name = 'Home/AddItems/Activity/delete.html'
    success_url = reverse_lazy('add_items')

    def delete(self, request, *args, **kwargs):
        quiz = self.get_object()
        return super().delete(request, *args, **kwargs)



# Party 2


# add tasck 
class Task_view_add(CreateView):
    model =Task
    form_class = TaskForm
    template_name = 'Home/AddItems/addTask.html'

    def form_valid (self, form):
        activity = form.save(commit=False)
        activity.save()
        return redirect ('task_task_change', activity.pk)


# Update task 


class Task_change_view(UpdateView):
    model = Task
    fields= '__all__'
    context_object_name = 'task'
    template_name = 'Home/AddItems/Task/task_change.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        return redirect('task_task_change', quiz.pk)
    
#Delete Task

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'Home/AddItems/Task/delete.html'
    success_url = reverse_lazy('add_items')

    def delete(self, request, *args, **kwargs):
        quiz = self.get_object()
        return super().delete(request, *args, **kwargs)





# add actors
class Actor_Task_View(CreateView):
    model = Actor
    fields = ['actor_name']
    template_name = 'Home/AddItems/Task/add_actors.html'


    def form_valid(self, form):    
        quiz = form.save(commit=False)
        quiz.save()
        form.save_m2m()
        return redirect('add_items')








class Add_other_task_task_view(CreateView):
    model = Task
    fields= ['name', 'definition']
    template_name = 'Home/AddItems/Task/another_task.html'
   


    def form_valid(self, form,  **kwargs):
        task=get_object_or_404(Task, pk=self.kwargs['pk'])
        case = form.save(commit=False)
        case.activety_id= task.activety_id
        case.save()
        return redirect('task_task_change', case.pk)

# Add actors

class actor_view_add(CreateView):
    model = Actor
    form_class = ActorForm_add
    template_name = 'Home/AddItems/Actor/add_actors.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        form.save_m2m()

        return redirect('actor_change', quiz.pk)


#Updae actor
class Actor_change_view(UpdateView):
    model = Actor
    form_class = ActorForm_add
    context_object_name = 'actor'
    template_name = 'Home/AddItems/Actor/actor_change.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        form.save_m2m()
        return redirect('actor_change', quiz.pk)



#Delete Task

class ActorDeleteView(DeleteView):
    model = Actor
    context_object_name = 'actor'
    template_name = 'Home/AddItems/Actor/delete.html'
    success_url = reverse_lazy('add_items')

    def delete(self, request, *args, **kwargs):
        quiz = self.get_object()
        return super().delete(request, *args, **kwargs)



# Add inputs
class input_view_add(CreateView):
    model = Input
    form_class = InputForm_add
    context_object_name = 'input'
    template_name = 'Home/AddItems/Input/input_add.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        form.save_m2m()
        return redirect('input_change', quiz.pk)


# Add inputs
class input_change_add(UpdateView):
    model = Input
    form_class = InputForm_add
    context_object_name = 'input'
    template_name = 'Home/AddItems/Input/input_change.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        form.save_m2m()
        return redirect('input_change', quiz.pk)



#Delete Input

class InputDeleteView(DeleteView):
    model = Input
    context_object_name = 'input'
    template_name = 'Home/AddItems/Input/delete.html'
    success_url = reverse_lazy('add_items')

    def delete(self, request, *args, **kwargs):
        quiz = self.get_object()
        return super().delete(request, *args, **kwargs)







# Add outputs
class output_view_add(SuccessMessageMixin, CreateView):
    model = Output
    form_class = OutputForm_add
    template_name = 'Home/AddItems/Output/output_add.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        messages.success = "The Output was created with success!"
        return redirect('output_change', quiz.pk)


# Add inputs
class Output_change(UpdateView):
    model = Output
    form_class = OutputForm_add
    context_object_name = 'output'
    template_name = 'Home/AddItems/Output/output_change.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        form.save_m2m()
        return redirect('output_change', quiz.pk)



#Delete Input

class OutputDeleteView(DeleteView):
    model = Output
    context_object_name = 'output'
    template_name = 'Home/AddItems/Output/delete.html'
    success_url = reverse_lazy('add_items')

    def delete(self, request, *args, **kwargs):
        quiz = self.get_object()
        return super().delete(request, *args, **kwargs)







# Add Tech
class tech_view_add(SuccessMessageMixin, CreateView):
    model = Technologie
    form_class = TechForm_add
    template_name = 'Home/AddItems/tech/tech_add.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        messages.success = "The Technologie was created with success!"
        return redirect('tech_change', quiz.pk)




# Add inputs
class tech_change(UpdateView):
    model = Technologie
    form_class = TechForm_add
    context_object_name = 'tech'
    template_name = 'Home/AddItems/tech/tech_change.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        form.save_m2m()
        return redirect('tech_change', quiz.pk)



#Delete Input

class techDeleteView(DeleteView):
    model = Technologie
    context_object_name = 'tech'
    template_name = 'Home/AddItems/tech/delete.html'
    success_url = reverse_lazy('add_items')

    def delete(self, request, *args, **kwargs):
        quiz = self.get_object()
        return super().delete(request, *args, **kwargs)


















# Add Skill
class skill_view_add(SuccessMessageMixin, CreateView):
    model = Skill
    form_class = SkillForm_add
    template_name = 'Home/AddItems/Skill/skill_add.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        messages.success = "The Skill was created with success!"
        return redirect('skill_change', quiz.pk)




# Add inputs
class skill_change(UpdateView):
    model = Skill
    form_class = SkillForm_add
    context_object_name = 'skill'
    template_name = 'Home/AddItems/Skill/skill_change.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        form.save_m2m()
        return redirect('skill_change', quiz.pk)



#Delete Input

class skillDeleteView(DeleteView):
    model = Skill
    context_object_name = 'skill'
    template_name = 'Home/AddItems/Skill/delete.html'
    success_url = reverse_lazy('add_items')

    def delete(self, request, *args, **kwargs):
        quiz = self.get_object()
        return super().delete(request, *args, **kwargs)




































# Add Dec
class dec_view_add(SuccessMessageMixin, CreateView):
    model = Decision
    form_class = DecForm_add
    template_name = 'Home/AddItems/Dec/dec_add.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        messages.success = "The Decision was created with success!"
        return redirect('dec_change', quiz.pk)






# Add inputs
class dec_change(UpdateView):
    model = Decision
    form_class = DecForm_add
    context_object_name = 'dec'
    template_name = 'Home/AddItems/Dec/dec_change.html'


    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        form.save_m2m()
        return redirect('dec_change', quiz.pk)



#Delete Input

class decDeleteView(DeleteView):
    model = Decision
    context_object_name = 'dec'
    template_name = 'Home/AddItems/Dec/delete.html'
    success_url = reverse_lazy('add_items')

    def delete(self, request, *args, **kwargs):
        quiz = self.get_object()
        return super().delete(request, *args, **kwargs)



































class First(ListView):
    model = Process
    ordering=('process_name')
    context_object_name='processes'
    template_name= 'Home/Display/process.html'

    def get_queryset(self):
        queryset = Process.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(First, self).get_context_data(**kwargs)
        # Add in the publisher
        context['activities'] = get_object_or_404(Process, pk=self.kwargs['pk'])
        return context    




class ActivityDetaiListView(ListView):
    model = Activity
    template_name = 'Home/Display/activities.html'
    context_object_name = 'activities'

    def get_queryset(self):
        activity = get_object_or_404(Activity, pk=self.kwargs['pk'])
        return activity 



class ProcessDisplayView(ListView):
    model = Process
    ordering=('process_name')
    context_object_name='processes'
    template_name= 'Home/Display/process.html'


    def get_queryset(self):
        queryset = Process.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProcessDisplayView, self).get_context_data(**kwargs)
        process= Process.objects.all()
        total_sales = {} # create an empty dictionary 
        for day in process:
            # get the sales for that particular day 
            total_sales[day] = Activity.objects.filter(process_id=day.pk)
        context['activities'] = total_sales # pass 'total_sales' dictionary in context
        return context



class ProcessDetailListView(ListView):
    model = Process
    template_name = 'Home/Display/detail_process.html'
    context_object_name = 'activities'

    def get_queryset(self):
        process = get_object_or_404(Process, pk=self.kwargs['pk'])
        return Activity.objects.filter(process_id=process.pk)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProcessDetailListView, self).get_context_data(**kwargs)
        # Add in the publisher
        process = get_object_or_404(Process, pk=self.kwargs['pk'])
  
        return context    

   
   




#Tasks
class TaskCreateView(CreateView):
    model= Task
 
    template_name='task.html'

    def form_valid(self, form) :
        form = form.save(commit=False)
        form.save()
        return redirect('home')

#Process 

class ProcessCreateView(CreateView):
    model = Process
    form_class = ProcessForm
    template_name = 'process.html'

    def form_valid(self, form):
        process = form.save(commit=False)
        process.save()
        return redirect('process_add')



# Add Create ADD_home Index 

class AddCreateView(ListView):
    model = Process
    context_object_name = 'process'
    template_name = 'Home/Add_query/add_elements.html'

    def get_queryset(self):
        queryset = Process.objects.all()  
        return queryset




def add_act(request, pk):
    process = get_object_or_404(Process, pk)

    if request.method =="POST" :
       actform = ActivityAddForm(request.POST)
       if actform.is_valid ():
          act = actform.save(commit=False)
          act.process_id= process
          act.save()
          return redirect('activity_add')
    else :
        actform = ActivityAddForm ()
    return render (request, 'activity_print')






# add other activity
class add_other_activ(CreateView):
    model =Activity
    form_class = ActivityForm
    template_name = 'Home/Add_query/add_activity.html'

    def form_valid (self, form):
        activity = form.save(commit=False)
        activity.save()
        return redirect ('add_activity')


# add task activity
class add_activity_task(CreateView):
    model =Activity
    form_class = ActivityForm
    template_name = 'Home/Add_query/add_activity.html'

    def form_valid (self, form):
        activity = form.save(commit=False)
        activity.save()
        return redirect ('add_task', activity.pk)


  








def add_task_prev(request, pk):
    act = get_object_or_404(Activity, pk=pk)
    template_name = 'Home/Add_query/add_task.html'


    if request.method == "POST":
        form = TaskAddForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.activety_id= act
            post.save()
            return redirect('home')
    else:

        form = TaskAddForm
    return render(request, template_name)







class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activity.html'

    def form_valid(self, form):
        activity = form.save(commit=False)
        activity.save()
        return redirect('home')




class ProcessListView(ListView):
    model = Process
    context_object_name = 'process'
    template_name = 'process_page.html'

    def get_queryset(self):
        queryset = Process.objects.all()  
        return queryset



class ActivityListView(ListView):
    model = Activity
    ordering = ('activity_name', )
    context_object_name = 'activities'
    template_name = 'activity_page.html'

    
    def get_queryset(self):
        queryset = Activity.objects.filter(process_id=self.kwargs['pk']).distinct() 
        return queryset

    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        queryskill= Skill.objects.filter(process_id=self.kwargs['pk']).distinct()
        querydecision= Decision.objects.filter(process_id=self.kwargs['pk']).distinct()
        # Add in the publisher
        context['projet'] = queryskill
        context['decision'] = querydecision
        return context







class Add_element(ListView):
    model = Activity
    template_name = 'Home/Display/elements.html'
    context_object_name = 'activities'

    def get_queryset(self):
        activity = get_object_or_404(Task, pk=self.kwargs['pk'])
        return activity 

class add_actor_element(CreateView):
    model = Actor
    form_class = ActorForm_add
    template_name = 'Home/Display/add_actors.html'

    def form_valid(self, form):
        act=get_object_or_404(Task, pk=self.kwargs['pk'])
        case = form.save(commit=False)
        case.save()
        form.save_m2m()
        return redirect('activities_detail', act.activety_id.pk)




class actor_carte(ListView):
    model = Actor
    template_name = 'Home/AddItems/Actor/carte_actor.html'
    context_object_name = 'var'

    def get_queryset(self):
        acteur = get_object_or_404(Actor, pk=self.kwargs['pk'])
        return acteur


class add_input_element(CreateView):
    model = Input
    fields = ['input_name', 'definition']
    template_name = 'Home/Display/add_input.html'

    def form_valid(self, form):
        act=get_object_or_404(Task, pk=self.kwargs['pk'])
        case = form.save(commit=False)
        case.task_id= act
        case.save()
        return redirect('activities_detail', act.activety_id.pk)

class add_output_element(CreateView):
    model = Output
    fields = ['output_name', 'definition']
    template_name = 'Home/Display/add_output.html'

    def form_valid(self, form):
        act=get_object_or_404(Task, pk=self.kwargs['pk'])
        case = form.save(commit=False)
        case.task_id= act
        case.save()
        return redirect('activities_detail', act.activety_id.pk)

class add_dec_element(CreateView):
    model = Decision
    fields = ['decision_name', 'definition']
    template_name = 'Home/Display/add_decision.html'

    def form_valid(self, form):
        act=get_object_or_404(Task, pk=self.kwargs['pk'])
        case = form.save(commit=False)
        case.task_id= act
        case.save()
        return redirect('activities_detail', act.activety_id.pk)


class add_tech_element(CreateView):
    model = Technologie
    fields = ['technologie_name', 'technology_maturity','definition']
    template_name = 'Home/Display/add_tech.html'

    def form_valid(self, form):
        act=get_object_or_404(Task, pk=self.kwargs['pk'])
        case = form.save(commit=False)
        case.task_id= act
        case.save()
        return redirect('activities_detail', act.activety_id.pk)

class add_skill_element(CreateView):
    model = Skill
    fields = ['skills_name', 'skills_maturity', 'definition']
    template_name = 'Home/Display/add_skill.html'

    def form_valid(self, form):
        act=get_object_or_404(Task, pk=self.kwargs['pk'])
        case = form.save(commit=False)
        case.task_id= act
        case.save()
        return redirect('activities_detail', act.activety_id.pk)





















def post_detail(request, pk):
    post = get_object_or_404(Task, pk=pk)
    return render(request, 'Home/Display/elements.html', {'post': post})
    
    #return render(request, 'classroom/students/case_form_display.html', {'post': post})
    






#Create Skill

class SkillCreateView(CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skill.html'

    def form_valid(self, form):
        skill = form.save(commit=False)
        skill.save()
        return redirect('home')




#Create Decision

class DecisionCreateView(CreateView):
    model = Decision
    form_class = DecisionForm
    template_name = 'decision.html'

    def form_valid(self, form):
        decision = form.save(commit=False)
        decision.save()
        return redirect('home')





#Create FinalProduct

class FinalProductCreateView(CreateView):
    model = Output
    form_class = FinalProductForm
    template_name = 'finalProduct.html'

    def form_valid(self, form):
        finalProduct = form.save(commit=False)
        finalProduct.save()
        return redirect('home')





#Create Ressource

class RessourceView(CreateView):
    
 
    template_name = 'ressource.html'

    def form_valid(self, form):
        ressource = form.save(commit=False)
        ressource.save()
        return redirect('home')

















def ActorCreateView(request):      
    return render(request, 'actor.html')
