# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from kennels.KennelsHandler import KennelsHandler
from kennels.models import Kennel


class KennelSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    owner = serializers.SerializerMethodField(read_only=True)
    owner_name = serializers.ReadOnlyField(source='owner.username')
    # country_club = serializers.SerializerMethodField(source='country_club.id')

    handler = KennelsHandler()

    read_only_field = ['id']

    class Meta:
        model = Kennel
        fields = ['id',
                  'url',
                  'title',
                  'type',
                  'reg_number',
                  'about',
                  'url',
                  'cover',
                  'slug',
                  'address',
                  'timezone',
                  'skype',
                  'facebook',
                  'site',
                  'owner',
                  'owner_name',
                  'country_club',
                  'country']

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)

    def validate_slug(self, value):
        slug = value.replace(' ', '_')
        kennels = self.handler.get_by_slug(slug)
        if kennels and self.instance and kennels.id != int(self.instance.id):
            raise serializers.ValidationError(_(u'This page address is already in use. Try another one'))
        return slug

    def create(self, validated_data):
        """
        Create and return a new `Kennel` instance, given the validated data.
        """
        validated_data['slug'] = self.handler.make_slug(validated_data.get('title'))
        return Kennel.objects.create(**validated_data)

    def get_owner(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            if obj.owner == request.user:
                return True
        return False

