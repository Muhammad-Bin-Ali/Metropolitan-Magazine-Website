from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import NewsPost
from .parse_function import parseRSSfeeds
from django.contrib.postgres.search import SearchVector
from newscatcher import Newscatcher
from django.http import HttpResponseRedirect
from .forms import AddFeedForm
from .rss_url_validator import validate_url


class News(ListView):
	# paginate_by = 10
	model = NewsPost
	template_name = 'main_news/main_news_app.html'
	context_object_name = 'posts' 
	ordering = ['-date_published']

	# def get_queryset(self):
	# 	print(self.request.POST)
	# 	return 

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['posts'] = NewsPost.objects.all()
		context['form'] = AddFeedForm()
		return context

class AddUrlToFeed(FormView):
	template_name = "main_news/test_add_url.html"
	form_class = AddFeedForm
	success_url = '/news/addurl/'
	
	def form_valid(self, form):
		print(self.request.POST.get('feed_url'))

		return super().form_valid(form)


class SearchView(ListView):
	model = NewsPost
	template_name = 'main_news/main_news_app_search.html'
	context_object_name = 'posts' 
	ordering = ['-date_published']

	def get_queryset(self):
		query = self.request.GET.get('q')
		entries = NewsPost.objects.annotate(search=SearchVector(
			'headline', 'description', 'publisher', 'date_published', 'category')
		).filter(search=query.lower())
		return entries

	def get_context_data(self, **kwargs):
	 	context = super().get_context_data(**kwargs)
	 	context['posts'] = self.get_queryset()
	 	return context





# class NewsPublisher(ListView):
# 	model = NewsPost
# 	template_name = 'main_news/main_news_app_test.html'

# 	def get_context_data(self, **kwargs):
# 		print(**kwargs)
# 		context = super().get_context_data(**kwargs)
# 		context['posts'] = NewsPost.objects.filter(publisher = self.kwargs['publisher'])
# 		context['chosen_pub'] = self.kwargs['publisher']
# 		context['categories'] = NewsPost.objects.filter(publisher = self.kwargs['publisher']).values('category').distinct()
# 		return context

# class NewsPublisherCategory(ListView):
# 	models = NewsPost
# 	template_name = 'main_news/main_news_app_test_category'
	

	# def get_context_data(self, **kwargs):
	# #  	context = super().get_context_data(**kwargs)
	# #  	#context['posts'] = NewsPost.objects.filter(publisher = self.kwargs['publisher'], category = self.kwargs['category'])
	# #  	#context['publishers'] = NewsPost.objects.values('publisher').distinct()
	#   	context['publisher'] = self.kwargs['publisher']
	# #  	return context


		#post__ = parseRSSfeeds()
	# for item in post__:
	# 	item = NewsPost(
	# 		headline = item['headline'], 
	# 		link = item['link'], 
	# 		image_url = item['image_url'],	
	# 		publisher = item['publisher'],
	# 		date_published = item['date'],
	# 		description = item['description'],
	# 		category = item['category']
	# 		)
	# 	item.save()