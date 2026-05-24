# UI自动化测试框架

基于8年工作经验搭建的UI自动化测试框架，采用PO模式和数据驱动架构。

## 技术栈

- **Selenium 4.31.0** - Web自动化测试框架
- **Pytest** - 测试框架
- **Allure** - 测试报告框架
- **OpenCV** - 图像处理（滑块验证码识别）
- **NumPy** - 数值计算

## 项目结构

```
autotest-work/
├── common/          # 公共基础层（通用操作方法封装）
├── conf/            # 元素定位层（页面元素定位表达式）
│   ├── sale/        # 销售模块元素
│   └── shopping/    # 购物模块元素
├── data/            # 测试数据层（JSON格式）
│   ├── sale/        # 销售模块数据
│   └── shopping/    # 购物模块数据
├── page/            # 页面对象层（业务操作封装）
│   ├── sale/        # 销售模块页面
│   └── shopping/    # 购物模块页面
├── scripts/         # 测试脚本层（测试用例）
│   ├── sale/        # 销售模块测试
│   └── shopping/    # 购物模块测试
├── tools/           # 工具层
│   ├── get_driver.py      # 浏览器驱动管理
│   ├── get_log.py         # 日志记录工具
│   ├── read_json.py       # JSON数据读取
│   └── make_picture.py    # 滑块验证码处理
├── report/          # 测试报告目录
├── result/          # 测试结果目录
│   ├── image/       # 截图存储
│   └── log/         # 日志文件
├── conftest.py      # 全局配置
├── pytest.ini       # Pytest配置
├── requirements.txt # 依赖包
└── run_mian.py      # 运行入口
```

## 核心特性

### 1. 分层架构
- **conf层**：元素定位，与页面解耦
- **page层**：业务操作封装，继承common通用方法
- **scripts层**：测试用例，调用page层方法

### 2. 数据驱动
- 测试数据与代码分离
- JSON格式管理测试数据
- 支持多环境数据配置

### 3. 滑块验证码处理
- 基于OpenCV图像识别
- 自动计算滑动距离
- 模拟人工拖动轨迹

### 4. 日志与报告
- 详细的操作日志记录
- Allure可视化测试报告
- 自动截图保存

### 5. 智能等待
- 显式等待机制
- 防止元素未加载导致的错误
- 可配置超时时间

## 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行测试
```bash
# 方式1：运行指定测试文件
cd scripts/shopping
pytest test_login.py

# 方式2：使用主入口运行
python run_mian.py
```

### 生成报告
```bash
# 生成Allure报告
allure generate ../../report -o ../../report/html --clean
```
报告路径：`report/html/index.html`

报告包含：
- 测试用例执行情况
- 步骤详情和截图
- 执行时间统计
- 历史趋势分析


## 注意事项

1. 确保已安装Chrome浏览器和对应版本的ChromeDriver
2. 测试数据文件需放在data目录下
3. 元素定位表达式需根据实际页面调整
4. 建议使用虚拟环境管理依赖

## 许可证

MIT License
