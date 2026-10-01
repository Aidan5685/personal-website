from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def home_page_view(request):
    return HttpResponse("Homepage")


def about_page_view(request):
    context = {
        "name": "Aidan",
        "age": 19,
    }
    return render(request, "pages/about.html", context)


class ProductsPageView(TemplateView):
    template_name = "pages/products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = [
            "Product 1",
            "Product 2",
            "Product 3",
            "Product 4",
        ]
        return context