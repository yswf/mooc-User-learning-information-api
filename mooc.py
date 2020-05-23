import requests
import json
#全局公用信息
csrfKey='None'
params = (
        ('csrfKey', csrfKey),
    )
headers = {
        
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'cookie': 'NTESSTUDYSI=None',
    }

#获取昵称,图像
def nickName(Id):
    memberId=Id
    data = {
    'memberId': memberId
    }
    url='https://www.icourse163.org/web/j/memberBean.getMocMemberPersonalDtoById.rpc'
    response = requests.post(url, headers=headers, params=params, data=data)
    datas=response.text#获得json信息
    json_data=json.loads(datas)#将返回json信息转化为字典类型
    nickName=json_data['result']['nickName']#昵称
    largeFaceUrl=json_data['result']['largeFaceUrl']#头像
    return nickName,largeFaceUrl
#获取学习时长
def learnLongTimeCount(Id):
    memberId=Id
    data = {
    'userId': memberId
    }
    url='https://www.icourse163.org/web/j/MocActivityScholarshipRpcBean.getActivityStatisticsByUser.rpc?csrfKey='+csrfKey
    response = requests.post(url, headers=headers, params=params, data=data)
    datas=response.text
    json_data=json.loads(datas)
    learnLongTimeCount=json_data['result']['statistics']['learnLongTimeCount']
    return learnLongTimeCount
#获取所选课程返回一个字符串列表
def courseName(Id):
    memberId=Id
    url='https://www.icourse163.org/web/j/learnerCourseRpcBean.getOtherLearnedCoursePagination.rpc'
    data = {
    'uid': memberId,
    'pageIndex': '1',
    'pageSize': '32'
    }
    response = requests.post(url, headers=headers, params=params, data=data)
    datas=response.text
    json_data=json.loads(datas)
    n=len(json_data['result']['list'])
    courseName=[]
    if(n==0):
        return'没选课'
    else:
        for i in range (n):
            courseName+=[(json_data['result']['list'][i]['courseName'])]
        return json_data
def main():
    #ID最小值为1017120000
    #下面为任意展示
    Id=1032127354
    for i in range(Id,1032127999):
            print("用户id:{}\n|昵称+头像|:\n|{}|→|学习时长{}分钟|\n所选课程↓\n{}".format(Id,nickName(Id),learnLongTimeCount(Id), courseName(Id)))
            print("=" * 100)
            Id=Id+1
main()  