# Dify 部署指南

## 概述

本项目使用 Docker Compose 部署 Dify 1.17.1，并接入本地 Ollama 千问模型。
### 验证启动

```powershell
# 查看容器状态（应有 15 个容器）
docker ps

# 测试 Web 访问
curl http://localhost
```

浏览器打开 http://localhost

首次进入会要求注册管理员账号。

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
