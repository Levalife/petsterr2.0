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

    def get_all(self, order_by='created_at'):
        return self.model_instance.objects.filter(is_deleted=False).order_by(order_by)

    @staticmethod
    def parse_serializer_errors(errors):
        return ['/n'.join(error) for error in errors.values()]