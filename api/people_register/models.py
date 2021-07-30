from django.db import models
from datetime import datetime
from people_register.object_constructor import construct_object_model, compress_image, convert_to_b64


class PersonTypeManager(models.Manager):
    def create_type(self, name):
        type = self.create(person_type=name)
        return type


class PersonType(models.Model):
    person_type = models.CharField(max_length=32, blank=False, null=False)
    objects = PersonTypeManager()

    def __str__(self):
        return self.person_type


class PersonMediaTypeManager(models.Manager):
    def create_type(self, name):
        type = self.create(media_type=name)
        return type


class PersonMediaType(models.Model):
    media_type = models.CharField(max_length=32, blank=False, null=False)
    objects = PersonMediaTypeManager()

    def __str__(self):
        return self.media_type


class Person(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=32, blank=False, null=False)
    person_type = models.ForeignKey(PersonType, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, blank=False, null=False, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    company = models.CharField(max_length=32, blank=False, null=False)
    last_update = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class PersonMedia(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    media = models.ImageField(blank=True)
    object_media = models.TextField(null=False)
    media_type = models.ForeignKey(PersonMediaType, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, *args, **kwargs):
        if self.media:
            image = self.media
            if image.size > 0.2445 * 1024 * 1024:
                self.media = compress_image(image)

                image_read = self.media.open(mode='rb')
                self.object_media = convert_to_b64(image_read)

        super(PersonMedia, self).save(*args, **kwargs)


class PersonAudit(models.Model):
    AUDIT_TYPE = (
        (1, 'Addition'),
        (2, 'Update')
    )

    person_id = models.BigIntegerField(blank=False, null=False)
    audit_type = models.IntegerField(blank=False, choices=AUDIT_TYPE, null=False)
    cpf_new = models.CharField(max_length=14, blank=False, null=False)
    cpf_old = models.CharField(max_length=14)
    last_update = models.DateTimeField(default=datetime.now, blank=True)


construct_object_model('type', PersonType)
construct_object_model('mediatype', PersonMediaType)
