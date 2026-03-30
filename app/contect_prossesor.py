from .models import News, Category, ContactData


def lasted_news(request):
    print("USER in context processor:", request.user)  # terminalga chiqadi
    lasted_news = News.published.all().order_by("-publish_time")
    categories = Category.objects.all()
    contact_data = ContactData.objects.all()
    return {
        'lasted_news': lasted_news,
        'categories': categories,
        'contact_data': contact_data,
    }
