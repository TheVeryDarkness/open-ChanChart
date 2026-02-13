"""股票数据API接口"""
from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from datetime import datetime, timedelta
import random

from app.models.stock_model import StockInfo, KlineData

router = APIRouter(prefix="/api/stock", tags=["stock"])


# 模拟股票数据库
MOCK_STOCKS = [
    {"code": "000001", "name": "平安银行", "market": "sz"},
    {"code": "000002", "name": "万科A", "market": "sz"},
    {"code": "600000", "name": "浦发银行", "market": "sh"},
    {"code": "600036", "name": "招商银行", "market": "sh"},
    {"code": "600519", "name": "贵州茅台", "market": "sh"},
    {"code": "000858", "name": "五粮液", "market": "sz"},
]


@router.get("/search", response_model=dict)
async def search_stocks(
    keyword: str = Query(..., description="股票名称或代码"),
    market: Optional[str] = Query(None, description="市场类型 sh/sz")
):
    """
    搜索股票
    """
    results = []
    
    for stock in MOCK_STOCKS:
        # 匹配关键词
        if keyword.lower() in stock["code"].lower() or keyword in stock["name"]:
            # 如果指定了市场，则过滤
            if market is None or stock["market"] == market:
                results.append(stock)
    
    return {
        "code": 200,
        "message": "Success",
        "data": results
    }


@router.get("/kline", response_model=dict)
async def get_kline_data(
    code: str = Query(..., description="股票代码"),
    market: str = Query(default="sh", description="市场类型"),
    period: str = Query(default="D", description="周期 D/30F/5F"),
    start_date: Optional[str] = Query(None, description="开始日期 YYYY-MM-DD"),
    end_date: Optional[str] = Query(None, description="结束日期 YYYY-MM-DD")
):
    """
    获取股票K线数据
    """
    # 生成模拟数据
    if end_date is None:
        end = datetime.now()
    else:
        end = datetime.strptime(end_date, "%Y-%m-%d")
    
    if start_date is None:
        start = end - timedelta(days=90)  # 默认90天
    else:
        start = datetime.strptime(start_date, "%Y-%m-%d")
    
    # 生成模拟K线数据
    klines = []
    current_date = start
    base_price = 100.0
    
    while current_date <= end:
        # 跳过周末
        if current_date.weekday() < 5:
            # 生成随机价格波动
            change = random.uniform(-0.05, 0.05)
            base_price = base_price * (1 + change)
            
            open_price = base_price + random.uniform(-2, 2)
            close_price = base_price + random.uniform(-2, 2)
            high_price = max(open_price, close_price) + random.uniform(0, 3)
            low_price = min(open_price, close_price) - random.uniform(0, 3)
            volume = random.uniform(100000, 500000)
            
            klines.append({
                "date": current_date.strftime("%Y-%m-%d"),
                "open": round(open_price, 2),
                "high": round(high_price, 2),
                "low": round(low_price, 2),
                "close": round(close_price, 2),
                "volume": round(volume, 0)
            })
        
        current_date += timedelta(days=1)
    
    return {
        "code": 200,
        "message": "Success",
        "data": {
            "code": code,
            "market": market,
            "period": period,
            "klines": klines
        }
    }
