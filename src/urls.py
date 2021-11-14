from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from api.urls import router as api_router
from django.conf import settings
from django.conf.urls.static import static
from api.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    path('api/', include(api_router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('home.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
