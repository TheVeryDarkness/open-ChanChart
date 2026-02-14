import request from './request'

/**
 * Get Chan theory analysis data
 */
export function getChanAnalysis(params) {
  return request({
    url: '/api/chan/analysis',
    method: 'get',
    params
  })
}
