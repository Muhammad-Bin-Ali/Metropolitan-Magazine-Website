from django.shortcuts import render
from django.views.generic import ListView, View
from main_news.models import NewsPost
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from .models import ReadLater
from main_news.models import NewsPost
from .forms import Populate_ReadLater
import json


class ReadLater_Ajax(View): 
    form_class = Populate_ReadLater

    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            post_id = request.POST.get('post')
            post_ = NewsPost.objects.filter(id=post_id).get()
            user_ = User.objects.filter(username=request.POST.get("user")).get().id  #uses name of user to find obj in DB (passed through POST), and then find pk
            form = self.form_class({'user':user_, 'post':post_})
            if form.is_valid():
                if ReadLater.objects.filter(user=user_, post=post_).exists():
                    ReadLater.objects.filter(user=user_, post=post_).delete()
                    print('post already existed. Now Removed')
                    return JsonResponse({'post_id':post_id}, status=200)
                form.save()
                print(True)
                return JsonResponse({'post_id':post_id}, status=200)
        else:
            print(False)
            return False

class ReadLaterView(LoginRequiredMixin, ListView):
    model = NewsPost
    template_name = 'read_later/read_later.html'

    def get_queryset(self):
        user = self.request.user.id
        read_later_list = ReadLater.objects.filter(user_id=user).all()
        context_list = []
        for object_ in read_later_list:
            post_id = object_.post.id
            post = NewsPost.objects.filter(id=post_id).get()
            context_list.append(post)
        return context_list

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_list = self.get_queryset()
        context['read_later_posts'] = context_list
        return context

        




