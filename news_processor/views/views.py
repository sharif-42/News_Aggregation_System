from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base.html'

    def get(self, request):
        #BanglaNews.objects.insert_sports_news()
        # mst = BanglaNews.objects.filter(news_category = 'Sports')
        # post = BanglaNews.objects.all().order_by('publish_time')
        h1 = "সর্বশেষ খবর"
        h2 = "সর্বাধিক পঠিত"
        return Response({'h1':h1,'h2':h2}, status=status.HTTP_200_OK)
