# Ollama 安装配置

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
