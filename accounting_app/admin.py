from django.contrib import admin
from .models import Service, Contact, Vacancy, MyModel
# Register your models here.


admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Vacancy)

admin.site.register(MyModel)
