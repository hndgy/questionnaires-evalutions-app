"""djangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import reverse
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from menu_questionnaire import views
from rest_framework.authtoken.views import obtain_auth_token
from menu_questionnaire.serializers import CustomAuthToken

router = routers.SimpleRouter()
router.register(r'Question', views.QuestionViews)

urlpatterns = [
    path('api/questionnaire', views.api_get_questionnaire_all_views, name = 'questionnaire_list'),
    path('register', views.registration_view, name = 'register_user'),
    path('api/get_utilisateur/<num>/<password>/', views.api_get_Etudiant_views, name = 'get_utilisateur'),
    path('api/update_reponse/<idR>/', views.api_put_reponse_views, name = 'update_reponse'),
    path('api/delete_reponse/<idR>/', views.api_delete_reponse_views, name = 'delete_reponse'),
    path('api/show_recap_user/<idU>/<idQ>', views.api_get_utilisateur_reponse, name = 'utilisateur_reponse'),
    path('api/show_question_reponse_user/<idU>/<idQ>/<idQu>', views.api_get_utilisateur_question_reponse, name = 'get reponse selon la Question et le questionnaire et le user'),
    path('api/create_reponse/', views.api_create_reponse_views, name = 'create_reponse'),
    path('api/type_question/<idQ>', views.api_type_question_views, name = 'type_question'),
    path('api/delete_questionnaire/<idQ>', views.api_delete_questionnaire_views, name = 'delete_question'),
    path('api/delete_question/<idQ>', views.api_delete_question_views, name = 'delete_question'),
    path('api/update_question/<idQ>', views.api_update_question_views, name = 'update_question'),
    path('api/update_questionnaire/<idQ>', views.api_put_questionnaire_views, name = "modif_questionnaire"),
    path('api/save_reponseUser/', views.api_save_reponseUser_views, name = "save_reponse_user"),
    path('api/show_questionnaire/<idQ>', views.api_get_questionnaire_views, name = "show_questionnaire_id"),
    path('api/show_question/<idG>', views.api_get_question_views, name = "show_question_id"),
    path('api/delete_user/<idU>', views.api_delete_reponse_views, name = "delete_user"),
    path('api/update_user/<idU>', views.api_update_user_views, name = "update_user"),
    path('api/create_question/', views.api_create_question_views, name = "create_question"),
    path('api/create_questionnaire/', views.api_create_questionnaire_views, name = "create_questionnaire"),
    path('api/update_question_questionnaire/<idQ>/<idQuest>', views.api_put_question_questionnaire_views, name = "update_question_selon_questionnaire"),
    path('api/delete_question_questionnaire/<idQ>/<idQuest>', views.api_delete_question_questionanire_views, name = "delete_question_selon_questionnaire"),
    path('api/add_question_questionnaire/<idQ>/<idQuest>', views.api_add_question_questionnaire_views, name = "add_question_selon_questionnaire"),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^login/', CustomAuthToken.as_view()),
    path('api/reponse/<idR>', views.api_get_reponse_views, name = 'get_reponse'),
]
