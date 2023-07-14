from django.urls import path
from .views import CreateAccountView, ViewAccount

app_name = 'users'

urlpatterns = [
     path('create-account/', CreateAccountView.as_view(), name='createAccount'),
     path('view-account/', ViewAccount.as_view(), name =  'viewAccount'),
]
