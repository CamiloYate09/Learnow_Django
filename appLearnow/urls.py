from django.urls import path
# >>>2 https://docs.djangoproject.com/en/2.0/topics/http/urls/#including-other-urlconfs
from . import views

urlpatterns = [
    # >>>10
    path('list/', views.learNow_list),
]
