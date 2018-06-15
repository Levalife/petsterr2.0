# -*- coding: utf-8 -*-


class BaseHandler:
    model_instance = None

    def create(self, data):
        item = self.model_instance(**data)
        item.save()
        return item

    def get_by_id(self,id):
        item = self.model_instance.objects.get(id=id)
        return item