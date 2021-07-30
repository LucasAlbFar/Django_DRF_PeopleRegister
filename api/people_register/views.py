from rest_framework import viewsets, generics, filters
from people_register.serializer import *
from django_filters.rest_framework import DjangoFilterBackend


class PersonTypeViewSets(viewsets.ModelViewSet):
    """
    Display and register types of a person
    """
    queryset = PersonType.objects.all()
    serializer_class = PersonTypeSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['person_type', ]
    search_fields = ['person_type', ]


class PersonMediaTypeViewSets(viewsets.ModelViewSet):
    """
    Display media's objects types
    """

    queryset = PersonMediaType.objects.all()
    serializer_class = PersonMediaTypeSerializer
    http_method_names = ['get']

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['media_type', ]
    search_fields = ['media_type', ]


class PersonViewSets(viewsets.ModelViewSet):
    """
    Register and update data from a person
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ['get', 'post', 'patch']

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'person_type', 'cpf', 'last_update', ]


class PersonMediaViewSets(viewsets.ModelViewSet):
    """
    Register the people's media object
    """
    queryset = PersonMedia.objects.all()
    serializer_class = PersonMediaSerializer
    http_method_names = ['get', 'post', 'patch']

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['person_id',]


class ListAuditViewSets(generics.ListAPIView):
    """
    Display all the audit registered
    """

    queryset = PersonAudit.objects.all().order_by('-last_update')
    serializer_class = PersonAuditSerializer


class ListPersonViewSets(generics.ListAPIView):
    """
    Display a person register
    """

    def get_queryset(self):
        queryset = Person.objects.filter(cpf=self.kwargs['cpf']).order_by('-last_update')
        return queryset

    serializer_class = ListPeopleSerializer


class ListAuditPersonViewSets(generics.ListAPIView):
    """
    Display all audit register for a person
    """

    def get_queryset(self):
        queryset = PersonAudit.objects.filter(person_id=self.kwargs['pk']).order_by('-last_update')
        return queryset

    serializer_class = PersonAuditSerializer


class ListMediaPersonViewSets(generics.ListAPIView):
    """
    Display all audit register for a person
    """

    def get_queryset(self):
        queryset = PersonMedia.objects.filter(person_id=self.kwargs['pk'])
        return queryset

    serializer_class = PersonMediaSerializer
