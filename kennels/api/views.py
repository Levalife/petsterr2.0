# -*- coding: utf-8 -*-
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from rest_framework import generics, status, pagination
from rest_framework.response import Response

from kennels.api.permissions import IsOwnerOrReadOnly
from kennels.api.serializers import KennelSerializer
from kennels.KennelsHandler import KennelsHandler


class KennelPageNumberPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 20

    def get_paginated_response(self, data):
        registered_user = False
        user = self.request.user
        if user.is_authenticated:
            registered_user = True
        context = {
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'registered_user': registered_user,
            'results': data
        }
        return Response(context)


class KennelAPIView(generics.ListCreateAPIView):
    handler = KennelsHandler()

    lookup_field = 'slug'
    serializer_class = KennelSerializer
    pagination_class = KennelPageNumberPagination

    def get_queryset(self):
        query = self.request.GET
        params = dict()
        for key, value in query.items():
            params[key] = value
        return self.handler.get_all_by_params(params=params, order_by='-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class KennelRUDView(generics.RetrieveUpdateDestroyAPIView):
    handler = KennelsHandler()

    lookup_field = 'slug'
    serializer_class = KennelSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return self.handler.get_all_by_params(params={}, order_by='title')

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
