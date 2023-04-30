from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.dashboard),
    path("about/", views.about, name="about"),
    path("support/", views.support, name="support"),
    path("product/<int:product_id>/", views.product, name="product"),
    path("purchase/", views.purchase, name="purchase"),
    path("categories/", views.categories, name="categories"),
    path("categories/Oil-Painting", views.oil_painting, name="Oil-Painting"),
    path("categories/Watercolors", views.Watercolors, name="Watercolors"),
    path("categories/Dry-Crayons", views.Dry_Crayons, name="Dry-Crayons"),
    path("categories/Oil-Crayons", views.Oil_Crayons, name="Oil-Crayons"),
    path("404/", TemplateView.as_view(template_name="404.html"), name="404"),
]
handler404 = "Rangel_portfolio.views.handler404"
