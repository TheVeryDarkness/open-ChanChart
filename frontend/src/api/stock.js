import request from './request'

/**
 * Search stocks
 */
export function searchStocks(keyword, market = null) {
  return request({
    url: '/api/stock/search',
    method: 'get',
    params: { keyword, market }
  })
}

/**
 * Get K-line data
 */
export function getKlineData(params) {
  return request({
    url: '/api/stock/kline',
    method: 'get',
    params
  })
}
