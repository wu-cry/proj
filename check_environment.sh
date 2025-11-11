#!/bin/bash
echo "=== WSL环境完整性检查 ==="

echo -e "\n1. 系统信息:"
uname -a

echo -e "\n2. Python检查:"
python3 --version
pip3 --version

echo -e "\n3. 虚拟环境检查:"
if [ -d "myenv" ]; then
    echo "虚拟环境目录存在"
    source myenv/bin/activate
    python -c "import sys; print(f'当前Python路径: {sys.prefix}')"
    deactivate
else
    echo "虚拟环境目录不存在"
fi

echo -e "\n4. Docker检查:"
docker --version
docker ps > /dev/null 2>&1 && echo "Docker服务: 运行中" || echo "Docker服务: 未运行"

echo -e "\n=== 检查完成 ==="
