from django.http import Http404
from django.shortcuts import render, redirect
from .models import Article

def archive(request):
    posts = Article.objects.all()
    return render(request, "archive.html", {"posts": posts})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, "article.html", {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    # доступ только для авторизованных пользователей
    if request.user.is_anonymous:
        raise Http404

    if request.method == "POST":
        form = {
            'title': request.POST.get("title", "").strip(),
            'text': request.POST.get("text", "").strip()
        }

        if form["title"] and form["text"]:
            # проверка уникальности названия
            if Article.objects.filter(title=form["title"]).exists():
                form["errors"] = u"Статья с таким названием уже существует"
                return render(request, 'create_post.html', {'form': form})

            article = Article.objects.create(
                title=form["title"],
                text=form["text"],
                author=request.user
            )
            return redirect('get_article', article_id=article.id)
        else:
            form["errors"] = u"Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})

    # GET: показать пустую форму
    return render(request, 'create_post.html', {'form': {}})
