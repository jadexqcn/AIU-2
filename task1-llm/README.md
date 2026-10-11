# 任务一：大模型部署与智能体搭建

本地部署千问3大模型，搭建 Dify 智能体平台，通过 API 接入应用。

## 完成情况

| 子任务 | 状态 | 说明 |
|--------|------|------|
| 本地大模型部署 | ✅ | Ollama + 千问3 (8b/14b) |
| 智能体平台搭建 | ✅ | Dify 1.17.1 (Docker) |
| API 接入应用 | ✅ | Dify Web + CLI 对话工具 |


## 部署架构

```
用户层 (Dify Web / CLI / 其他应用)
    ↓
Dify API (localhost:80)
    ↓
Ollama API (127.0.0.1:11434)
    ↓
模型 (qwen3:8b / qwen3:14b)
```

## 快速开始

### 1. 启动 Ollama

```powershell
ollama serve
curl http://127.0.0.1:11434/api/tags  # 验证
```

### 2. 启动 Dify

```powershell
cd <Dify项目目录>/docker
docker compose up -d
```

访问 http://localhost

### 3. 接入模型

Dify 设置 → 模型供应商 → Ollama：
- 模型名称：`qwen3:8b`
- Base URL：`http://host.docker.internal:11434`
- 模型类型：对话模型

## 详细文档

- [Ollama 安装配置](./ollama-setup.md)
- [Dify 部署指南](./dify-setup.md)
- [踩坑记录](./troubleshooting.md)
