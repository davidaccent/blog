from wtforms import fields, form, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.ext.sqlalchemy.orm import model_form
from wtforms_alchemy import ModelForm as BaseModelForm


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(cls):
        from starlette_core.database import Session

        return Session()


class BlogForm(form.Form):
    title = fields.StringField(validators=[validators.InputRequired()])
    meta_description = fields.StringField(validators=[validators.optional()])
    author = fields.StringField(validators=[validators.InputRequired()])
    post_body = fields.StringField(validators=[validators.optional()])
