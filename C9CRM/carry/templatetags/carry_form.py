# _*_coding:utf-8_*_
# Author:xupan
from django.forms.models import ModelChoiceField
from django.template import Library
from django.urls import reverse

from carry.service import carry

register = Library()


@register.inclusion_tag("carry/change_form.html")
def show_add_edit_form(form):
    def inner():
        for item in form:
            row = {'popup': False, 'item': item, 'popup_url': None}
            if isinstance(item.field, ModelChoiceField) and item.field.queryset.model in carry.site._registry:
                row['popup'] = True
                opt = item.field.queryset.model._meta
                url_name = "{0}:{1}_{2}_add".format(carry.site.namespace, opt.app_label, opt.model_name)
                row['popup_url'] = "{0}?_popup={1}".format(reverse(url_name), item.auto_id)
            yield row

    return {'form': inner()}
