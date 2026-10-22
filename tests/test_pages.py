"""第15次课：Flask 测试客户端——不开服务器直接测路由（三个测试全绿）"""
from app import app


def test_index(client):
    """首页应 200 并包含 CampusFix 标题"""
    resp = client.get("/")
    assert resp.status_code == 200
    assert "CampusFix".encode("utf-8") in resp.data


def test_index_title(client):
    """考试：首页标题应显示学号版本 CampusFix-20252152"""
    resp = client.get("/")
    assert resp.status_code == 200
    assert "CampusFix-20252152".encode("utf-8") in resp.data


def test_detail(client):
    """创建工单后，详情页应 200 并显示该工单"""
    client.post(
        "/tickets/new",
        data={"title": "演示工单", "room": "A区101", "description": "测试详情页"},
        follow_redirects=True,
    )
    resp = client.get("/tickets/1")
    assert resp.status_code == 200
    assert "演示工单".encode("utf-8") in resp.data


def test_create(client):
    """POST 创建工单并跟随跳转后，列表应出现新工单"""
    resp = client.post(
        "/tickets/new",
        data={"title": "测试工单", "room": "A区101", "description": "灯坏了"},
        follow_redirects=True,
    )
    assert resp.status_code == 200
    assert "测试工单".encode("utf-8") in resp.data
