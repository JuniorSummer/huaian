import requests
from lxml import etree

def spider(tid):
	# 注意这边要换成对应服务器的public ip
	url=f'http://39.103.59.219/forum.php?mod=viewthread&tid={tid}'
	header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
	response=requests.get(url,headers=header)
	
	if response.status_code == 200:
		if "抱歉，指定的主题不存在或已被删除或正在被审核" not in response.text:
			html=etree.HTML(response.text)
			username=html.xpath(f'//*[@id="favatar{tid}"]/div[1]/div/a/text()')[0]
			score=html .xpath(f'//*[@id="favatar{tid}"]/dl[1]/dd/a/text()')[0]
			level=html.xpath(f'//*[@id="favatar{tid}"]/p[1]/em/a/text()')[0]
			title=html.xpath(f'//*[@id="thread_subject"]/text()')[0]
			content=html.xpath(f'//*[@id="postmessage_{tid}"]/text()')[0].strip()
			line=f'{tid},{username},{score},{level},{title},{content}\n'
			return line
	
def main():
	output_file=open('./data.txt','w',encoding='utf-8')
	max_tid=6000
	for tid in range(1,max_tid):
		line=spider(tid)
		if line:
			output_file.write(line)
	output_file.close()

if __name__=='__main__':
	main()
	print('done!')