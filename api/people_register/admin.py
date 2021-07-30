from django.contrib import admin
from people_register.models import *


class PersonTypes(admin.ModelAdmin):
    list_display = ('id', 'person_type')
    list_display_links = ('id', 'person_type')
    search_fields = ('id', 'person_type',)
    list_per_page = 10
    ordering = ('id', 'person_type',)


admin.site.register(PersonType, PersonTypes)


class PersonMediaTypes(admin.ModelAdmin):
    list_display = ('id', 'media_type')
    list_display_links = ('id', 'media_type')
    search_fields = ('id', 'media_type',)
    list_per_page = 10
    ordering = ('id', 'media_type',)


admin.site.register(PersonMediaType, PersonMediaTypes)


class People(admin.ModelAdmin):
    list_display = ('id', 'name', 'person_type', 'cpf', 'company', 'last_update')
    list_display_links = ('id', 'name', 'person_type', 'cpf', 'last_update')
    search_fields = ('id', 'name', 'person_type', 'cpf', 'last_update',)
    list_per_page = 10
    ordering = ('id', 'name', 'person_type', 'cpf', 'last_update',)


admin.site.register(Person, People)


class PersonMedias(admin.ModelAdmin):
    list_display = ('id', 'person_id', 'media_type')
    list_display_links = ('id', 'person_id', 'media_type')
    search_fields = ('id', 'person_id', 'media_type',)
    list_per_page = 10
    ordering = ('id', 'person_id', 'media_type',)


admin.site.register(PersonMedia, PersonMedias)


class PersonAudits(admin.ModelAdmin):
    list_display = ('id', 'person_id', 'cpf_new', 'audit_type', 'last_update')
    list_display_links = ('id', 'person_id', 'audit_type', 'last_update')
    search_fields = ('id', 'person_id', 'audit_type', 'last_update',)
    ordering = ('id', 'person_id', 'audit_type', 'last_update',)


admin.site.register(PersonAudit, PersonAudits)