from django.urls import path, include
from .views import *


urlpatterns = [
    path('', TodoHome.as_view(), name='index'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('addtask/', AddTask.as_view(), name='addtask'),
    path('delete/<int:pk>/', DeleteTask.as_view(), name='task-delete'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('complete/<int:pk>/', Complete.as_view(), name='complete'),
]
