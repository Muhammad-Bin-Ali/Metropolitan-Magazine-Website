from django.urls import path
from .views import News, SearchView, AddUrlToFeed
# NewsPublisher, NewsPublisherCategory

urlpatterns = [
	path('', News.as_view(), name = 'news'),
    path('search/', SearchView.as_view(), name = 'search-results'),
    path('addurl/', AddUrlToFeed.as_view(), name = 'add-url'),

]
