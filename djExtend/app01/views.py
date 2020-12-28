from django.shortcuts import render,HttpResponse,redirect
import json


# Create your views here.

def index(request):
    books=[]
    with open("book.txt","r",encoding='utf-8') as f:
        for line in f.readlines():
        #data = f.readline()
            books.append(json.loads(line))
    #print(books)
    return render(request,'index.html',locals())

    # return HttpResponse('欢迎进入图书管理页面')


    #放到缓存里
    # class Book(object):
    #     def __init__(self,title,price,publish):
    #         self.title=title
    #         self.price=price
    #         self.publish=publish
    #
    # book01 = Book("西游记",122,"北京出版社")
    # book02 = Book("水浒传",233,"南京出版社")
    # book03 = Book("三国演义",552,"工业出版社")
    # book04 = Book("金瓶梅",233,"橘子出版社")
    # book05 = Book("红楼梦",567,"河北出版社")
    # book06 = Book("大话西游",169,"老男孩出版社")
    #
    # books =[book01,book02,book03,book04,book05,book06]


    # return render(request,'index.html',locals())

def add(request):

    if request.method=="GET":

        return render(request,'add.html',locals())
    #return HttpResponse('欢迎进入添加页面')
    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        publish = request.POST.get("publish")
        nid = request.POST.get("nid")


        book = {"title":title,"price":price,"publish":publish,"nid":nid}

        with open("book.txt","a") as f:
            f.write(json.dumps(book)+"\n")

        return redirect("/")

def delete(request,del_id):
    print("del_id",del_id)
    return HttpResponse("删除成功")