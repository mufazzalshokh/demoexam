from django.views.generic import ListView

from detail.models import DetailNewsModel


class HomeListView(ListView):
    template_name = 'index.html'
    model = DetailNewsModel

    def get_queryset(self):
        qs = DetailNewsModel.objects.filter(testfield=8).latest('testfield')

        return qs

    def count_post(self, post_id):
        posts = DetailNewsModel.objects.get(id=post_id)
        posts.post_views += 1
        posts.save()
