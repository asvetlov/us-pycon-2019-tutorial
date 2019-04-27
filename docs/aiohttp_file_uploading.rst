aiohttp file uploading
=======================

Blog post can have images, let's support them!

Extend Post structure
---------------------

Add ``image BLOB`` field.

+------------+-----------------+--------+
| Field      | Description     | Type   |
+============+=================+========+
| id         |  Post id        | int    |
+------------+-----------------+--------+
| title      | Title           | str    |
+------------+-----------------+--------+
| text       | Content         | str    |
+------------+-----------------+--------+
| owner      | Post creator    | str    |
+------------+-----------------+--------+
| editor     | Last editor     | str    |
+------------+-----------------+--------+
| **image**  | Image content   | bytes  |
+------------+-----------------+--------+

.. note::

   Usually you serve images by *Content Delivery Network* or save them on *BLOB storage*
   like *Amazon S3*. Database keeps an image URL only.

   But for sake of simplicity we use database for storing the *image content*.


Image web handler
-----------------

.. literalinclude:: ../code/07-file-uploading/01-file-uploading.py
   :pyobject: render_post_image

Return a black image if nothing is present in DB, the image content with ``image/jpeg``
content type otherwise.

To render image we need to change ``view.html`` template:

.. literalinclude:: ../code/07-file-uploading/templates/view.html

Upload form
-----------

Add ``<input type="file" name="image" accept="image/png, image/jpeg">`` HTML form field:

.. literalinclude:: ../code/07-file-uploading/templates/edit.html


Handle uploaded image
---------------------

.. literalinclude:: ../code/07-file-uploading/01-file-uploading.py
   :pyobject: edit_post_apply

If a new image was provided by HTML form -- update DB:

.. literalinclude:: ../code/07-file-uploading/01-file-uploading.py
   :pyobject: apply_image


Full example for server with images support
---------------------------------------------

Example for HTML version of blogs server with images: :ref:`full-image-upload-server`

.. toctree::
   :hidden:

   aiohttp_images_upload_full
