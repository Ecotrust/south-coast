from django.conf.urls.defaults import *
from views import *


urlpatterns = patterns('',
	(r'^authenticateUser', authenticateUser),
	(r'^createUser', createUser),
	(r'^updateUser', updateUser),
	(r'^forgotPassword', forgotPassword),
)