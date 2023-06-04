from django.contrib import admin
from django.urls import path, include
from . import views
from .views import DocumentListView, HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("changer", views.changer, name="changer"),
    path("view", DocumentListView.as_view(), name="view"),
    path("create", views.create, name="create"),
    path('download/<int:document_id>/', views.download, name='download'),
    path('pdf/<int:document_id>/', views.pdf_view, name='pdf'),
    path('delete/<int:document_id>/', views.delete, name='delete'),
]
