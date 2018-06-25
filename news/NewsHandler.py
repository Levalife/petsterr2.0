# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from base.BaseHandler import BaseHandler
from news.models import BaseNews


class NewsHandler(BaseHandler):
    model_instance = BaseNews

    def create_news(self, data, user):
        news = self.model_instance(**data, author=user)
        news.save()
        return news

    def get_news_by_params(self, params, order_by='-created_at'):
        return self.model_instance.objects.filter(**params, is_deleted=False).order_by(order_by)

    def get_dump_news_by_params(self, params, order_by='-created_at'):
        news_list = self.get_news_by_params(params, order_by)
        return [self.dump(news) for news in news_list]

    def delete(self, id):
        try:
            news = self.model_instance.objects.get(id=id)
            news.is_deleted = True
            news.save()
        except self.model_instance.DoesNotExist:
            pass

    def dump(self, news):
        plain_data = dict()
        plain_data['content'] = news.content
        plain_data['author'] = '{} {}'.format(news.author.first_name, news.author.last_name) if \
            news.author.first_name else news.author.username
        plain_data['created_at'] = news.created_at.strftime('%d.%m.%Y')
        return plain_data