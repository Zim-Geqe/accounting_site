from django.contrib import admin
from .models import Service, Contact, Vacancy, MyModel, CustomUser
# Register your models here.

# from .models import User

admin.site.register(CustomUser)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Vacancy)

admin.site.register(MyModel)
