from app.routes.upload_image import get_image, upload_image


def init_app(app):
    upload_image(app)
    get_image(app)