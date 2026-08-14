"""
FastAPI 示例应用 —— 一个简单的问候 API
这是贯穿整个 k8s 学习的示例程序
"""
from fastapi import FastAPI
import socket
import os
import time

# 创建 FastAPI 应用实例
app = FastAPI(title="JoyK8 学习应用", version="1.0.0")

# 记录启动时间（后面用来算运行时长）
START_TIME = time.time()


@app.get("/")
def root():
    """根路径 —— 健康检查用"""
    return {
        "message": "Hello from JoyK8! 🚀",
        "status": "running",
        "hostname": socket.gethostname(),  # 显示容器的主机名（k8s 里就是 Pod 名）
    }


@app.get("/health")
def health():
    """健康检查接口 —— k8s 会用这个判断应用是否存活"""
    return {"status": "healthy"}


@app.get("/info")
def info():
    """应用信息接口"""
    return {
        "app": "JoyK8",
        "version": "1.0.0",
        "hostname": socket.gethostname(),
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "env": os.environ.get("APP_ENV", "development"),  # 读取环境变量（后面 ConfigMap 会用）
    }
