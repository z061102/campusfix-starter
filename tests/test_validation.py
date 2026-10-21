"""第14次课：为"标题长度校验"缺陷写的测试（先红后绿）
第15次课：新增请求级测试（POST 表单 + 400 + 错误提示断言）"""
from app import validate_ticket


def test_title_too_long():
    error = validate_ticket("A" * 21, "A101")
    assert error == "标题不能超过20个字符"


def test_post_title_too_long(client):
    """通过真实 POST 请求验证路由层的 400 拦截与错误提示"""
    resp = client.post(
        "/tickets/new",
        data={"title": "A" * 21, "room": "A区101", "description": "测试"},
    )
    assert resp.status_code == 400
    assert "标题不能超过20个字符".encode("utf-8") in resp.data

