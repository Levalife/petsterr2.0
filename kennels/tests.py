from django.test import TestCase

from kennels.KennelsHandler import KennelsHandler


class KennelTest(TestCase):
    handler = KennelsHandler()

    def test_create_model(self):
        kennel = self.handler.create(dict(title="test 1", type="dogs"))
        self.assertEqual(kennel.title, "test 1")
        self.assertEqual(kennel.type, "dogs")
        self.assertEqual(kennel.slug, "test_1")

    def test_get_by_slug(self):
        kennel_1 = self.handler.create(dict(title="test 1", type="dogs"))
        kennel_2 = self.handler.get_by_slug("test_1")

        self.assertEqual(kennel_1, kennel_2)
        self.assertEqual(kennel_1.title, kennel_2.title)

    def test_get_by_id(self):

        kennel_1 = self.handler.create(dict(title="test 1", type="dogs"))

        kennel_2 = self.handler.get_by_id(1)

        self.assertEqual(kennel_1, kennel_2)
        self.assertEqual(kennel_1.id, kennel_2.id)
        self.assertEqual(kennel_1.title, kennel_2.title)

    def test_make_slug(self):

        slug = self.handler.make_slug('test_1')

        self.assertEqual(slug, "test_1")

        kennel = self.handler.create(dict(title="test 2", type="dogs"))
        slug_2 = self.handler.make_slug('test 2')
        self.assertNotEqual(slug_2, "test_2")

    def test_delete(self):
        kennel_1 = self.handler.create(dict(title="test 1", type="dogs"))
        kennel_2 = self.handler.create(dict(title="test 2", type="dogs"))

        self.handler.delete(kennel_1.slug)

        kennel_1 = self.handler.get_by_slug(kennel_1.slug)
        kennel_2 = self.handler.get_by_slug(kennel_2.slug)

        self.assertTrue(kennel_1.is_deleted)
        self.assertFalse(kennel_2.is_deleted)


from django.test import Client
from django.urls import reverse

class KennelViewTest(TestCase):
    client = Client()
    handler = KennelsHandler()

    def test_get_kennel_view(self):
        kennel_1 = self.handler.create(dict(title="test 1", type="dogs"))


        response_1 = self.client.get(reverse('kennels:kennel_page', kwargs={"slug": "test_1"}))
        self.assertEqual(response_1.status_code, 200)

        response_2 = self.client.get(reverse('kennels:kennel_page', kwargs={"slug": "test_100000000000"}))
        self.assertEqual(response_2.status_code, 404)