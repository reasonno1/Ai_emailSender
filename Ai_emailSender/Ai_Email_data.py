
from email.mime.text import MIMEText
import smtplib
import os

def email_subject(index):
    if index == 0:
        subject = r"<首次輸出申請>專案_"
    elif index == 1:
        subject = r"<修改輸出申請>專案_"
    elif index == 2:
        subject = r"<燈光構圖輸出申請>專案_"

    return subject


def email_dest(ben_chk, rick_chk, ccw_chk, rozy_chk):
    dest = []
    email_list = ["數位傳達部-林羣晏 <benjaminlin@aistyle.com>"
                  , "數位傳達部-許羽樑 <rickhsu@aistyle.com>"
                  , "數位傳達部-王筑君 <chuchunwang@aistyle.com>"
                  , "數位傳達部-邱奕珊 <rozychiu@aistyle.com>"]
    # email_list = ["canchen@aistyle.com", "canchen@aistyle.com", "canchen@aistyle.com"]

    if ben_chk:
        dest.append(email_list[0])
    if rick_chk:
        dest.append(email_list[1])
    if ccw_chk:
        dest.append(email_list[2])
    if rozy_chk:
        dest.append(email_list[3])

    return dest


def email_content(index, exp_path, ref_path, final_path, maxfile_ary):
    content =""

    if index == 0 :
        content ="""\

專案紀錄:

%s

檔案輸出:

%s

Final:

%s

        """ % (ref_path, exp_path, final_path)
    elif index == 1:
        content = """\

專案紀錄:

%s

檔案輸出:

%s

Final更新:

%s

        """ % (ref_path, exp_path, final_path)
    elif index == 2:
        content = """\

專案紀錄:

%s

檔案輸出:

%s

檔案連結:

%s

        """ % (ref_path, exp_path, maxfile_ary)

    return content



def email_send(USERNAME, PASSWORD, sender, dest, email_sub, content):

    SMTPserver = r"webmail.aistyle.com"
    msg = MIMEText(content)
    msg['Subject'] = email_sub
    msg['From'] = sender

    ai_smtp = smtplib.SMTP()
    ai_smtp.connect(host=SMTPserver, port=25)
    ai_smtp.login(USERNAME, PASSWORD)

    dest.append(sender)

    try:
        ai_smtp.sendmail(sender, dest, msg.as_string())
    finally:
        ai_smtp.quit()


def get_space_name(path):

    cht_data = {'LVR': '客廳',
                'ENT': '玄關',
                'BAT': '浴室',
                'GSB': '客浴',
                'MSB': '主浴',
                'KIT': '廚房',
                'LOB': '大廳',
                'MSR': '主臥',
                'BAR': '臥房',
                'STR': '書房',
                'GSR': '客房',
                'KDR': '小孩房',
                'DNR': '用餐區',
                'MOP': '多功能室',
                'SWP': '游泳池',
                'GYM': '健身房',
                'BLC': '陽台',
                'MDR': '視聽室',
                'GDR': '警衛室',
                'ELL': '梯廳',
                'PRK': '停車場',
                'GMR': '遊戲室',
                'RSR': '休憩室',
                'FTR': '更衣室',
                'RCR': '接待室',
                'ROF': '屋凸',
                'ELV': '乘廂',
                'ETR': '娛樂室',
                'BOR': '宴會廳',
                'PIA': '琴房',
                'BEN': '練團室',
                'VIP': 'VIP',
                'LCR': '階梯教室',
                'PIA': '琴房',
                'BEN': '練團室',
                'VIP': 'VIP',
                'LCR': '階梯教室',
                'LDR': '洗衣間',
                'YGR': '瑜珈室',
                'MLR': '信箱室'
                }

    name = []
    cht_name = []
    if len(os.listdir(path))!=0:

        for file in os.listdir(path):
            temp = file.split("_")

            if len(temp) > 2:
                if not temp[1] in name:
                    name.append(temp[1])

    if len(name) != 0:
        for i in name:
            print(i)
            try:
                cht_name.append(cht_data[str(i)])
            except KeyError:
                cht_name.append(str(i))

    return (", ".join(cht_name))
