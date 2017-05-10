from django.shortcuts import render,get_object_or_404,redirect
from  django.utils import timezone
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
# for function based views to automatically activate the login required fucntionality use decorators
from django.contrib.auth.decorators import login_required
# for class based views to automatically activate the login required fucntionality use mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,
                                    UpdateView,DeleteView)

# class based views for the blog posts
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    #this queryset will fetch all the post form model whose publish date is less
    #than or equal to current time and orber by in descending order by using '-'
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

#after deletion of post user will be redirected to the home page i.e list of posts
class DeletePostView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

#draft post which has not yet been published_date
class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

##Function views
#fucntion view for the publish post
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

# function based views for the blog comment
@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #grab the comment
            comment = form.save(commit=False)
            #connect that comment to the post object
            comment.post = post
            #save the comment
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    #post_pk we need to store this primary key in order to send it in response after we delete comment
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
