from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import *
from .models import *
from datetime import datetime
from zoneinfo import ZoneInfo
from django.core.paginator import Paginator#ページネーション機能
from django.contrib import messages#フラッシュメッセージ
from django.db.models import Count#1対多の多の要素をカウントするため
from django.http import JsonResponse#非同期処理のために使用
from django.template.loader import render_to_string#jsonでhtmlファイルを返すときに使用


class IndexView(View):
    def get(self, request):
        datetime_now = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        return render(
            request, "diary/index.html", {"datetime_now": datetime_now})


class PageCreateView(View):
    def get(self, request):
        form = PageForm()
        return render(request, "diary/page_form.html", {"form": form})

    def post(self, request):
        form = PageForm(request.POST, request.FILES)#request.FILESは画像のために追加
        if form.is_valid():
            form.save()
            return redirect("diary:index")
        return render(request, "diary/page_form.html", {"form": form})
    
class PageListView(View):
    def get(self, request):
        #page_list = Page.objects.all()
        page_list = Page.objects.order_by("-page_date")#降順にしたいときは-をつける
        return render(request, "diary/page_list.html", {"page_list": page_list})

class PageDetailView(View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "diary/page_detail.html", {"page": page})
        
class PageUpdateView(View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(instance=page)
        return render (request, "diary/page_update.html", {"form": form})

    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect("diary:page_detail", id=id)
        return render(request, "diary/page_form.html", {"form": form})

class PageDeleteView(View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "diary/page_confirm_delete.html", {"page": page})

    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        page.delete()
        return redirect("diary:page_list")
    
def login(request):
    request.session["user_name"] = None
    form = LoginForm()
    con = {"form": form}
    return render(request, "user/login.html", con)

def logout(request):
    request.session["user_name"] = None
    #import pdb; pdb.set_trace()
    return redirect("diary:user_login")

def home(request):
    form = LoginForm(request.POST)
    #import pdb; pdb.set_trace()
    if request.session["user_name"] != None:#ログインユーザーあり
        user = MyUser.objects.get(name=request.session["user_name"])

        #いいね済みのページIDをまとめる
        good_ids = Good.objects.filter(my_user_id=user.id).values_list('page_id', flat=True)#flat=Trueでリストとなる
        #総いいね数をgood_count属性に追加
        pages = Page.objects.annotate(good_count=Count('good')).all()

        #pages = Page.objects.all()
        paginator = Paginator(pages, 2)  # 1ページに5件ずつ表示
        page_number = request.GET.get('page')  # ?page=2 などから取得
        pages = paginator.get_page(page_number)  # 例外処理も含まれる安全な方法

        con = {"name":user.name, "pages": pages, "good_ids":good_ids}
        return render(request, "user/home.html", con)
        
    else:#ログインユーザーなし
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            try:
                user = MyUser.objects.get(name=name,password=password)
            except:
                messages.error(request, '名前またはパスワードが違うよ')
                return redirect("diary:user_login")
            #session定義
            request.session["user_name"] = user.name
            
            #userがいいね済みのページIDをまとめる
            good_ids = Good.objects.filter(my_user_id=user.id).values_list('page_id', flat=True)#flat=Trueでリストとなる

            #総いいね数をgood_count属性に追加
            pages = Page.objects.annotate(good_count=Count('good')).all()

            #pages = Page.objects.all()
            paginator = Paginator(pages, 2)  # 1ページに5件ずつ表示
            page_number = request.GET.get('page')  # ?page=2 などから取得
            pages = paginator.get_page(page_number)  # 例外処理も含まれる安全な方法

            con = {"name":name, "pages": pages, "good_ids":good_ids}
            #import pdb; pdb.set_trace()
            return render(request, "user/home.html", con)
        else:
            return redirect("diary:user_login")

def good(request, id):
    my_user = MyUser.objects.get(name=request.session["user_name"])
    page = Page.objects.get(id=id)
    #import pdb; pdb.set_trace()
    Good.objects.create(my_user_id=my_user,page_id=page)#外部キーのカラムにオブジェクトを入れることで作成できる、こうしないとエラー

    page = Page.objects.annotate(good_count=Count('good')).get(id=id)
    #import pdb; pdb.set_trace()

    con = {"page":page,"good_or_delete":True}
    html = render_to_string("user/good.html",con,request)
    return JsonResponse({"status": "success","html":html})

def good_delete(request, id):
    my_user = MyUser.objects.get(name=request.session["user_name"])
    page = Page.objects.get(id=id)
    Good.objects.get(my_user_id=my_user.id,page_id=page.id).delete()

    page = Page.objects.annotate(good_count=Count('good')).get(id=id)
    con = {"page":page,"good_or_delete":False}
    html = render_to_string("user/good.html",con,request)
    return JsonResponse({"status": "success","html":html})

def test(request):
    return render(request, "user/test.html")

def test2(request):
    return render(request, "user/test2.html")






index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
page_update = PageUpdateView.as_view()
page_delete = PageDeleteView.as_view()
