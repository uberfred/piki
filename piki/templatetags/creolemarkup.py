from django import template
from django.utils.safestring import mark_safe
from creoleparser.core import Parser
from creoleparser.dialects import create_dialect, creole11_base

register = template.Library()
text2html = Parser(
   dialect=create_dialect(creole11_base, wiki_links_base_url='/piki/',
                          blog_style_endings=True), method='html')

@register.filter
def creole(value):
   print text2html(value)
   return text2html(value)