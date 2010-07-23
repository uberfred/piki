from django.forms import ModelForm

class Page(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('last modified')

    def __unicode__(self):
        return self.name

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['content']