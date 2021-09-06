import json
import random
#import time , datetime

from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json' , 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

option_1 = "【誕生数６】\n痛みと苦しみに耐えていた時期が過ぎて、あなたの前に新たな展開、展望が広がってきました。これまで辛かった分を上回るほど、あなたは新たな展開に大きく期待が出来ますし、現在のところに留まらず、どこへでも飛んで行ける自由さも手に入れました。閉ざされ引き止められていた自分の根から起き上がり、これからはあまり深刻にならずに、もっともっと人生を楽しむ方向に舵を切りましょう。明るいきらめきの世界が広がっていることを信じてください。"
option_2 = "【誕生数６】\n今、あなたはこの地を離れることを望んでいるか、人間関係において距離を置きたい人がいるでしょうか。心の中では望んでいるのに、人からどう見られるか、何と言われるかということが気になり過ぎていませんか？でもあなたの人生はあなたのもので、やりたい事を我慢しても誰も責任は取ってくれません。あなたの本当の声を聴き、自分の人生を自分で導きましょう。"
option_3 = "【誕生数６】\nあなたは、偉大な発展と祝福の時期に入りました。あなたは、豊穣、祝福、歓待の季節にいざなわれています。今こそ、人生があなたにその実りで報いる時期なのです。あなたは婚約したり、結婚したり、昇格したり、何かを獲得したり、あるいは長く待たれたラッキーな休暇を得るかも知れません。/nあなたが何を望もうとも、確実にそれが来ているので準備をしましょう。人生の潮の流れがあなたの方へ向いてきており、それはあなたがしっかりと努力をしてきたことや、あなたが夢や目標に誓いを立て、コミットしてきたことへの当然の結果なのです。/n/n「パーティーの計画を立てなさい。すぐに、その祝福の理由が分かります」"
#option_4 = "確率分散 1"
#option_5 = "確率分散 2"
#option_6 = "確率分散 3"

def main():
    USER_ID = info['USER_ID']
    mylist = [ option_1,option_2,option_3]    
    messages1= TextSendMessage(random.choice(mylist))
    #messages = TextSendMessage(text=random.choice(mylist))
    #messages2= TextSendMessage(text = "今日も1日頑張りましょう♪")
    # today = datetime.datetime.fromtimestamp(time.time())
    #time  = today.strftime('%H')      
 
     #   if int(time) > 20 :
    line_bot_api.broadcast(messages1)
     #   else :
    #line_bot_api.broadcast(messages2)  
    
if __name__ == "__main__" :
    main()
