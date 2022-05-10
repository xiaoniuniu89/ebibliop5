from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO
import string
from django.utils.crypto import get_random_string
import store.models


# the solution for creating unique slugs was found in this stack overflow thread https://stackoverflow.com/questions/3816307/how-to-create-a-unique-slug-in-django
def unique_slugify(instance, slug):
    """ checks if a product has unique slug, if not will add random 4 character string to the slug"""
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + get_random_string(length=4)
    return unique_slug

image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}

# this solution for resizing images uploaded to amazon s3 was taken from https://blog.soards.me/posts/resize-image-on-save-in-django-before-sending-to-amazon-s3/
def image_resize(image, width, height):
    """ takes an image uploaded to the site and resizes if too big"""
    # Open the image using Pillow
    img = Image.open(image)
    # check if either the width or height is greater than the max
    if img.width > width or img.height > height:
        output_size = (width, height)
        # Create a new resized “thumbnail” version of the image with Pillow
        img.thumbnail(output_size)
        # Find the file name of the image
        img_filename = Path(image.file.name).name
        # Spilt the filename on “.” to get the file extension only
        img_suffix = Path(image.file.name).name.split(".")[-1]
        # Use the file extension to determine the file type from the image_types dictionary
        img_format = image_types[img_suffix]
        # Save the resized image into the buffer, noting the correct file type
        buffer = BytesIO()
        img.save(buffer, format=img_format)
        # Wrap the buffer in File object
        file_object = File(buffer)
        # Save the new resized file as usual, which will save to S3 using django-storages
        image.save(img_filename, file_object)

def update_image_url(books):
    """updates image_url which is a url on aws s3 bucket that expires after a time."""
    for book in books:
        book = store.models.Product.objects.get(id=book['id'])
        book.image_url = book.image.url
        book.save()