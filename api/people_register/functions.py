from people_register.models import *
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import serializers
from datetime import datetime


def upper_case(string: str):
    """ Transform a string to upper case """
    return string.upper()


def check_duplicate_person_type(data: dict):
    """ Check if new the person type is already registered"""
    types = get_list_or_404(PersonType, person_type=data['person_type'])
    if len(types) > 0:
        raise serializers.ValidationError({'Person Type': 'Person Type already registered in the database'})


def id_generator():
    """ Person ID generator """
    people = Person.objects.all().order_by('-last_update')
    if len(people) == 0:
        id = 1
    else:
        id = people[0].id + 1
    return id


def trigger_audit(data: dict):
    """ Trigger function for the audit database """
    if not audit_exist(data['id']):
        create_audit(data)


def audit_exist(id: int):
    """ Check if a person has already been registered in the audit database """
    audit = PersonAudit.objects.filter(person_id=id)
    return len(audit) > 1


def create_audit(data: dict):
    """ Create a new audit register for the person_id """
    audit = PersonAudit()
    audit.person_id = data['id']
    audit.audit_type = 1
    audit.cpf_new = data['cpf']
    audit.last_update = datetime.now()
    audit.save()


def update_audit(instance, data):
    """ Update audit register with the new data """
    cpf_old = 0
    change = False

    audit_exist = PersonAudit.objects.all().filter(person_id=instance.id).order_by('-last_update')

    if change_cpf(instance.cpf, data['cpf']):
        change = True
        for item in audit_exist:
            if item.cpf_new != '':
                cpf_old = item.cpf_new
                break

    audit = PersonAudit()
    audit.person_id = instance.id

    if change:
        audit.cpf_new = data['cpf']

    audit.cpf_old = cpf_old
    audit.audit_type = 2
    audit.last_update = datetime.now()
    audit.save()


def change_cpf(cpf, cpf_new):
    """ Check if there was an CPF change """
    return cpf != cpf_new


def update_person_data(instance, validated_data):
    person_register = get_object_or_404(Person, id=instance.id)

    person_register.name = upper_case(validated_data['name'])
    person_register.cpf = validated_data['cpf']
    person_register.person_type = validated_data['person_type']
    person_register.phone = validated_data['phone']
    person_register.company = validated_data['company']
    person_register.last_update = datetime.now()

    return validated_data