"""
FastAPI 示例应用 —— 支持环境变量配置
"""
from fastapi import FastAPI, Response, status
from socket import gethostname
import os
import time

app = FastAPI(title="JoyK8 学习应用")

# === 从环境变量读取配置（ConfigMap 注入）===
APP_VERSION = os.environ.get("APP_VERSION", "2.0.0")
APP_ENV = os.environ.get("APP_ENV", "development")
GREETING = os.environ.get("GREETING", "Hello from JoyK8 v2! 🚀🚀")

START_TIME = time.time()


@app.get("/")
def root():
    """根路径"""
    return {
        "message": GREETING,           # 来自配置
        "status": "running",
        "version": APP_VERSION,        # 来自配置
        "hostname": gethostname(),
    }


@app.get("/health")
def health():
    """健康检查接口（k8s 探针用）"""
    return {"status": "healthy"}


@app.get("/info")
def info():
    """应用信息接口"""
    return {
        "app": "JoyK8",
        "version": APP_VERSION,
        "env": APP_ENV,
        "hostname": gethostname(),
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "config": {
            "greeting": GREETING,
        }
    }


@app.get("/version")
def version():
    """版本接口"""
    return {"version": APP_VERSION, "env": APP_ENV}


# === 新增：用于 readiness 探针（启动检查）===
@app.get("/ready")
def ready(response: Response):
    """
    就绪探针：应用启动后过 5 秒才返回 200
    用于测试"探针启动延迟"功能
    """
    uptime = time.time() - START_TIME
    if uptime < 5:  # 启动 5 秒内返回 503
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "starting", "uptime": round(uptime, 2)}
    return {"status": "ready", "uptime": round(uptime, 2)}
