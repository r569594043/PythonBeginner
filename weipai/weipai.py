# http://www.weipai.cn/square/video/popular?page=1
# http://www.weipai.cn/square/video/popular?page=2
# http://www.weipai.cn/video/play/id/52ca974be34167c91c8b4612/type/theater/source/web?_=1389692311345

import sys, os, os.path, re, time, base64, logging, logging.config
import urllib.request, urllib.parse
from bs4 import BeautifulSoup as bs

CURDIR = os.path.dirname(sys.argv[0])
os.chdir(CURDIR)

WEIPAI_PAGE_URL = 'http://www.weipai.cn/square/video/popular'

WEIPAI_VIDEO_URL = 'http://www.weipai.cn/video/play/id/{0}/type/theater/source/web'

REG = re.compile(r"s=(.*?)',")
REG1 = re.compile(r"p=(.*?)&")

LOG_CONFIG = 'weipai.conf'

def analysis_video(video_id):
	'''
		analysis the video url by video id
	'''
	video_url = None
	logger.info('start analysis video: ' + video_id)
	params = {
		'_': int(time.time()*1000)
	}
	try:
		video_info = urllib.request.urlopen(WEIPAI_VIDEO_URL.format(video_id) + '?' + urllib.parse.urlencode(params)).read().decode()
		logger.debug('video_info: ' + video_info)
		m = REG.search(video_info)
		if m:
			video_url_encrypted = m.group(1)
			video_params = base64.b64decode(video_url_encrypted).decode()
			logger.debug('video_params: ' + video_params)
			m1 = REG1.search(video_params)
			if m1:
				video_url = m1.group(1)
				logger.debug('video_url: ' + video_url)
				return video_url
			else:
				logger.error("video_params didn't match regex: " + video_params)
		else:
			logger.error("video_info didn't match regex: " + video_info)
	except Exception as ex:
		logger.exception('error during analysis video')
	else:
		logger.info('end analysis video: ' + video_id)
	return video_url

def main():
	'''
	main method
	'''
	global logger
	logging.config.fileConfig(LOG_CONFIG)
	logger = logging.getLogger("weipai")
	logger.info('begin analysis...')
	f = open('weipai.downlist', 'w')
	for i in range(0, 100):
		logger.info('start analysis page: {0}'.format(i + 1))
		params = {
			'page': i + 1
		}
		try:
			html_doc = urllib.request.urlopen(WEIPAI_PAGE_URL + '?' + urllib.parse.urlencode(params)).read().decode()
			bs_doc = bs(html_doc)
			for div in bs_doc.select('div.wf_cell.video.box'):
				video_url = analysis_video(div['id'])
				if video_url:
					f.write(video_url)
					f.write(os.linesep)
				else:
					logger.error('analysis video: {0} failed'.format(div['id']))
			f.flush()
		except Exception as ex:
			logger.exception('error during analysis page')
		else:
			logger.info('end analysis page: ' + str(i + 1))
	f.close()
	logger.info('end analysis...')
		
if __name__ == "__main__":
	main()