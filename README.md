# mooc-User-learning-information-api
User learning information api用户在mooc平台上学习情况api
=======
通过post提交用户Id返回用户学习情况。（以我信息为例，仅需要Id，不需要登录后其他cookies身份信息）
=============
id为大于1015002001十位数，最大值自己注册最新账号看
经过仔细观察找到接口,接口传参是以post形式提交请求返回参数的,提交过程中params中的csrfKey和浏览器cookie中NTESSTUDYSI以及请求地址末尾参数做校验,所以只要csrfkey中数值和NTESSTUDYSI一样就行，随便你填什么，只要是字符串
id查看方法https://www.icourse163.org/home.htm?userId=XXXXXXXXXX   去mooc中国大学mooc平台个人中心查看。

1.https://www.icourse163.org/web/j/memberBean.getMocMemberPersonalDtoById.rpc #返回用户头像，昵称等信息
<br>post提交data  ` {memberId: xxxxxxxxxx}` <br>
返回json：<br>
`
 {'code': 0, 'result': {'memberId': 1032127354, 'schoolName': '其他', 'schoolId': None, 'nickName': '游尚忘烦', 'largeFaceUrl': 'https://img-ph-mirror.nosdn.127.net/y-3-D05OabXYiLo3y6G00w==/6632377284050677150.jpg', 'department': '其他', 'memberType': 1, 'highestDegree': 5, 'jobName': None, 'description': None, 'richDescription': None, 'lectorTitle': None, 'realName': None, 'isTeacher': False, 'followCount': 3, 'followedCount': 0, 'schoolShortName': None, 'logoForCertUrl': None, 'supportMooc': None, 'supportSpoc': None, 'followStatus': False, 'supportCommonMooc': None, 'supportPostgradexam': None, 'lectorTag': None, 'relType': None}, 'message': '', 'traceId': '', 'sampled': False}
 ` 


2.https://www.icourse163.org/web/j/MocActivityScholarshipRpcBean.getActivityStatisticsByUser.rpc #返回平台参与度信息，包含需要学习时长等
<br>post提交data  ` {memberId: xxxxxxxxxx}` <br>
返回json：<br>

`
{'code': 0, 'result': {'isSign': None, 'statistics': {'signCount': 0, 'courseCount': 0, 'postCount': 1, 'voteCount': 0, 'replyCount': 7, 'commentCount': 0, 'learnLongTimeCount': 4470}}, 'message': '', 'traceId': '', 'sampled': False}
` 


3.https://www.icourse163.org/web/j/learnerCourseRpcBean.getOtherLearnedCoursePagination.rpc #返回所学习课程信息，最近学习靠前
<br>post提交参数信息：<br>

` {
'uid': XXXXXXXXXXX,
'pageIndex': '1',
'pageSize': '32'
}` 
<br>
返回json：
<br>


`
{'code': 0, 'result': {'query': {'sortCriterial': None, 'DEFAULT_PAGE_SIZE': 10, 'DEFAULT_PAGE_INDEX': 1, 'DEFAULT_TOTLE_PAGE_COUNT': 1, 'DEFAULT_TOTLE_COUNT': 0, 'DEFAULT_OFFSET': 0, 'pageSize': 32, 'pageIndex': 1, 'totlePageCount': 1, 'totleCount': 1, 'offset': 0, 'limit': 32}, 'list': [{'uid': 1032127356, 'courseCoverUrl': 'http://edu-image.nosdn.127.net/65B575B91765DBCD593C825AB376F329.jpeg?imageView&thumbnail=426y240&quality=100', 'courseId': 53004, 'courseProductType': 1, 'courseName': '高等数学（一）', 'enrollCount': 109782, 'schoolName': '同济大学', 'schoolId': 8013, 'schoolShortName': 'TONGJI', 'whatCertGot': None, 'termId': 50003, 'supportCommonMooc': None, 'mode': 0, 'termPrice': None, 'termOriginalPrice': None}]}, 'message': '', 'traceId': '', 'sampled': False}
` 


这个接口是我做python爬虫课设时候发现的，已经咨询过平台，为公开可查信息，第一次在github发项目，不是很懂，觉得还不错希望给个star⭐
发之前搜索下应该是GitHub首发。
例子为我写一个py爬虫，关于接口更多python爬虫使用信息请转到[爬取了中国大学mooc平台7万多用户学习情况发现](https://wantofun.cn/index.php/archives/114)

![](https://github.com/yswf/mooc-User-learning-information-api/blob/master/eg.png) 
