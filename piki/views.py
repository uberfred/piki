from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from piki.models import Page

def edit_page(request, page_name):
    try:
        page = Page.objects.get(name=page_name)
    except Page.DoesNotExist:
        return render_to_response('piki/edit.html', {'page_name': page_name,
                                                'page_content': ''},
                                  context_instance=RequestContext(request))
    return render_to_response('piki/edit.html', {'page_name': page.name,
                                            'page_content': page.content},
                              context_instance=RequestContext(request))

def save_page(request, page_name):
    page_content = request.POST['page_content']
    now = datetime.now()
    try:
        page = Page.objects.get(name=page_name)
        page.content = page_content
        page.mod_date = now
    except Page.DoesNotExist:
        page = Page(name=page_name, content=page_content, pub_date=now,
                    mod_date=now)
    page.save()
    return HttpResponseRedirect('/piki/' + page_name + '/')

def view_page(request, page_name):
    try:
        page = Page.objects.get(name=page_name)
    except Page.DoesNotExist:
        return render_to_response('piki/create.html', {'page_name': page_name})
    return render_to_response('piki/view.html', {'page_name': page.name,
                                            'page_content': page.content})
