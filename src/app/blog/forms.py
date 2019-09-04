from wtforms import ValidationError, fields, form, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.ext.sqlalchemy.orm import model_form
from wtforms_alchemy import ModelForm as BaseModelForm

from app.blog.tables import Blog


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(cls):
        from starlette_core.database import Session

        return Session()


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        only = ["title", "meta_description", "author", "post_body", "is_live"]

    def validate_is_live(form, field):
        if (
            any([form.meta_description.data == "", form.post_body.data == ""])
            and field.data
        ):
            raise ValidationError("All field must be complete to set blog as live")
