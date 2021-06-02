from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .models import gallery, gallery_type, article, news, teacher
from .forms import GalleryForm, GalleryTypeForm, ArticleForm, NewsForm,  TeacherForm

def index(request):
    articles = article.objects.all().order_by('-id')[:3]
    items = news.objects.all().order_by('-id')[:5]
    return render(request, 'home/dash.html', {'items': items, 'articles' : articles  })


def user_all(request):
        course_id = request.GET.get("course_id")
        upcoming_li=[]
        batch_qs=list(Batch.objects.filter(course_name_id=course_id).values())
        user_qs=User.objects.get(id=request.user.id)
        user_batch_qs=list(user_qs.batch.all().values("id"))
        now = datetime.now()
        now1=now+timedelta(days = 7)
        lst = []
        pending=[]
        completed=[]
        dic={}
        for i in user_batch_qs:
            for j in batch_qs:
                if i["id"] == j["id"]:
                    timing = ast.literal_eval(j["timing"])
                    if timing:
                        data = upcoming_classes(timing)
                        dic["course_id"]=j["course_name_id"]
                        course_qs=Course.objects.get(id=j["course_name_id"])
                        dic["course_name"]=course_qs.title
                        dic["upcoming_classes"]=data
                        data1 = completed_classes(timing)
                        dic["completed_classes"]=data1
                        dic["batch_id"]=i["id"]
                        dic["batch_name"]=j["batch_name"]
                        dic["online_link"]=j["online_link"]
        return render (request, 'teacher.html' , {'all_teachers': all_teachers } )




def user_all(request):
        course_id = 2
        upcoming_li=[]
        batch_qs=list(Batch.objects.filter(course_name_id=course_id).values())
        user_qs=User.objects.get(id=85)
        user_batch_qs=list(user_qs.batch.all().values("id"))
        now = datetime.now()
        now1=now+timedelta(days = 7)
        lst = []
        pending=[]
        completed=[]
        dic={}
        links = []
        for i in user_batch_qs:
            for j in batch_qs:
                if i["id"] == j["id"]:
                    timing = ast.literal_eval(j["timing"])
                    if timing:
                        data = upcoming_classes(timing)
                        dic["course_id"]=j["course_name_id"]
                        course_qs=Course.objects.get(id=j["course_name_id"])
                        dic["course_name"]=course_qs.title
                        dic["upcoming_classes"]=data
                        data1 = completed_classes(timing)
                        dic["completed_classes"]=data1
                        dic["batch_id"]=i["id"]
                        dic["batch_name"]=j["batch_name"]
                        links.append(j["online_link"])
        return render (request, 'student.html' , {'data':dic , 'link':links } )




def admin_page(request):
    return render(request, 'home/admin.html')

def about1(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def facility(request):
    return render(request, 'home/facilities.html')


def gallery1(request):
    items = gallery_type.objects.all().order_by('-pk')
    return render(request, 'home/gallery.html', {'items': items })



def gallery2(request, pk):
    item = gallery_type.objects.get(pk=pk)
    items = gallery.objects.filter(category=item).order_by('-id')
    return render(request, 'home/gallery_section.html', {'items': items , "main_item": item })


def gallery_type_add(request):
    if request.method == "POST":
        form = GalleryTypeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(True)
            return redirect('home:index')
        else:
            return HttpResponse("Nhi hua")
    else:
        return render(request, 'home/gallery_type_form.html')


def gallery_add(request):
    form = GalleryForm()
    if request.method == "POST":
        form = GalleryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(True)
            return redirect('home:index')
        else:
            return HttpResponse("Nhi hua")
    else:
        return render(request, 'home/gallery_form.html', {"form": form})


def gallery_list(request):
    sections = gallery_type.objects.all().order_by('-pk')
    items = gallery.objects.all().order_by('-pk')
    return render(request, 'home/images_list.html', {"items": items, "sections": sections })


def del_img(request,pk):
    img = gallery.objects.get(pk=pk)
    img.delete()
    items = gallery.objects.all().order_by('-pk')
    return render(request, 'home/images_list.html', {"items": items } )


def del_gal(request,pk):
    sect = gallery_type.objects.get(pk=pk)
    imgs = gallery.objects.filter(category=sect)
    for i in imgs:
        i.delete()
    sect.delete()
    items = gallery.objects.all().order_by('-pk')
    sections = gallery_type.objects.all().order_by('-pk')
    return render(request, 'home/images_list.html', {"items": items,  "sections": sections } )



def article_form(request):
    if request.method == "POST":
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(True)
            return redirect('home:article-list')
        else:
            return HttpResponse("Nhi hua")
    return render(request, 'home/article_form.html')


def articles(request, pk):
    art = article.objects.get(pk=pk)
    return render(request, 'home/article.html', {'art': art} )


def article_page(request):
    items = article.objects.all()
    return render(request, 'home/articles.html', {'items': items} )


def article_list(request):
    items = article.objects.all()
    return render(request, 'home/article_list.html', {'items': items} )


def article_delete(request,pk):
    item = article.objects.get(pk=pk)
    item.delete()
    items = article.objects.all()
    return render(request, 'home/article_list.html', {'items': items} )


def news_page(request):
    items = news.objects.all().order_by('-id')
    return render(request, 'home/news.html', {'items': items  })


def news_form(request):
    if request.method == "POST":
        form = NewsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(True)
            return redirect('home:news-list')
        else:
            return HttpResponse("Nhi hua")
    return render(request, 'home/news_form.html')


def news_list(request):
    items = news.objects.all()
    return render(request, 'home/news_list.html', {'items': items} )


def news_delete(request,pk):
    item = news.objects.get(pk=pk)
    item.delete()
    items = news.objects.all()
    return render(request, 'home/news_list.html', {'items': items} )


def teacher_page(request):
    items = teacher.objects.all()
    return render(request, 'home/teacher.html', {'items': items} )


def teacher_form(request):
    if request.method == "POST":
        form = TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(True)
            return redirect('home:tech-list')
        else:
            return HttpResponse("Nhi hua")
    return render(request, 'home/tech_form.html')


def teacher_list(request):
    items = teacher.objects.all()
    return render(request, 'home/tech_list.html', {'items': items} )


def teacher_delete(request,pk):
    item = teacher.objects.get(pk=pk)
    item.delete()
    items = teacher.objects.all()
    return render(request, 'home/tech_list.html', {'items': items} )
