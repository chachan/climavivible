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

from contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from contact.models import Contact


class ContactView(View):
    template_name = 'index.html'
    form_class = ContactForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            contact = Contact(
                name=request.POST.get('name'),
                subject=request.POST.get('subject'),
                email=request.POST.get('email'),
                message=request.POST.get('message'),
            )
            contact.put()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})


