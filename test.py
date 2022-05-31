import requests
import re
import base64
import subprocess
headers ={'Cookie': 'ttcid=adbb8905cd1444f2aefad02743e3d55710; MONITOR_WEB_ID=c4c86636-acef-4da4-8b1d-42f7b3efc3d0; ttwid=1%7CA6SG_rNJrqHYrQ4eyPkK7u3n34WXEOdTQjsur3AIS5I%7C1648704646%7C12c5d9cf70430add3ea7924019458285c0c385fcf78183e12c2b552690c14c30; _tea_utm_cache_1300=undefined; ixigua-a-s=1; support_webp=true; support_avif=true; __ac_nonce=062453c70007e2f23dded; __ac_signature=_02B4Z6wo00f01D5esOQAAIDBuHaVQta5aFg-f7RAAG3Za8RHYpuZb0ClOgeSBjNGv4KiMhhgqHKg4bsimHLf1L--hi1dqBtnnm4ROlE2jebJ8KRv1MXNPX7E9spguTMVGNZ3Agybem6MuDqv84; msToken=wux9BNwjPzI765u7KUgt2wi80tz4I1GgLAzI22fuSsHDpDe2lu7lviS4D2_5MAmqR2hkurNolqJf53_kGUV4Ux6mbiaJJcIZ86L5L5ELoWQyjDMIlF9uvVr0HRBQNU0=; tt_scid=E9UoJeM1ywphoPAsrfZCttebr4R6fBE3XXvk6VqaNgazK6ZdQeQWEIPS9ahdQ3Qg89f3',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0'}
url = 'https://www.ixigua.com/7073276658265883149'
response = requests.get(url,headers=headers)
response.encoding='utf-8'
#长视频的格式基本上都是m3u8  大视频可以分割成好几个小片段每个片段都是一个小视频 节约宽带
html_data=(response.text)
main_url_list=re.findall('"main_url":"(.*?)"',html_data)
#for main_url in main_url_list:
#    print(base64.b64decode(main_url))
#第四个是最大的视频 倒数第二个是音频
video_url=main_url_list[3]
audio_url=main_url_list[-2]
video_url=base64.b64decode(video_url)
audio_url=base64.b64decode(audio_url)

video_url=str(video_url).replace(r'.\xd3M\x85','?')[2:-1]
audio_url =audio_url.decode()
print(video_url)
print(audio_url)
video_data=requests.get(video_url).content

'''
with  open(f'data/{title}',mode='wb')as f:
    f.write(video_data)
audio_url =requests.get(audio_url).content
with  open(f'/data/{title}',mode='wb')as f:
    f.write(audio_url)
cmd =r'ffmpeg -i'+'data/'+title+'.mp4 -i'+'data/'+title+'.mp3 -acodec copy -vcodec copy '+"data/"+title+'out.mp4 '
subprocess.run(cmd,shell=True)
'''







