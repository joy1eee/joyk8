#!/bin/bash
# 服务器端部署脚本 - 由 GitHub Actions 触发

set -e
echo "=== [$(date)] 开始部署 ==="

# 1. 加载新镜像到 k3s
echo "加载镜像..."
k3s ctr -n k8s.io images import /data/joyk8/tmp/joyk8-app.tar

# 2. 清理临时文件
rm /data/joyk8/tmp/joyk8-app.tar

# 3. 触发滚动更新
echo "触发滚动更新..."
kubectl set image deployment/joyk8-app joyk8=joyk8-app:latest

# 4. 等待更新完成
echo "等待更新完成..."
kubectl rollout status deployment/joyk8-app --timeout=120s

echo "=== [$(date)] 部署完成 ==="

# 5. 显示当前状态
echo "=== 当前 Pod 状态 ==="
kubectl get pods -l app=joyk8
