#!/usr/bin/env python3
import sys
import os
import subprocess
import requests

def comprehensive_test():
    print("🎯 WSL开发环境综合测试报告")
    print("=" * 60)
    
    test_results = []
    
    # 测试1: 虚拟环境
    print("1. 🔍 虚拟环境检查...")
    in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    if in_venv:
        print("   ✅ 虚拟环境已激活")
        test_results.append(("虚拟环境", "✅"))
    else:
        print("   ❌ 虚拟环境未激活")
        test_results.append(("虚拟环境", "❌"))
    
    # 测试2: Python包
    print("2. 🔍 Python包检查...")
    try:
        import requests
        print("   ✅ requests库可用")
        test_results.append(("Python包", "✅"))
    except ImportError:
        print("   ❌ requests库不可用")
        test_results.append(("Python包", "❌"))
    
    # 测试3: Docker安装
    print("3. 🔍 Docker安装检查...")
    try:
        result = subprocess.run(['docker', '--version'], capture_output=True, text=True, check=True)
        print(f"   ✅ {result.stdout.strip()}")
        test_results.append(("Docker安装", "✅"))
    except:
        print("   ❌ Docker未安装")
        test_results.append(("Docker安装", "❌"))
    
    # 测试4: Docker权限
    print("4. 🔍 Docker权限检查...")
    try:
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True, check=True)
        print("   ✅ Docker权限正常")
        test_results.append(("Docker权限", "✅"))
    except:
        print("   ❌ Docker权限异常")
        test_results.append(("Docker权限", "❌"))
    
    # 测试5: 网络连接
    print("5. 🔍 网络连接检查...")
    try:
        response = requests.get('https://httpbin.org/get', timeout=10)
        if response.status_code == 200:
            print("   ✅ 网络连接正常")
            test_results.append(("网络连接", "✅"))
        else:
            print("   ❌ 网络连接异常")
            test_results.append(("网络连接", "❌"))
    except:
        print("   ❌ 网络连接失败")
        test_results.append(("网络连接", "❌"))
    
    print("=" * 60)
    print("📊 测试结果汇总:")
    for test, result in test_results:
        print(f"   {test}: {result}")
    
    all_passed = all(result == "✅" for _, result in test_results)
    
    if all_passed:
        print("🎉 所有测试通过！WSL开发环境完美配置！")
        print("\n✨ 环境准备就绪，您可以：")
        print("   • 使用 'source myenv/bin/activate' 激活虚拟环境")
        print("   • 使用 'pip install' 安装Python包")
        print("   • 使用 'docker' 命令管理容器")
        print("   • 开始您的Python和Docker开发项目")
    else:
        print("⚠️  部分测试未通过，请检查相关配置")
    
    return all_passed

if __name__ == "__main__":
    comprehensive_test()
