from import_export import resources
from news_processor.models import News


class NewsResources(resources.ModelResource):
    class Meta:
        model = News
        exclude = ('published_time', 'news_type',)
        # fields = ('id', 'author', 'url','headline','summary')
        # export_order = ('id', 'author', 'url','headline','summary')
