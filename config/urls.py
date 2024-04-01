from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from core.views import AutorViewSet, CategoriaViewSet, EditoraViewSet, LivroViewSet, CompraViewSet

from usuario.router import router as usuario_router

from uploader.router import router as uploader_router

from usuario.views import UsuarioViewSet

from usuario.auth import AuthRegister, AuthLogin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = DefaultRouter()

router.register(r"autores", AutorViewSet, basename="autores")
router.register(r"categorias", CategoriaViewSet, basename="categorias")
router.register(r"editoras", EditoraViewSet, basename="editoras")
router.register(r"livros", LivroViewSet, basename="livros")
router.register(r"users", UsuarioViewSet, basename="users")
router.register(r"compras", CompraViewSet, basename="compras")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("users/", include(usuario_router.urls)),
    path("api/register/", AuthRegister, name="AuthRegister"),
    path("api/login/", AuthLogin, name="AuthLogin"),
    path("api/media/", include(uploader_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)