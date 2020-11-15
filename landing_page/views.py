from django.shortcuts import render
from main_news.models import NewsPost


def templanding(request):
	context = {
		"publishers" : NewsPost.objects.values('publisher').distinct(),
		"categories" : NewsPost.objects.values('category').distinct(),
	}
	return render(request, 'landing_page/landing_page.html', context)