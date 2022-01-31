from app.routes.upload_image import get_image, upload_image


def init_app(app, mongo):
    upload_image(app,mongo)
    get_image(app, mongo)