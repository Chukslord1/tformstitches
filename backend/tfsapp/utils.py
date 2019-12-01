<<<<<<< HEAD
from django.utils.text import slugify

def unique_slug_generator(model_instance, title, slug_field):
    """
    :param model_instance:
    :param title:
    :param slug_field:
    :return:
    """

    slug = slugify(title)
    model_class = model_instance.__class__

    while model_class._default_manager.filter(slug=slug).exists():
        object_pk = model_class._default_manager.latest('pk')
        object_pk = object_pk.pk + 1
        slug = f'{slug}-{object_pk}'

    return slug
=======
from django.utils.text import slugify

def unique_slug_generator(model_instance, title, slug_field):
    """
    :param model_instance:
    :param title:
    :param slug_field:
    :return:
    """

    slug = slugify(title)
    model_class = model_instance.__class__

    while model_class._default_manager.filter(slug=slug).exists():
        object_pk = model_class._default_manager.latest('pk')
        object_pk = object_pk.pk + 1
        slug = f'{slug}-{object_pk}'

    return slug
>>>>>>> e02e672991c01fb3cf85b969aa70585e1cfe48be
