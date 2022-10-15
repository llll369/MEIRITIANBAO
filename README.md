# MEIRITIANBAO

## 实现西工大疫情填报自动化

## 原理

使用github action 实现自动化填报。  
时间设为每日7.50，因为action机制会有十分钟到几小时延迟。介意可以使用第三方调用action webhook优化实现定时执行

执行成功后会推送提示消息到手机。  
使用PushDeer实现(IOS端)，

自动填报有两种方案，分别为模拟Web端登录和模拟APP端登录  
APP端登录仅为本地手动，需要在setting.py添加device_id字段，  
device_id可以通过抓取APP登录获得，不理解可以无视该模块

22年10月增加了mfa验证，需要保证登录ip为可信ip，即不可信需要增加手机验证步骤。已解决

## 安装依赖

pip install -r requirement.txt

## 使用

1. Star仓库(可选)，Follow作者(可选),fork该仓库

2. 在仓库的Setting->Secrets->Actions添加环境变量，依次为NAME,PASSWORD,PUSHDEER  
该字段名字、顺序不可有误
NAME     为学号
PASSWORD 为账号密码
PUSHDEER 为PushDeer软件的key

3. 如果需要本地调试，clone代码后在setting.py文件内输入字段对应的值
