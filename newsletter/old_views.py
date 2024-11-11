from django.shortcuts import render, redirect
from django.views import View
from .models import SubUsers, newsletter
from .forms import SubForm, AddLetter
from django.contrib import messages
from django.views.generic import CreateView, DetailView, ListView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.

# class HomePageView(View):
#     template_name = 'newsletter/index.html'

#     def get(self, request):
        
#         return render(request, self.template_name)
    
class HomePageView(View):

    template_name = 'newsletter/index.html'

    def get(self, request):
        form = SubForm()

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = SubForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You've successfully subscribed!")
            return HttpResponse('done!')
        
class News2(CreateView):

    template_name = 'newsletter/news.html'
    model = newsletter
    fields = '__all__'

class Newslist(ListView):
    model = newsletter
    template_name = 'newsletter/newslist.html'

def news_detail(request, pk):
    template_name = 'newslist.html'
    news_item = get_object_or_404(Newslist, pk=pk)
    print(news_item)
    return render(request, template_name, {'news_item': news_item})


class Main_news(DetailView):

    template_name = 'newsletter/detail_news.html'
    model = newsletter

    def get(request, pk):
        news_item = get_object_or_404(Main_news, pk=pk)
        return render(request, 'news_detail.html', {'news_item': news_item})

# class News(View):
    
    template_name = 'newsletter/news.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        form = AddLetter(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('time to send to email')