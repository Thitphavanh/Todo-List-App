from django.urls import path
from .views import * # * ດຶງມາທຸກຟັງຊັ້ນໃນ views.py

urlpatterns = [
    path('', Home),
    path('api/all-todolist/',all_todolist), # localhost:8000/api/all_todolist
    path('api/post-todolist',post_todolist),
    path('api/update-todolist/<int:TID>',update_todolist),
    path('api/delete-todolist/<int:TID>',delete_todolist),
]
