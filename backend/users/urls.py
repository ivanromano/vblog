from django.urls import path
from users import views

urlpatterns = [
    path('token', views.CreateTokenView.as_view()),
    path('create', views.CreateUserView.as_view()),
    path('user', views.RetreiveUpdateUserView.as_view()),
    path('list', views.ListaUserView.as_view())
]



