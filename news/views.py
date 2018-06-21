from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View

from news.NewsHandler import NewsHandler
from news.forms.CreateNewsForm import CreateNewsForm


class NewsView(View):
    form_class = CreateNewsForm
    news_handler = NewsHandler()

    def get(self, request, *args, **kwargs):
        source_id = request.GET.get('source_id')
        type = request.GET.get('type')
        data = dict(source_id=source_id, type=type)
        news_list = self.news_handler.get_news_by_params(data)
        paginator = Paginator(news_list, 15)  # Show 15 contacts per page
        page = request.GET.get('page')
        news_object = paginator.get_page(page)
        dump_news = [self.news_handler.dump(news) for news in news_object.object_list]
        return JsonResponse(dict(result=True, news=dump_news, page_number=news_object.number,
                                 num_pages=news_object.paginator.num_pages))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            news = self.news_handler.create_news(form.cleaned_data, request.user)
            return JsonResponse(dict(result=True, news=self.news_handler.dump(news)))
