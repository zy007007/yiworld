# yiworld
小毅开始的毅世界
2018年11月25日，终于完成了初始毅世界。幸好今年毕设后期尝试的在服务器搞了一下，有了小小的经验，才在昨天得以用不到一天的时间完成。 这里就记录一下整体的流程，以及网上获取的帮助。今后如果还有类似的需求，应该来这里寻求指点就可。 －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－ 服务器： 阿里云ESC服务器，学生认证，配置最低但自己一个人正好可以用 唯一需要注意的是安全组开放入方向的端口问题

相关技术： python flask + nginx 数据库　postgresl mongo

下面的文章收集，就是从本地代码编写运行到搞到服务器上面运行的这一过程，有教程也有坑解决。

在CentOS上配置Nginx+Gunicorn+Python+Flask环境的教程　https://www.jb51.net/article/86129.htm

CentOS7下PostgreSQL安装过程　 https://www.cnblogs.com/hannyblogs/p/6535664.html

命令行方式登录PostgreSQL、创建用户和数据库并赋权　　https://blog.csdn.net/zhangzeyuaaa/article/details/77941039

centos7 yum安装MongoDB　　　https://blog.csdn.net/xgs736214763/article/details/78505856

postgresal使用错误解决 （记录篇）　　　　　https://blog.csdn.net/wangyezi19930928/article/details/20358369

上传本地代码及更新代码到GitHub教程 https://www.cnblogs.com/zlxbky/p/7727895.html

supervisor 管理进程简明教程 https://blog.csdn.net/woshixiaosimao/article/details/54315258

在centos下启动nginx出现Failed to start nginx.service:unit not found https://blog.csdn.net/qq_36663951/article/details/79815872

在编写代码，以及项目初始化的时候 记得新项目，初始化数据库 db.create_all db.create_all() db init

项目中常用的配置，记得保留，例如　
