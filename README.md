# EFC
利用```go-cqhttp```的事件过滤器增强 ```HoshinoBot```功能 

## 简介
本项目的目标是增强HoshinoBot（直接调的话也能给其它nonebot项目用）的拉黑方法，实现全局化、持久化

[![State-of-the-art Shitcode](https://img.shields.io/static/v1?label=State-of-the-art&message=Shitcode&color=7B5804)](https://github.com/trekhleb/state-of-the-art-shitcode)

## 目标
* 及时解除用户拉黑
* 简洁优雅的代码
* SUPERUSER通知功能
* 简洁配置读取

## 目前
* 每隔三分钟检查拉黑列表
* 大量冗余重复代码
* 只有logger通知
* 复杂的配置读写方法（群和用户居然分成两个配置！）

> 我知道优化一下很简单，但是*摸了*！
