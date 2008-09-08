from django.shortcuts import get_object_or_404, render_to_response

from denklab.articles.models import Article

def article_detail(request, year, month, slug):
    article = get_object_or_404(Article,
        published__year=year,
        published__month=month, 
        slug=slug)

    return render_to_response('articles/article_detail.html',
        {'article': article})
