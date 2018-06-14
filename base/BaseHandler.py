# -*- coding: utf-8 -*-


class BaseHandler:
    model_instance = None

    def get_by_id(self,id):
        item = self.model_instance.objects.get(id=id)
        return item