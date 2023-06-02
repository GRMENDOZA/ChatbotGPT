from google.cloud import storage

def upload_image(image_path, bucket_name):
    """
    Sube una imagen a un depósito de Cloud Storage y devuelve la URL pública.
    """

    # Crea una instancia del cliente de almacenamiento de la nube
    storage_client = storage.Client()

    # Selecciona el depósito de Cloud Storage
    bucket = storage_client.bucket(bucket_name)

    # Genera una clave única para el nombre del objeto
    unique_filename = str(uuid.uuid4())

    # Obtén la extensión de la imagen
    extension = os.path.splitext(image_path)[1]

    # Crea el objeto en Cloud Storage con el nombre de archivo único
    blob = bucket.blob(unique_filename + extension)

    # Sube el archivo a Cloud Storage
    blob.upload_from_filename(image_path)

    # Genera la URL pública y devuelve
    url = blob.public_url
    if isinstance(url, bytes):
        url = url.decode('utf-8')
    return url

uploaded_image_url = upload_image('../static/177414078596474.png', 'example_pruebas')
print(uploaded_image_url)