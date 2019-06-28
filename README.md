# 网易考拉 Python SDK

目前只支持1.0版本的接口

## 安装

```python
pip install kaola
```


## 使用方法

```python
from kaola.api.kaola import KaoLa

kl = KaoLa("edb6c3b9ac4847e7584c38e2b630b14f", "8200ee92ec22fcae76e2f00bc5c79247188e0593",access_token="bff74ff8-bbec-4699-bc4c-529801aefcb4", sandbox=True)
# 搜索订单
kl.order.search_order(
    1, 1, "2019-01-01 0:00:00", "2019-01-30 23:59:59").json()
```

sandbox 是否是沙箱环境

## changelog

* [0.0.3] 修复返回结果格式问题
* [0.0.4] 更新access token获取机制