from django.urls import include, path

from .views import classroom

urlpatterns = [
    path('', classroom.home, name='home'),
    path('test/', classroom.test,  name='test'),

#DataBase

    path('database/processes/', classroom.DataBaseView.as_view(), name='data_base'),

#Search Items 
    path('Research/items/', classroom.Research, name='search_items'),
    #detail_of_search
    path('Research/Items/datail/<int:pk>', classroom.SearchDetailView.as_view(), name='detail_research_view'),

# Add Items 
    
    path('AddItems/', classroom.AddItemsHomeView.as_view(), name='add_items'),
        
#add activity 
    #  Adda activity
    path('add_activity/', classroom.add_activity.as_view(), name='add_activity'),
    path('activity/<int:pk>/change', classroom.Update_activity_View.as_view(), name='activity_change'),
      # add task to the activity
    path('add_task/<int:pk>', classroom.add_task_view.as_view(), name='add_task'),
    path('add_task/<int:pk>/change', classroom.Update_Task_View.as_view(), name='task_change'),
    path('add_another_activity/(?P<int:pk>\d+)/', classroom.add_activity_second.as_view(), name='add_another_activity'),
    path('delete_activity/(?P<int:pk>\d+)/', classroom.activityDeleteView.as_view(), name='delete_activity'),


# add Task 
    path('task_view_add/', classroom.Task_view_add.as_view(), name='task_view_add'),
    #update task 
   
    path('add_task/update_task/(?P<int:pk>\d+)/change', classroom.Task_change_view.as_view(), name='task_task_change'),
    path('add_task/add_other_task_task/(?P<int:pk>\d+)/change', classroom.Add_other_task_task_view.as_view(), name='add_other_task_task'),
    path('add_task/add_actor(?P<int:pk>\d+)/', classroom.Actor_Task_View.as_view(), name='actor_task'),

    
    path('delete_task/<int:pk>/', classroom.TaskDeleteView.as_view(), name='delete_task'),



#add activity 
    #  Adda activity
 
    #add actors
    #  Adda actors
    path('actor_view_add/', classroom.actor_view_add.as_view(), name='actor_view_add'),
    path('actor_view_change/(?P<int:pk>\d+)/$', classroom.Actor_change_view.as_view(), name='actor_change'),
    path('delete_actor/(?P<int:pk>\d+)/$', classroom.ActorDeleteView.as_view(), name='delete_actor'),


       #  Adda inputs
    path('input_view_add/', classroom.input_view_add.as_view(), name='input_view_add'),
    path('input_view_change/(?P<int:pk>\d+)/$', classroom.input_change_add.as_view(), name='input_change'),
    path('delete_input/(?P<int:pk>\d+)/$', classroom.InputDeleteView.as_view(), name='delete_input'),




 
        #  Adda Output
    path('output_view_add/', classroom.output_view_add.as_view(), name='output_view_add'),
    path('output_view_change/(?P<int:pk>\d+)/$', classroom.Output_change.as_view(), name='output_change'),
    path('delete_output/(?P<int:pk>\d+)/$', classroom.OutputDeleteView.as_view(), name='delete_output'),





#add activity 
    #  Adda activity
 
    #add actors
    #  Adda actors
    path('actor_view_add/', classroom.actor_view_add.as_view(), name='actor_view_add'),

        #  Adda Technologie
    path('tech_view_add/', classroom.tech_view_add.as_view(), name='tech_view_add'),
    path('tech_view_change/(?P<int:pk>\d+)/$', classroom.tech_change.as_view(), name='tech_change'),
    path('delete/(?P<int:pk>\d+)/$', classroom.techDeleteView.as_view(), name='delete_tech'),
   
   
            #  Adda Skills
    path('skill_view_add/', classroom.skill_view_add.as_view(), name='skill_view_add'),
    path('skill_view_change/(?P<int:pk>\d+)/$', classroom.skill_change.as_view(), name='skill_change'),
    path('skill_delete/(?P<int:pk>\d+)/$', classroom.skillDeleteView.as_view(), name='skill_delete'),  
    
            #  Adda Decision
    path('dec_view_add/', classroom.dec_view_add.as_view(), name='dec_view_add'),
    path('decision_view_change/(?P<int:pk>\d+)/$', classroom.dec_change.as_view(), name='dec_change'),
    path('skill_delete/(?P<int:pk>\d+)/$', classroom.decDeleteView.as_view(), name='delete_dec'),  
   
    
  


    path('process/add/', classroom.ProcessCreateView.as_view(), name='process_add'),
    path('process/print/', classroom.ProcessListView.as_view(), name='process_print'),

    
    path('activity/add/', classroom.ActivityCreateView.as_view(), name='activity_add'),
    path('activity/print/<pk>/', classroom.ActivityListView.as_view(), name='activity_print'),
   
    path('actor/add/', classroom.ActorCreateView, name='actor_add'),



    path('skill/add/', classroom.SkillCreateView.as_view(), name='skill_add'),

    path('task/add/', classroom.TaskCreateView.as_view(), name='task_add'),



    # Add processing 
    path('Add_query/', classroom.AddCreateView.as_view(), name='add_query'),






    #  Adda other activity
    path('add_other_activity/', classroom.add_other_activ.as_view(), name='add_other_activity'),

    
    #  Acteur
    path('stakeholder_carte/(?P<int:pk>\d+)/$', classroom.actor_carte.as_view(), name='carte_acteur'),

  # add task to the activity (activitu url)
    path('add_task_activity/', classroom.add_activity_task.as_view(), name='add_task_activity'),


  # add task to the activity (activitu url)
    path('add_task_elements/<int:pk>/', classroom.Add_element.as_view(), name='task_elements'),
    path('case/<int:pk>/display', classroom.post_detail, name='post_detail'),
    path('add_task_elements/add_actor_element/<int:pk>/', classroom.add_actor_element.as_view(), name='add_actor_element'),
    path('add_task_elements/add_input_element/<int:pk>/', classroom.add_input_element.as_view(), name='add_input_element'),
    path('add_task_elements/add_output_element/<int:pk>/', classroom.add_output_element.as_view(), name='add_output_element'),
    path('add_task_elements/add_decision_element/<int:pk>/', classroom.add_dec_element.as_view(), name='add_decision_element'),
    path('add_task_elements/add_tech_element/<int:pk>/', classroom.add_tech_element.as_view(), name='add_tech_element'),
    path('add_task_elements/add_skill_element/<int:pk>/', classroom.add_skill_element.as_view(), name='add_skill_element'),  
  





# Afficher les processus 
    path('Dispaly/Processes/', classroom.ProcessDisplayView.as_view(), name='display_process'),
    path('Display/Processes/Detail_View/<int:pk>/', classroom.ProcessDetailListView.as_view(), name='process_detail'),
    path ('Dispaly/Process/Activity/Detail_view/<int:pk>/', classroom.ActivityDetaiListView.as_view(), name='activities_detail'),
# Afficher les processus 
    path('Elements/', classroom.elements, name='elements'),
    





]
