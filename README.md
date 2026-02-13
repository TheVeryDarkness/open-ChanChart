# ChanChart - 缠论股票图表可视化系统

## 一、项目核心需求
实现股票K线与缠论核心结构（笔、段、中枢）的可视化展示，支持股票选择、周期切换、缠论参数配置，提供清晰的缠论结构数据查询接口。

## 二、技术框架
### 2.1 前端技术框架
Vue3 + Vite + Element Plus + ECharts

### 2.2 后端技术框架
Python + FastAPI + Uvicorn + MySQL + Redis

## 三、功能需求
### 3.1 前端功能需求
- K线图表绘制：支持日K、30F、5F等周期K线展示

- 缠论结构可视化：叠加展示缠论笔（红/绿线段）、段（粗线）、中枢（矩形框）

- 股票选择功能：支持股票代码/名称模糊搜索、沪深A股切换，记忆最近选择股票

- 缠论参数配置：可配置顶底分型确认K线数、中枢级别、是否显示包含关系处理

- 交互功能：鼠标滚轮缩放K线、悬停显示缠论结构详情、周期切换、数据刷新

- 接口对接：封装后端API请求，处理请求/响应、异常提示

- 全局状态管理：存储选中股票、周期、缠论参数等全局状态

### 4.1 后端功能需求
- 行情数据接口：接收前端请求，从Tushare/Akshare获取股票K线数据，缓存至Redis

- 缠论算法实现：顶底分型识别（处理包含关系）、笔生成、段生成、中枢识别

- 缠论数据接口：接收前端请求，返回股票对应周期的缠论笔、段、中枢数据

- 股票搜索接口：支持股票名称/代码模糊搜索，返回匹配股票列表

- 数据校验：校验行情数据完整性（缺失K线、价格异常），返回标准化格式数据

- 缓存管理：缓存高频查询的K线、缠论数据（1小时过期），减少数据源调用

- 异常处理：统一捕获算法计算、接口请求异常，返回标准化错误信息

- 数据操作：MySQL存储股票基础信息、历史K线数据，提供增删改查操作

## 四、项目结构
### 4.1 前端项目结构
```text
frontend/
├── src/
│   ├── api/                # 接口封装（对接后端API）
│   │   ├── stock.js        # 股票行情相关接口
│   │   └── chan.js         # 缠论数据相关接口
│   ├── components/         # 通用组件
│   │   ├── KlineChart.vue  # K线+缠论图表核心组件
│   │   ├── StockSelector.vue  # 股票选择组件
│   │   └── ChanParams.vue    # 缠论参数配置组件
│   ├── store/              # Pinia状态管理（全局状态存储）
│   ├── utils/              # 工具函数（请求、格式化等）
│   ├── views/              # 页面视图
│   │   ├── Home.vue        # 首页（核心图表展示）
│   │   └── History.vue     # 历史数据查看页
│   ├── App.vue             # 根组件
│   └── main.js             # 前端入口文件
├── .env.development        # 开发环境配置
├── package.json            # 前端依赖清单
└── vite.config.js          # Vite配置文件
```

### 4.2 后端项目结构
```text
backend/
├── app/
│   ├── api/                   # 路由层
│   │   ├── route.py           # 路由接口
│   │   ├── stock.py           # 股票行情接口
│   │   └── chan.py            # 缠论数据接口
│   ├── core/                  # 核心逻辑
│   │   ├── chan_algorithm.py  # 缠论核心算法实现
│   │   └── data_processor.py  # 行情数据处理与校验
│   ├── service/               # 服务层
│   │   ├── stock_service.py   # MySQL数据增删改查
│   │   └── cache_service.py   # Redis缓存操作
│   ├── models/                # 数据模型（Pydantic校验）
│   │   ├── stock_model.py     # K线数据模型
│   │   └── chan_model.py      # 缠论数据模型
│   ├── utils/                 # 后端工具函数
│   └── main.py                # 后端入口文件
├── .env                       # 后端环境变量（数据源Token、缓存配置等）
├── requirements.txt           # 后端依赖清单
└── run.py                     # 后端启动脚本
```

## 五、API接口

### 5.1 股票搜索接口
- 请求方式： GET
- 接口路径： /api/stock/search
- 请求参数：
  - `keyword`：股票名称或代码（必填）
  - `market`：市场类型（可选，默认为`sh`，可选值为`sh`、`sz`）
- 响应示例：
```json
{
  "code": 200,
  "message": "Success",
  "data": [
    {
      "code": "000001",
      "name": "平安银行",
      "market": "sz"
    }
  ]
}
```

### 5.2 股票K线数据接口
- 请求方式： GET
- 接口路径： /api/chan/kline
- 请求参数：
  - `code`：股票代码（必填）
  - `market`：市场类型（可选，默认为`sh`，可选值为`sh`、`sz`）
  - `period`：周期（可选，默认为`D`，可选值为`D`、`30F`、`5F`）
  - `start_date`：开始日期（可选，格式为`YYYY-MM-DD`）
  - `end_date`：结束日期（可选，格式为`YYYY-MM-DD`）
- 响应示例：
```json
还没想好
```