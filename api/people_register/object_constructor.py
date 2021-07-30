from django.core.files import File
from io import BytesIO
from PIL import Image
import base64


def construct_object_model(object: str, model):
    """
    Function that will construct two objects for the PersonType and PersonMediaType Model
    """
    dict_model = model.objects.all()

    if first_round(dict_model):
        if object == 'type':
            list_person_type = ['visitante', 'empregado', 'terceirizado', 'ajudante']
            for item in list_person_type:
                item = item.upper()
                model.objects.create_type(item)
        else:
            model.objects.create_type("FOTO")
            model.objects.create_type("BIOMETRIA")


def first_round(dict_model: dict):
    """
    Check the length of model dictionary
    """
    return len(dict_model) <= 1


def compress_image(image):
    """ Compress image """
    im = Image.open(image)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im_io = BytesIO()
    im.save(im_io, 'jpeg', quality=15, optimize=False)
    new_image = File(im_io, name=image.name)

    return new_image


def convert_to_b64(image_parm):
    """ Convert image to Base 64 """
    image_read = image_parm.read()
    image_b64 = base64.encodebytes(image_read)
    return image_b64