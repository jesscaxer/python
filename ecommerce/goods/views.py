from django.shortcuts import render
from django.views import View
from goods.models import GoodsSKU, Category


class IndexClassView(View):
    def get(self, request):
        return render(request, 'goods/index.html')

class DetailClassView(View):
    def get(self, request, id):
        goods_sku = GoodsSKU.objects.get(pk=id)
        context = {"goods_sku": goods_sku}
        return render(request, 'goods/detail.html', context=context)


class CategoryClassView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'goods/category.html', context={'categories':categories})

