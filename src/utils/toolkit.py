from app import db
from utils.errors import ValidationError


class Toolkit:
    @staticmethod
    def commit():
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    @staticmethod
    def check_necessary(**kwargs):
        for k, v in kwargs.items():
            if not v:
                raise ValidationError(message=f'{k} is necessary')
