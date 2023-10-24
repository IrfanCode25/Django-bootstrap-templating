from django.shortcuts import render

# Create your views here.
def blog_list(request):
   print(request.resolver_match.url_name)
   return render(request, 'blog_index.html')