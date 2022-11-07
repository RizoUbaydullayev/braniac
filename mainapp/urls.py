from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('news/', views.NewsView.as_view()),
    path('courses_list/', views.CoursesListView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('doc_site/', views.DocSiteView.as_view()),
    path('contacts/', views.ContactsView.as_view()),
]
