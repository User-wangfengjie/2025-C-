"""
批量回答问题的入口脚本
"""
import os
import sys
import nest_asyncio

# 应用nest_asyncio以支持异步函数
nest_asyncio.apply()

# 添加当前目录到系统路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.batch_processing.run_batch import main

if __name__ == "__main__":
    sys.exit(main()) 