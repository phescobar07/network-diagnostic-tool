Write-Host "`n🚀 Iniciando instalador automático de dependências..."

# Verifica se o Python está instalado
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "❌ Python não está instalado. Baixe em: https://www.python.org/downloads/"
    Pause
    Exit
}

Write-Host "✅ Python encontrado: $($python.Source)"

# Verifica se o pip está funcionando
try {
    python -m pip --version | Out-Null
    Write-Host "✅ pip está funcionando!"
}
catch {
    Write-Host "⚠️ pip não encontrado. Tentando instalar/atualizar pip..."
    python -m ensurepip --default-pip
}

# Instala os pacotes necessários
Write-Host "📦 Instalando dependências: speedtest-cli, requests"
python -m pip install --upgrade pip
python -m pip install speedtest-cli requests

# Roda o script principal
Write-Host "`nExecutando o script de diagnóstico de rede...`n"
python .\diagnostico_rede.py
