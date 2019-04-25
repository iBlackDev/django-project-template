使用Django+Docker搭建的项目模板，可快速用于搭建Django项目的开发环境，也可以用于生产部署，保持开发和生产环境一致性

## 使用方法

1. 更改项目目录名称，更改myproject为项目名称
2. 全局查找替换myproject为项目名称
3. 修改dockerizing->nginx->sites-enabled->default.conf中域名等配置
4. 修改docker-compose.yml中端口号配置
5. 执行：docker-compose build 构建项目容器
6. 执行：docker-compose up -d 启动容器
7. 执行：docker-compose logs -f 可查看日志，日志相关配置可在setting修改
 

## 项目说明
1. 项目配置使用django-environ插件，可在myproject->envs目录下修改对应环境配置
2. requirements.txt为依赖三方库描述文件，需要添加其他三方库，可直接在文件中添加三方库名称并指定版本号