from django.contrib import admin

from .models import Account, Course, Term

admin.site.register(Account)
admin.site.register(Course)
admin.site.register(Term)
