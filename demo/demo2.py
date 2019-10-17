#coding=utf-8
from weibopy import WeiboOauth2,WeiboClient
import webbrowser
import time
import re
from collections import defaultdict
import snownlp
from pyecharts import Map
import echarts_china_provinces_pypkg
import echarts_countries_pypkg

client_key='639887680'
client_secret='fe072eade69680cbdfd8e7b1801ab22f'
redirect_url='https://api.weibo.com/oauth2/default.html'
auth=WeiboOauth2(client_key,client_secret,redirect_url)
webbrowser.open_new(auth.authorize_url)


code=input('输入code\n')
token=auth.auth_access(code)
print(token)
print("\n\n")
client=WeiboClient(token['access_token'])
result=client.get(suffix='comments/show.json',params={'id':111680,'count':100,'page':1})
print(result)
province_list = defaultdict(list) # 保存按省划分的评论正文
comment_text_list = [] # 保存所有评论正文

# 获取「自杀式单身」评论列表
# 共获取 10 页 * 每页最多 200 条评论
for i in range(1, 11):
    result = client.get(suffix='comments/show.json', params={'id': 4322140368509204, 'count': 200, 'page': i})

    comments = result['comments']
    if not len(comments):
        break

    for comment in comments:
        text = re.sub('回复.*?:', '', str(comment['text']))
        province = comment['user']['province']
        province_list[province].append(text)
        comment_text_list.append(text)

    print('已抓取评论 {} 条'.format(len(comment_text_list)))
    time.sleep(1)

    provinces={}
    results=client.get(suffix='common/get_province.json',params={'country':'001'})
    for prov in results:
        for code,name in prov.items():
            provinces[code]=name
    print(provinces)



    # 评论情感分析
    positives={}
    for province_code,comments in province_list.items():
        sentiment_list=[]
        for text in comments:
            s=snownlp.SnowNLP(text)
            sentiment_list.append(s.sentiments)
        # 统计平均情感
        positive_number=sum(sentiment_list)
        positive=positive_number/len(sentiment_list)*100

        # 按省保存数据, 0010 为国家前缀
        province_code='0010'+str(province_code)
        if province_code in provinces:
            provice_name=provinces[province_code]
            positives[provice_name]=int(positive)

    # 绘制情感分布图
    keys=list(positives.keys())
    values=list(positives.values())
    map1=Map("自杀式单身 情感分析地域图",width=1200,height=600)
    map1.add("积极情感",keys,values,visual_range=[0,100],maptype='china',is_visualmap=True,is_label_show=True,
            visual_text_color='#000')
    map1.render(path="单身热评分布.html")