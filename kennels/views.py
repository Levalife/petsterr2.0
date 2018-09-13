# FOR REFERENCES

# from django.utils.translation import ugettext_lazy as _
# from rest_framework import status, permissions, pagination, generics
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from animals.AnimalsHandler import AnimalsHandler
# from kennels.KennelsHandler import KennelsHandler
# from kennels.api.permissions import IsOwnerOrReadOnly
# from kennels.api.serializers import KennelSerializer
# from litters.LittersHandler import LittersHandler
#
#
# class KennelPageNumberPagination(pagination.PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'size'
#     max_page_size = 20
#
#     def get_paginated_response(self, data):
#         registered_user = False
#         user = self.request.user
#         if user.is_authenticated:
#             registered_user = True
#         context = {
#             'next': self.get_next_link(),
#             'previous': self.get_previous_link(),
#             'count': self.page.paginator.count,
#             'registered_user': registered_user,
#             'results': data
#         }
#         return Response(context)
#
#
# class KennelView(GenericAPIView):
#     handler = KennelsHandler()
#     animals_handler = AnimalsHandler()
#     litters_handler = LittersHandler()
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
#
#     def get(self, request, *args, **kwargs):
#         kennel = self.handler.get_by_slug(kwargs.get('slug'))
#         if kennel:
#             serializer = KennelSerializer(kennel, context=dict(request=request))
#             return Response(dict(result=True, kennel=serializer.data))
#         return Response(dict(result=False, detail=_('Not Found')), status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, format=None, *args, **kwargs):
#         kennel = self.handler.get_by_slug(kwargs.get('slug'))
#         serializer = KennelSerializer(kennel, data=request.data, context=dict(request=request))
#         if serializer.is_valid():
#             serializer.save()
#             return Response(dict(result=True, kennel=serializer.data))
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, format=None, *args, **kwargs):
#         kennel = self.handler.get_by_slug(kwargs.get('slug'))
#         kennel.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class KennelsView(generics.ListCreateAPIView):
#     handler = KennelsHandler()
#
#     queryset            = handler.get_all()
#     serializer_class    = KennelSerializer
#     permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
#     pagination_class    = KennelPageNumberPagination
#
#     # def get(self, request, format=None, *args, **kwargs):
#     #     kennels_list = self.handler.get_all()
#     #     serializer = KennelSerializer(kennels_list, many=True, context=dict(request=request))
#     #     return Response(dict(result=True, kennels=serializer.data))
#
#     def post(self, request, format=None, *args, **kwargs):
#         serializer = KennelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=self.request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
