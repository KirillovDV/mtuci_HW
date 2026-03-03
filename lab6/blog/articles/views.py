from django.http import Http404
from django.shortcuts import render, redirect
from .models import Article
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get('username', '').strip(),
            'password': request.POST.get('password', '').strip()
        }

        if form['username'] and form['password']:
            user = authenticate(username=form['username'], password=form['password'])
            if user is not None and user.is_active:
                login(request, user)
                return redirect('archive')
            else:
                form['errors'] = "Неверный логин или пароль"
        else:
            form['errors'] = "Не все поля заполнены"

        return render(request, 'login.html', {'form': form})

    return render(request, 'login.html', {'form': {}})


def logout_user(request):
    logout(request)
    return redirect('archive')


def register_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get('username', '').strip(),
            'email': request.POST.get('email', '').strip(),
            'password': request.POST.get('password', '').strip()
        }

        if form['username'] and form['email'] and form['password']:
            # проверка уникальности username
            if User.objects.filter(username=form['username']).exists():
                form['errors'] = "Пользователь с таким именем уже существует"
                return render(request, 'register.html', {'form': form})

            user = User.objects.create_user(form['username'], form['email'], form['password'])
            login(request, user)
            return redirect('archive')
        else:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': {}})


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
