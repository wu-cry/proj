#!/usr/bin/env python3
try:
    import requests
    print("✅ requests库安装成功!")
    
    # 测试简单HTTP请求
    response = requests.get('https://httpbin.org/get', timeout=5)
    if response.status_code == 200:
        print("✅ 网络连接测试通过!")
        print("✅ 环境配置完全成功！")
    else:
        print("⚠️  网络连接测试失败")
        
except ImportError:
    print("❌ requests库未安装")
except Exception as e:
    print(f"⚠️  测试过程中出现错误: {e}")
