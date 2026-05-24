import os
import subprocess
import sys
from typing import Tuple


def run_command(command: str, cwd: str = None) -> Tuple[bool, str]:
    """执行命令并返回执行结果"""
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            return True, stdout.strip()
        else:
            return False, stderr.strip()
    except Exception as e:
        return False, str(e)


def get_project_root() -> str:
    """自动获取项目根目录"""
    # 尝试通过当前文件路径推断项目根目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 向上查找直到找到项目根目录（包含requirements.txt）
    while current_dir != os.path.dirname(current_dir):  # 直到根目录
        if os.path.exists(os.path.join(current_dir, "requirements.txt")):
            return current_dir
        current_dir = os.path.dirname(current_dir)

    # 如果没找到，使用当前目录
    return os.path.dirname(os.path.abspath(__file__))


def main():
    # 获取项目根目录
    project_root = get_project_root()
    print(f"项目根目录: {project_root}")

    # # 1. 安装依赖
    # print("\n" + "=" * 50)
    # print("步骤1: 正在安装依赖...")
    # success, output = run_command("pip3 install -r requirements.txt", cwd=project_root)
    #
    # if not success:
    #     print(f"❌ 依赖安装失败: {output}")
    #     sys.exit(1)
    #
    # print(f"✅ 依赖安装成功!\n{output}")

    # 2. 运行测试脚本
    print("\n" + "=" * 50)
    print("步骤2: 正在运行测试脚本...")
    test_dir = os.path.join(project_root, "scripts", "shopping")
    print(test_dir)
    if not os.path.exists(test_dir):
        print(f"❌ 测试目录不存在: {test_dir}")
        sys.exit(1)

    success, output = run_command("python3 -m pytest -v test_login.py", cwd=test_dir)

    if not success:
        print(f"❌ 测试运行失败: {output}")
        sys.exit(1)

    print(f"✅ 测试运行成功!\n{output}")

    # 3. 生成Allure报告
    print("\n" + "=" * 50)
    print("步骤3: 正在生成测试报告...")
    success, output = run_command(
        "allure generate ../../report -o ../../report/html --clean",
        cwd=test_dir
    )

    if not success:
        print(f"❌ 报告生成失败: {output}")
        sys.exit(1)

    print(f"✅ 报告生成成功!\n{output}")

    # 4. 提示用户查看报告
    print("\n" + "=" * 50)
    report_dir = os.path.join(project_root, "report", "html")
    report_path = os.path.join(report_dir, "index.html")

    if not os.path.exists(report_path):
        print(f"❌ 报告文件不存在: {report_path}")
        sys.exit(1)

    print("自动化测试流程完成!")
    print(f"请前往以下路径查看报告:\n{report_path}")



if __name__ == "__main__":
    main()
