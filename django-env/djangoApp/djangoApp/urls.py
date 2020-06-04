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

router = routers.SimpleRouter()
router.register(r'Questionnaire', views.QuestionnaireViews)
router.register(r'Question', views.QuestionViews)


urlpatterns = [
    path('api/update_questionnaire/<idQ>', views.api_put_questionnaire_views, name = "modif_questionnaire"),
    path('api/create_user', views.api_create_utilisateur_views, name = "create_user"),
    path('api/create_reponse/', views.api_create_reponse_views, name = "create_reponse"),
    path('api/show_questionnaire/<idQ>', views.api_get_questionnaire_views, name = "show_questionnaire_id"),
    path('api/show_question/<idG>', views.api_get_question_views, name = "show_question_id"),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
