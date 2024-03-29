from django.shortcuts import render, get_object_or_404
from .models import Post, Group

LIMITER: int = 10


def index(request):
    posts = Post.objects.all().select_related('author', 'group')[:LIMITER]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.all().select_related('author', 'group')[:LIMITER]
    context = {
        'group': group,
        'posts': posts}
    return render(request, 'posts/group_list.html', context)
