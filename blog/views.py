from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def post_list(request):
    """
    Renders a list of all posts with pagination.
    Retrieves all posts from the database, paginates them by 5 posts per page,
    and renders them to the 'post_list.html' template.
    """
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})


def post_detail(request, post_id):
    """
    Renders the detail view of a single post.
    Fetches a post by its ID or returns a 404 error if not found. Renders the
    'post_detail.html' template with the post data.
    """
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def edit_post(request, post_id):
    """
    Handles the editing of an existing post.
    Fetches a post by its ID for editing. If the form is submitted via POST and
    is valid, the post is saved and the user is redirected to the post's
    detail view.
    Otherwise, the 'edit_post.html' template is rendered with the form.
    """
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})


@login_required
def create_article(request):
    """
    Allows a staff member to create a new article.
    If the user is not staff, redirects to the post list.
    Otherwise, if the form is submitted via POST and is valid,
    a new article is created and the user is
    redirected to the new article's detail view. If the form is not submitted,
    the 'create_article.html' template is rendered with an empty form.
    """
    if not request.user.is_staff:
        return redirect('post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster_name = request.user.username
            post.save()
            return redirect('post_detail', post.id)
    else:
        form = PostForm()
    return render(request, 'blog/create_article.html', {'form': form})
