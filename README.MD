使用Django+Docker搭建的项目模板，可快速用于开发和生产部署中

## 使用方法

1. 更改项目目录名称，更改myproject为项目名称
2. 全局查找替换myproject为项目名称
3. 修改dockerizing->nginx->sites-enabled->default.conf中域名等配置
4. 修改docker-compose.yml中端口号配置
5. 执行：docker-compose build 构建项目容器
6. 执行：docker-compose up -d 启动容器
7. 使用IP:PORT或域名访问服务
8. 项目配置使用django-environ插件，可在myproject->envs目录下修改对应环境配置