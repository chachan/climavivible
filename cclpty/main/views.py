#!/usr/bin/env python
# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from django.views.generic import TemplateView
from contact.forms import ContactForm


class ContextForm(object):
    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        kwargs['form_contact'] = ContactForm()
        kwargs['hello'] = 'hello'
        return kwargs


class IndexView(ContextForm, TemplateView):
    template_name = "index.html"


class VolunteersView(TemplateView, ContextForm):
    template_name = "voluntarios/index.html"


class TariffView(TemplateView, ContextForm):
    template_name = "tarifas/index.html"


class JoinUpView(TemplateView, ContextForm):
    template_name = "unete/index.html"

