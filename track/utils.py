from django.utils.text import slugify


def track_unique_slug_generator(model_instance):
        slug = slugify(model_instance.title) + '-' + slugify(model_instance.album)
        model_class = model_instance.__class__
        while model_class._default_manager.filter(slug=slug).exists():
            object_pk = model_class._default_manager.latest('pk')
            object_pk = object_pk.pk + 1
            slug = f'{slug}-{object_pk}'

        return slug

def album_unique_slug_generator(model_instance):
        slug = slugify(model_instance.title)
        model_class = model_instance.__class__
        while model_class._default_manager.filter(slug=slug).exists():
            object_pk = model_class._default_manager.latest('pk')
            object_pk = object_pk.pk + 1
            slug = f'{slug}-{object_pk}'

        return slug

def artist_unique_slug_generator(model_instance):
        slug = slugify(model_instance.name)
        model_class = model_instance.__class__
        while model_class._default_manager.filter(slug=slug).exists():
            object_pk = model_class._default_manager.latest('pk')
            object_pk = object_pk.pk + 1
            slug = f'{slug}-{object_pk}'

        return slug