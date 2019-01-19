from django.shortcuts import redirect

# 将验证登录的方法写成装饰器
def check_login(func):
    def verify_login(self, *args, **kwargs):
        # 判断是否登录
        if args[0].session.get('ID') is None:
            # 跳转到登录
            return redirect('user:登录')
        else:
            # 调用原函数
            return func(args[0], *args, **kwargs)
    # 返回新函数
    return verify_login