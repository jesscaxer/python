from django.shortcuts import redirect

from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest

from aliyunsdkcore.client import AcsClient

from aliyunsdkcore.profile import region_provider




# 将验证登录的方法写成装饰器


from ecommerce.settings import ACCESS_KEY_ID, ACCESS_KEY_SECRET


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

REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)
def send_sms(business_id, phone_numbers, sign_name, template_code, template_param=None):
    smsRequest = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    smsRequest.set_TemplateCode(template_code)

    # 短信模板变量参数
    if template_param is not None:
        smsRequest.set_TemplateParam(template_param)

    # 设置业务请求流水号，必填。
    smsRequest.set_OutId(business_id)

    # 短信签名
    smsRequest.set_SignName(sign_name)

    # 数据提交方式
    # smsRequest.set_method(MT.POST)

    # 数据提交格式
    # smsRequest.set_accept_format(FT.JSON)

    # 短信发送的号码列表，必填。
    smsRequest.set_PhoneNumbers(phone_numbers)

    # 调用短信发送接口，返回json
    smsResponse = acs_client.do_action_with_exception(smsRequest)

    # TODO 业务处理

    return smsResponse