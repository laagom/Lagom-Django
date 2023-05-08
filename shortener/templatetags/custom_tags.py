from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name="email_ma")
def email_masker(value, arg):
    email_split = value.split("@")

    return f"{email_split[0]}@******.***" if arg % 2 == 0 else value 


@register.filter(name="price_comma")
def price_comma(value):
    return format(value, ',d')


# takes_context를 True로 설정하지 않으면 메소드에서 context를 사용할 수 없음
@register.simple_tag(name="test_tags", takes_context=True)
def test_tags(context):
    tag_html = "<span class='badge badge-primary'>테스트 태그</span>"

    # 클라이언트로 전달 시 스트링만 보내게 되면 html 태그로 인식하지 못함
    return mark_safe(tag_html)