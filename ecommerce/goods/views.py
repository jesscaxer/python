from django.shortcuts import render
from django.views import View
from goods.models import GoodsSKU, Category, ActivityZone


class IndexClassView(View):
    def get(self, request):
        return render(request, 'goods/index.html')

class DetailClassView(View):
    def get(self, request, id=1):
        goods_sku = GoodsSKU.objects.get(id=id)
        context = {"goods_sku": goods_sku}
        activity_zone = ActivityZone.objects.filter(is_delete=False)
        return render(request, 'goods/detail.html', context=context)


class CategoryClassView(View):
    def get(self, request, cate_id, order):

        #做列表的点击
        categories = Category.objects.filter(is_delete=False)
        if cate_id == '':
            category = categories.first()
            cate_id = category.pk
        else:
            cate_id = int(cate_id)
            category = Category.objects.get(pk=cate_id)
        goods_sku = category.goodssku_set.all()
        #做排序的点击
        order_rule = ['pk', 'price', '-price', 'sale_num']
        if order == '':
            goods_sku = goods_sku.order_by(order_rule[0])
        else:
            order = int(order)
            goods_sku = goods_sku.order_by(order_rule[order])


        context = {
            'cate_id': cate_id,
            'goods_sku': goods_sku,
            'categories': categories,
            'order': order}
        return render(request, 'goods/category.html', context=context)

