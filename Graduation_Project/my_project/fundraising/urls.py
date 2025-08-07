from django.urls import path
from . import views

urlpatterns = [
    # رابط الصفحة الرئيسية
    path('', views.home, name='home'),

    # روابط تسجيل المستخدمين والدخول والخروج
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # رابط لعرض كل المشاريع (القائمة)
    path('projects/', views.project_list, name='project_list'),
    
    # رابط لإنشاء مشروع جديد
    path('projects/create/', views.create_project, name='create_project'),

    # رابط لتعديل مشروع معين، نمرر له رقم المشروع (project_id)
    path('projects/<int:project_id>/edit/', views.edit_project, name='edit_project'),

    # رابط لحذف مشروع معين، نمرر له رقم المشروع (project_id)
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),
]