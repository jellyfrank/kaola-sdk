[![Build Status](https://travis-ci.com/block-cat/kaola-sdk.svg?branch=master)](https://travis-ci.com/block-cat/kaola-sdk)
[![Coverage Status](https://coveralls.io/repos/github/block-cat/kaola-sdk/badge.svg?branch=master)](https://coveralls.io/github/block-cat/kaola-sdk?branch=master)
[![PyPI](https://img.shields.io/pypi/v/kaola)](https://pypi.org/project/kaola/)

# 网易考拉 Python SDK

目前只支持1.0版本的接口

## 安装

```python
pip install kaola
```

## 使用方法

### 获取access_token

1. 首先在[考拉开放平台](https://open.kaola.com)注册账号，注册通过后创建应用，给应用起个名字，获取到appkey和appsecret。
2. 使用generate_authorization_code_url方法获取获取access code的url，然后访问这个url，用户授权后会自动跳转参数中的redirect_url
   ```python
   kaola = KaoLa(appkey, appsecret)
   kaola.generate_authorization_code_url(redirect_url)
   ```
3. 在redirect_url的响应事件中先验证state的合法性：
   ```python
   kaola.check_authorization_state(redirect_url, state)
   ```
4. 第3步获取到的code，使用get_access_token方法获取token
   ```python
   kaola.get_access_token(code, shop.redirect_url)
   ```

## 调用API

获取到access_token后，传给初始化函数，或使用set_token方法设置到已有KaoLa实例中。

```python
from kaola.api.kaola import KaoLa

kl = KaoLa("edb6c3b9ac4847e7584c38e2b630b14f", "8200ee92ec22fcae76e2f00bc5c79247188e0593",access_token="bff74ff8-bbec-4699-bc4c-529801aefcb4", sandbox=True)
# 搜索订单
kl.order.search_order(
    1, 1, "2019-01-01 0:00:00", "2019-01-30 23:59:59").json()
```

sandbox 是否是沙箱环境

## changelog

* [0.0.8] 修复订单详细信息查询接口
* [0.0.3] 修复返回结果格式问题
* [0.0.4] 更新access token获取机制
* [0.0.5] 更新说明
* [0.0.6] 接口返回数据直接返回内层数据