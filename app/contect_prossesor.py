from .models import News, Category, ContactData


def lasted_news(request):
    """Provide shared news, category, and contact data to templates."""
    return {
        'lasted_news': News.published.all().order_by('-publish_time'),
        'categories': Category.objects.all(),
        'contact_data': ContactData.objects.all(),
    }
