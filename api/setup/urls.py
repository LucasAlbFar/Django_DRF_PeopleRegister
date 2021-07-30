from django.contrib import admin
from django.urls import path, include
from people_register.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="People Register",
      default_version='v1',
      description="People Register is aiming the task of record a new reponsible person in the establishment",
      terms_of_service="#",
      contact=openapi.Contact(email="lucasalbfar@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register('type', PersonTypeViewSets, basename='type')
router.register('mediatype', PersonMediaTypeViewSets, basename='mediatype')
router.register('person', PersonViewSets, basename='person')
router.register('media', PersonMediaViewSets, basename='media')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('audit/', ListAuditViewSets.as_view(), name='audit'),
    path('listaudit/<int:pk>/', ListAuditPersonViewSets.as_view(), name='list_person_audit'),
    path('listperson/<int:cpf>/', ListPersonViewSets.as_view(), name='list_person'),
    path('listmedia/<int:pk>/', ListMediaPersonViewSets.as_view(), name='list_person'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
