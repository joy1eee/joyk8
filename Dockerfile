# === 第一层：选择基础镜像 ===
# Python 3.11 的精简版（slim 比 full 小很多，生产推荐）
FROM python:3.11-slim

# === 第二层：设置工作目录 ===
# 容器内的代码存放路径（类似 cd /app）
WORKDIR /app

# === 第三层：复制依赖文件 ===
# 先只复制 requirements.txt（利用 Docker 缓存机制，后面解释）
COPY requirements.txt .

# === 第四层：安装依赖 ===
# --no-cache-dir 不保存缓存，让镜像更小
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# === 第五层：复制应用代码 ===
# 把当前目录所有文件复制到容器的 /app 目录
COPY . .

# === 第六层：开放端口 ===
# 声明容器监听 8000 端口（文档性质，实际映射看 docker run）
EXPOSE 8000

# === 第七层：启动命令 ===
# uvicorn 启动 FastAPI，监听所有网卡的 8000 端口
# --host 0.0.0.0 很重要！否则只能容器内访问，外部访问不了
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
