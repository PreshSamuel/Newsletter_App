from django.shortcuts import render, redirect
from django.views import View
from .models import SubUsers, newsletter
from .forms import SubForm, AddLetter

class HomePage(View):
    template_name = 'newsletter/index.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        email = request.POST['email']
        user = SubUsers.objects.create(email=email)
        user.save()
        return redirect('newsletter:newsletter_view')

class NewsletterView(View):

    template_name = 'newsletter/news.html'

    def get(self, request):
        context = {
            "form": AddLetter()
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        newsletter = AddLetter(request.POST)
        if newsletter.is_valid():
            newsletter.save()
            return redirect('newsletter:news_list')
        else:
            return redirect('newsletter:newsletter_view')

class NewsList(View):
    queryset = newsletter.objects.all()
    template_name = 'newsletter/news_list.html'

    def get(self, request):
        context = {
            "newsletters": self.queryset
        }
        return render(request, self.template_name, context=context)