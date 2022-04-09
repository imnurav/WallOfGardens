from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from wallofgardens.views import Home, shop

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('securelogin/', admin.site.urls),
    path('', Home, name='home'),
    path('contact/', include('contact.urls')),
    path('shop/', shop, name='shop'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),

    # order URls
    path('orders/', include('orders.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
