# Ollama 安装配置

## 安装步骤

### 1. 下载 Ollama

从官方下载 Windows 版本：

```powershell
# 方法1：直接下载（推荐）
# 访问 https://ollama.com/download/windows
# 下载 OllamaSetup.exe

# 方法2：使用 winget
winget install Ollama.Ollama
```


### 2. 启动服务

```powershell
# 前台运行（调试用）
ollama serve

# 后台运行（推荐）
Start-Process -FilePath "ollama" -ArgumentList "serve" -WindowStyle Hidden
```

### 3. 下载模型

```powershell
# 下载千问3 8B（推荐，速度快）
ollama pull qwen3:8b

# 下载千问3 14B（质量更好，但慢）
ollama pull qwen3:14b
```

下载位置：`%USERPROFILE%\.ollama\models`（或你设置的 `OLLAMA_MODELS` 路径）

### 4. 验证安装

```powershell
# 查看已下载模型
ollama list

# 测试对话
ollama run qwen3:8b
```

## 常用命令

```powershell
# 模型管理
ollama list              # 列出所有模型
ollama pull <model>      # 下载模型
ollama rm <model>        # 删除模型
ollama show <model>      # 查看模型信息

# 运行模型
ollama run <model>       # 交互式对话
ollama run <model> "问题" # 单次问答

# 服务管理
ollama serve             # 启动服务（前台）
```

## API 使用

Ollama 提供 REST API，端口 11434。

### 生成文本

```powershell
$body = @{
    model = "qwen3:8b"
    prompt = "你好"
    stream = $false
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:11434/api/generate" `
    -Method Post -Body $body -ContentType "application/json"
```

### 对话接口

```powershell
$body = @{
    model = "qwen3:8b"
    messages = @(
        @{ role = "user"; content = "你好" }
    )
    stream = $false
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:11434/api/chat" `
    -Method Post -Body $body -ContentType "application/json"
```



## 下一步

安装完成后，继续部署 [Dify 智能体平台](./dify-setup.md)。
