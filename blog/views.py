from django.shortcuts import render
from blog.models import Post



def blog(request):
  return render(request, 'blog.html', {
    'posts': Post.objects.order_by('-created')
    })


def filter_by_tags(request, tag_name):

  return render(request, 'filter_by_tags.html', {
    'posts': Post.objects.filter(tags__name=tag_name),
    })

def register(request):
  if request.method == 'POST':
    form = EmailUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')
  else:
    form = EmailUserCreationForm()

  return render(request, "registration/register.html", {
    'form': form,
    })
