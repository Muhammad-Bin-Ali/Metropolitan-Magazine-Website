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
                form.save()
                print(True)
                return JsonResponse({}, status=200)
        else:
            print(False)
            return False
        # if self.request.is_ajax:
        #     post_id = request.POST.get('post')
        #     return JsonResponse({"post_id": post_id}, status=200)
        # else:
        #     return JsonResponse({"error": ""}, status=400)


# class ReadLater(LoginRequiredMixin, ListView):
#     # model = NewsPost
#     template_name = 'read_later/read_later.html'
#     # # form_class = Populate_ReadLater
    
#     def post(self, request, *args, **kwargs):
#     #     # post_id = self.request.POST.get('test')
#     #     # post_ = NewsPost.objects.filter(id=post_id).get()
#     #     # user_ = self.request.user.id
#     #     # form = self.form_class({'user':user_, 'post':post_})
#     #     # if form.is_valid():
#     #     #     # form.save()
#     #     #     print(True)
#     #     #     return render(request, self.template_name)
#     #     # else:
#     #     #     print(False)
#             return render(request, self.template_name)




