from .models import *


def sidebar(request):
    context = {
        "categories": Category.objects.all(),
    }
    return context
