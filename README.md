# 🚀 JoyK8 — Kubernetes 学习实战项目

> 从零开始，用 FastAPI + Kubernetes 搭建一个完整的生产级应用部署。

## 📖 项目简介

这是我的 Kubernetes 学习实战仓库，记录从零基础到部署完整应用的每一步。

## 🛠️ 技术栈

| 类别 | 技术 |
|------|------|
| 后端框架 | FastAPI (Python) |
| 容器化 | Docker |
| 容器编排 | Kubernetes (k3s) |
| CI/CD | GitHub Actions（规划中） |

## 📁 项目结构

joyk8/
├── app.py              # FastAPI 应用主程序
├── requirements.txt    # Python 依赖
├── Dockerfile          # 容器构建文件
├── .dockerignore       # Docker 构建排除规则
└── .gitignore          # Git 提交排除规则



## 🚀 本地运行

### 1. 构建镜像
```bash
docker build -t joyk8-app:1.0 .
2. 运行容器

docker run -d -p 8000:8000 --name joyk8 joyk8-app:1.0
3. 测试接口

curl http://localhost:8000/        # 根路径
curl http://localhost:8000/health  # 健康检查
curl http://localhost:8000/info    # 应用信息
📚 API 接口
方法路径说明
GET/根路径，返回问候信息
GET/health健康检查（k8s 存活探针用）
GET/info应用详细信息
🎯 学习进度
 环境搭建（Docker + k3s）
 FastAPI 应用开发
 容器化（Dockerfile）
 部署到 Kubernetes（进行中 🔄）
 Ingress 域名访问
 ConfigMap 配置管理
 滚动更新与回滚
 CI/CD 自动化
📝 学习笔记
详细的 k8s 学习笔记见 docs/ 目录（持续更新中）。

⭐ 如果这个项目对你有帮助，欢迎 Star！
