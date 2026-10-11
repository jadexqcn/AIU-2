# Dify 部署指南

## 概述

本项目使用 Docker Compose 部署 Dify 1.17.1，并接入本地 Ollama 千问模型。

## 部署步骤

### 1. 克隆 Dify 仓库

```powershell
git clone --depth 1 https://github.com/langgenius/dify.git <你的项目目录>/Dify/dify
```

> 如果 GitHub 直连不通，可使用镜像加速或配置代理。

### 2. 配置环境变量

```powershell
cd <你的项目目录>/Dify/dify/docker
Copy-Item .env.example .env
```

### 3. 修改 Weaviate 镜像地址

默认 Weaviate 镜像从 `cr.weaviate.io` 拉取，国内可能不通。

编辑 `docker-compose.yaml`，找到 weaviate 的 image 配置：

```yaml
# 修改前
image: cr.weaviate.io/semitechnologies/weaviate:1.39.2

# 修改后
image: semitechnologies/weaviate:1.39.2
```

### 4. 配置 Docker 镜像加速

编辑 `~/.docker/daemon.json`（Windows: `%USERPROFILE%\.docker\daemon.json`）：

```json
{
  "registry-mirrors": [
    "https://docker.m.daocloud.io",
    "https://dockerproxy.com",
    "https://docker.1ms.run"
  ]
}
```

修改后重启 Docker Desktop。

### 5. 启动服务

```powershell
cd <你的项目目录>/Dify/dify/docker
docker compose up -d
```

首次启动会拉取约 2-3GB 的镜像，耐心等待。

### 6. 验证启动

```powershell
# 查看容器状态（应有 15 个容器）
docker ps

# 测试 Web 访问
curl http://localhost
```

浏览器打开 http://localhost，首次进入会要求注册管理员账号。

## 接入本地 Ollama 模型

### 1. 进入设置

登录 Dify → 右上角头像 → **设置** → **模型供应商**

### 2. 添加 Ollama


### 3. 验证接入


## 下一步

Dify 部署完成后，可以：
1. 创建聊天应用，接入千问模型
2. 搭建 RAG 知识库应用
3. 编排 Workflow 工作流
4. 创建 Agent 智能体
