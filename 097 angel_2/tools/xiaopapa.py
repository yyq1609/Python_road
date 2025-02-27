# import json
# import os
# from uuid import uuid4
#
# import requests
#
# from config import COVER_PATH, MUSIC_PATH, mongo
#


import json
import os
from uuid import uuid4

import requests
# 数据库配置
from pymongo import MongoClient

COVER_PATH = '../Covers'
MUSIC_PATH = '../Musics'
MG = MongoClient('localhost', 27017)
mongo = MG['Angel']
url = 'https://www.ximalaya.com/revision/play/album?albumId=291718&pageNum=1&sort=1&pageSize=30'
"""
钢琴曲
"""
# data = '{"ret":200,"msg":"声音播放数据","data":{"uid":0,"albumId":291718,"sort":1,"pageNum":1,"pageSize":30,"tracksAudioPlay":[{"index":30,"trackId":204667582,"trackName":"《夜色钢琴曲》你不知道de事 - 赵海洋","trackUrl":"/yinyue/291718/204667582","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":187,"src":"https://fdfs.xmcdn.com/group65/M07/59/FB/wKgMdF1RdPyz9cAaABc1h1qlvy8243.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"2天前","createTime":"2天前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":29,"trackId":202862216,"trackName":"《夜色钢琴曲》雨的印记 - 赵海洋","trackUrl":"/yinyue/291718/202862216","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":141,"src":"https://fdfs.xmcdn.com/group61/M06/73/C6/wKgMcF1HySnTQ9PgABGPHVnATfU286.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"9天前","createTime":"9天前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":28,"trackId":201146044,"trackName":"《夜色钢琴曲》像鱼 - 赵海洋","trackUrl":"/yinyue/291718/201146044","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":278,"src":"https://fdfs.xmcdn.com/group58/M05/A2/FA/wKgLc10-gDjx9OIPACJpYarvlv0924.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"16天前","createTime":"16天前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":27,"trackId":198986326,"trackName":"《夜色钢琴曲》远远遥望 - 赵海洋","trackUrl":"/yinyue/291718/198986326","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":244,"src":"https://fdfs.xmcdn.com/group63/M04/96/84/wKgMaF0x3rLwboy7AB4tq52GAqw155.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"19天前","createTime":"26天前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":26,"trackId":194700410,"trackName":"《夜色钢琴曲》蜗牛 - 赵海洋","trackUrl":"/yinyue/291718/194700410","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":166,"src":"https://fdfs.xmcdn.com/group63/M06/2C/84/wKgMaF0aCVXiI6QLABSQlRq-YyQ481.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"1月前","createTime":"1月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":25,"trackId":192110181,"trackName":"《夜色钢琴曲》只要平凡 - 赵海洋","trackUrl":"/yinyue/291718/192110181","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":253,"src":"https://fdfs.xmcdn.com/group61/M05/70/C1/wKgMcF0JCZuw9cSkAB9RrgvYaVU283.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"1月前","createTime":"1月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":24,"trackId":189791115,"trackName":"《夜色钢琴曲》胡广生 - 赵海洋","trackUrl":"/yinyue/291718/189791115","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":224,"src":"https://fdfs.xmcdn.com/group62/M06/6B/04/wKgMcVz8o7zg-mZKABvMEcBq7lw950.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"2月前","createTime":"2月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":23,"trackId":188059451,"trackName":"《夜色钢琴曲》星辰 - 赵海洋","trackUrl":"/yinyue/291718/188059451","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":215,"src":"https://fdfs.xmcdn.com/group60/M07/5F/DF/wKgLb1zyVXSi5pv-ABqzmf3Ij2U189.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"19天前","createTime":"2月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":22,"trackId":151321312,"trackName":"《夜色钢琴曲》烟花易冷 - 赵海洋","trackUrl":"/yinyue/291718/151321312","trackCoverPath":"//imagev2.xmcdn.com/group10/M05/5B/52/wKgDaVcpubzQe2tUAAFgmIO_2l8396.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":302,"src":"https://fdfs.xmcdn.com/group54/M06/B7/98/wKgLclw1gcDAkonkACVU3f2TSwI053.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"7月前","createTime":"7月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":21,"trackId":186306464,"trackName":"《夜色钢琴曲》你的远方 - 赵海洋","trackUrl":"/yinyue/291718/186306464","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":187,"src":"https://fdfs.xmcdn.com/group60/M08/64/31/wKgLb1zmO3mj312tABc6Vq7waHE914.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"19天前","createTime":"2月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":20,"trackId":184363025,"trackName":"《夜色钢琴曲》蝶恋 - 赵海洋","trackUrl":"/yinyue/291718/184363025","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":203,"src":"https://fdfs.xmcdn.com/group60/M00/CE/06/wKgLb1zeS3vyoYdBABkru-5uOnw058.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"2月前","createTime":"2月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":19,"trackId":181172977,"trackName":"《夜色钢琴曲》窗外的风景 - 赵海洋","trackUrl":"/yinyue/291718/181172977","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":212,"src":"https://fdfs.xmcdn.com/group60/M09/91/7E/wKgLeVzNkobi3ggxABo56-KAK7I124.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"19天前","createTime":"3月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":18,"trackId":178970147,"trackName":"《夜色钢琴曲》云烟成雨 - 赵海洋","trackUrl":"/yinyue/291718/178970147","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":255,"src":"https://fdfs.xmcdn.com/group58/M06/B0/40/wKgLglzBPyeAndW-AB-IBMPY6Qs339.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"3月前","createTime":"3月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":17,"trackId":175559165,"trackName":"《夜色钢琴曲》微风 - 赵海洋","trackUrl":"/yinyue/291718/175559165","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":207,"src":"https://fdfs.xmcdn.com/group60/M09/49/CD/wKgLb1yvS6PRCRkNABmsv_x0Wy4336.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"19天前","createTime":"4月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":16,"trackId":173751081,"trackName":"《夜色钢琴曲》棋子 - 赵海洋","trackUrl":"/yinyue/291718/173751081","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":215,"src":"https://fdfs.xmcdn.com/group55/M08/DC/E5/wKgLf1yluC7ztuRMABqmlyVKoAE795.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"4月前","createTime":"4月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":15,"trackId":170873339,"trackName":"《夜色钢琴曲》不染 - 赵海洋","trackUrl":"/yinyue/291718/170873339","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":235,"src":"https://fdfs.xmcdn.com/group55/M0B/D6/1D/wKgLdVyXr6GDxZBWAB0X7K2mZCA281.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"19天前","createTime":"4月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":14,"trackId":167913808,"trackName":"《夜色钢琴曲》盗将行 - 赵海洋","trackUrl":"/yinyue/291718/167913808","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":214,"src":"https://fdfs.xmcdn.com/group56/M04/A2/32/wKgLdlyJKZbyv82bABqGSo-IiuU637.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"4月前","createTime":"5月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":13,"trackId":162572031,"trackName":"《夜色钢琴曲》雪落下的声音 - 赵海洋","trackUrl":"/yinyue/291718/162572031","trackCoverPath":"//imagev2.xmcdn.com/group10/M05/5B/52/wKgDaVcpubzQe2tUAAFgmIO_2l8396.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":330,"src":"https://fdfs.xmcdn.com/group56/M0B/7F/20/wKgLdlxv8muyC4tTACjRoBKObJU716.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"4月前","createTime":"5月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":12,"trackId":160082897,"trackName":"《夜色钢琴曲》蓝色生死恋Reason - 赵海洋","trackUrl":"/yinyue/291718/160082897","trackCoverPath":"//imagev2.xmcdn.com/group10/M05/5B/52/wKgDaVcpubzQe2tUAAFgmIO_2l8396.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":131,"src":"https://fdfs.xmcdn.com/group56/M04/74/1D/wKgLgFxkG3KxsjkyABBBlCBRFng997.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"6月前","createTime":"6月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":11,"trackId":165412454,"trackName":"《夜色钢琴曲》寂静的环海东路-赵海洋","trackUrl":"/yinyue/291718/165412454","trackCoverPath":"//imagev2.xmcdn.com/group16/M02/5D/54/wKgDbFcpubOAcFbpAAFgmIO_2l8844.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":190,"src":"https://fdfs.xmcdn.com/group55/M02/A3/2E/wKgLf1x9W66AsRiJABeE0ehXXeo602.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"19天前","createTime":"5月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":10,"trackId":155208734,"trackName":"《夜色钢琴曲》今夜月光 - 赵海洋","trackUrl":"/yinyue/291718/155208734","trackCoverPath":"//imagev2.xmcdn.com/group53/M05/6B/1B/wKgLcVxJxBzB3MwPAANVqWHRN58645.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":204,"src":"https://fdfs.xmcdn.com/group53/M05/6B/15/wKgLcVxJxBSwtqnDABlR60tS3bs432.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"19天前","createTime":"6月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":9,"trackId":158196644,"trackName":"《夜色钢琴曲》恋曲1990 - 赵海洋","trackUrl":"/yinyue/291718/158196644","trackCoverPath":"//imagev2.xmcdn.com/group10/M05/5B/52/wKgDaVcpubzQe2tUAAFgmIO_2l8396.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":251,"src":"https://fdfs.xmcdn.com/group55/M05/AE/CE/wKgLf1xZA-GwzAgTAB8hcEqcuO4319.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"6月前","createTime":"6月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":8,"trackId":153464641,"trackName":"《夜色钢琴曲》追梦人 - 赵海洋","trackUrl":"/yinyue/291718/153464641","trackCoverPath":"//imagev2.xmcdn.com/group10/M05/5B/52/wKgDaVcpubzQe2tUAAFgmIO_2l8396.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":243,"src":"https://fdfs.xmcdn.com/group52/M06/AE/39/wKgLcFxBSuvRdSeSAB4nzXZTD3E586.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"6月前","createTime":"6月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":7,"trackId":148989642,"trackName":"《夜色钢琴曲》你瞒我瞒 - 赵海洋","trackUrl":"/yinyue/291718/148989642","trackCoverPath":"//imagev2.xmcdn.com/group10/M05/5B/52/wKgDaVcpubzQe2tUAAFgmIO_2l8396.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":242,"src":"https://fdfs.xmcdn.com/group54/M01/B2/E9/wKgLfVwpoWrhlzlSAB33nH36nrw071.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"7月前","createTime":"7月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":6,"trackId":146443400,"trackName":"《夜色钢琴曲》月亮 - 赵海洋","trackUrl":"/yinyue/291718/146443400","trackCoverPath":"//imagev2.xmcdn.com/group10/M05/5B/52/wKgDaVcpubzQe2tUAAFgmIO_2l8396.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":254,"src":"https://fdfs.xmcdn.com/group53/M01/8D/5B/wKgLcVwbr_rg8M96AB98vdwXQtE108.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"7月前","createTime":"7月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":5,"trackId":144319816,"trackName":"《夜色钢琴曲》飞走的雁 - 赵海洋","trackUrl":"/yinyue/291718/144319816","trackCoverPath":"//imagev2.xmcdn.com/group10/M05/5B/52/wKgDaVcpubzQe2tUAAFgmIO_2l8396.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":259,"src":"https://fdfs.xmcdn.com/group54/M0B/A0/44/wKgLfVwR_Ieg1X0MACAICeW1l3s853.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"19天前","createTime":"8月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":4,"trackId":141236276,"trackName":"《夜色钢琴曲》小城故事 - 赵海洋","trackUrl":"/yinyue/291718/141236276","trackCoverPath":"//imagev2.xmcdn.com/group10/M05/5B/52/wKgDaVcpubzQe2tUAAFgmIO_2l8396.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":174,"src":"https://fdfs.xmcdn.com/group52/M0A/53/9C/wKgLe1wDltvCVNVqABWhwWrWex0114.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"8月前","createTime":"8月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":3,"trackId":139367374,"trackName":"《夜色钢琴曲》思念的声音 - 赵海洋","trackUrl":"/yinyue/291718/139367374","trackCoverPath":"//imagev2.xmcdn.com/group10/M05/5B/52/wKgDaVcpubzQe2tUAAFgmIO_2l8396.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":182,"src":"https://fdfs.xmcdn.com/group49/M05/3A/62/wKgKmFv6X6ihPNaTABaIg6w53rw741.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"19天前","createTime":"8月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":2,"trackId":137566704,"trackName":"《夜色钢琴曲》哭砂 - 赵海洋","trackUrl":"/yinyue/291718/137566704","trackCoverPath":"//imagev2.xmcdn.com/group10/M05/5B/52/wKgDaVcpubzQe2tUAAFgmIO_2l8396.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":286,"src":"https://fdfs.xmcdn.com/group49/M0B/6E/FD/wKgKl1vxLYaTMSu9ACNjENIEnQE836.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"8月前","createTime":"8月前","isLike":false,"isCopyright":true,"firstPlayStatus":true},{"index":1,"trackId":135386132,"trackName":"《夜色钢琴曲》真永远 - 赵海洋","trackUrl":"/yinyue/291718/135386132","trackCoverPath":"//imagev2.xmcdn.com/group10/M05/5B/52/wKgDaVcpubzQe2tUAAFgmIO_2l8396.jpg","albumId":291718,"albumName":"《夜色钢琴曲》","albumUrl":"/yinyue/291718/","anchorId":16550049,"canPlay":true,"isBaiduMusic":false,"isPaid":false,"duration":266,"src":"https://fdfs.xmcdn.com/group51/M0A/70/31/wKgKnlvlRnGhNasCACD-7oKwNPk101.m4a","hasBuy":true,"albumIsSample":false,"sampleDuration":0,"updateTime":"8月前","createTime":"9月前","isLike":false,"isCopyright":true,"firstPlayStatus":true}],"hasMore":true}}'
"""
儿歌
"""
data = """{
    "ret": 200,
    "msg": "声音播放数据",
    "data": {
        "uid": 0,
        "albumId": 245037,
        "sort": 1,
        "pageNum": 1,
        "pageSize": 30,
        "tracksAudioPlay": [
            {
                "index": 11,
                "trackId": 4608410,
                "trackName": "我和星星打电话",
                "trackUrl": "/ertong/245037/4608410",
                "trackCoverPath": "//imagev2.xmcdn.com/group5/M04/D7/42/wKgDtVSJZ_PARwdiAADbM_v7Sf0613.jpg",
                "albumId": 245037,
                "albumName": "宝宝经典儿歌 - 网趣儿歌",
                "albumUrl": "/ertong/245037/",
                "anchorId": 7618912,
                "canPlay": true,
                "isBaiduMusic": false,
                "isPaid": false,
                "duration": 61,
                "src": "https://fdfs.xmcdn.com/group14/M04/50/DC/wKgDY1W0e0aTyWBqAAeRaG2X-bg781.m4a",
                "hasBuy": true,
                "albumIsSample": false,
                "sampleDuration": 0,
                "updateTime": "2年前",
                "createTime": "4年前",
                "isLike": false,
                "isCopyright": true,
                "firstPlayStatus": true
            },
            {
                "index": 10,
                "trackId": 4542816,
                "trackName": "虫儿飞",
                "trackUrl": "/ertong/245037/4542816",
                "trackCoverPath": "//imagev2.xmcdn.com/group5/M03/C3/F5/wKgDtlSBY6uy-nZ1AADbM_v7Sf0453.jpg",
                "albumId": 245037,
                "albumName": "宝宝经典儿歌 - 网趣儿歌",
                "albumUrl": "/ertong/245037/",
                "anchorId": 7618912,
                "canPlay": true,
                "isBaiduMusic": false,
                "isPaid": false,
                "duration": 97,
                "src": "https://fdfs.xmcdn.com/group13/M03/1F/6B/wKgDXVV6TO-ivqNQAAwaBkl9SK4828.m4a",
                "hasBuy": true,
                "albumIsSample": false,
                "sampleDuration": 0,
                "updateTime": "2年前",
                "createTime": "4年前",
                "isLike": false,
                "isCopyright": true,
                "firstPlayStatus": true
            },
            {
                "index": 9,
                "trackId": 2700962,
                "trackName": "小毛驴",
                "trackUrl": "/ertong/245037/2700962",
                "trackCoverPath": "//imagev2.xmcdn.com/group5/M00/06/1B/wKgDtVNwql_A4Qs6AADbM_v7Sf0828.jpg",
                "albumId": 245037,
                "albumName": "宝宝经典儿歌 - 网趣儿歌",
                "albumUrl": "/ertong/245037/",
                "anchorId": 7618912,
                "canPlay": true,
                "isBaiduMusic": false,
                "isPaid": false,
                "duration": 75,
                "src": "https://fdfs.xmcdn.com/group8/M05/49/A3/wKgDYVWtYnTCvNouAAlLQgOBy5M496.m4a",
                "hasBuy": true,
                "albumIsSample": false,
                "sampleDuration": 0,
                "updateTime": "2年前",
                "createTime": "5年前",
                "isLike": false,
                "isCopyright": true,
                "firstPlayStatus": true
            },
            {
                "index": 8,
                "trackId": 2787732,
                "trackName": "哈巴狗6",
                "trackUrl": "/ertong/245037/2787732",
                "trackCoverPath": "//imagev2.xmcdn.com/group5/M00/20/B0/wKgDtlOC9BHiIgnPAADbM_v7Sf0998.jpg",
                "albumId": 245037,
                "albumName": "宝宝经典儿歌 - 网趣儿歌",
                "albumUrl": "/ertong/245037/",
                "anchorId": 7618912,
                "canPlay": true,
                "isBaiduMusic": false,
                "isPaid": false,
                "duration": 97,
                "src": "https://fdfs.xmcdn.com/group7/M09/1F/DF/wKgDX1V6oBOAQFDwAAwebX5XC5c380.m4a",
                "hasBuy": true,
                "albumIsSample": false,
                "sampleDuration": 0,
                "updateTime": "2年前",
                "createTime": "5年前",
                "isLike": false,
                "isCopyright": true,
                "firstPlayStatus": true
            },
            {
                "index": 7,
                "trackId": 2835453,
                "trackName": "数鸭子",
                "trackUrl": "/ertong/245037/2835453",
                "trackCoverPath": "//imagev2.xmcdn.com/group5/M01/2E/2A/wKgDtlONb4-xth35AADbM_v7Sf0607.jpg",
                "albumId": 245037,
                "albumName": "宝宝经典儿歌 - 网趣儿歌",
                "albumUrl": "/ertong/245037/",
                "anchorId": 7618912,
                "canPlay": true,
                "isBaiduMusic": false,
                "isPaid": false,
                "duration": 78,
                "src": "https://fdfs.xmcdn.com/group12/M00/27/81/wKgDXFWDiiDwEVBdAAnCE4YWLRo372.m4a",
                "hasBuy": true,
                "albumIsSample": false,
                "sampleDuration": 0,
                "updateTime": "2年前",
                "createTime": "5年前",
                "isLike": false,
                "isCopyright": true,
                "firstPlayStatus": true
            },
            {
                "index": 6,
                "trackId": 3016609,
                "trackName": "春天在哪里",
                "trackUrl": "/ertong/245037/3016609",
                "trackCoverPath": "//imagev2.xmcdn.com/group4/M02/5A/92/wKgDtFOxBb2iu0jJAADbM_v7Sf0754.jpg",
                "albumId": 245037,
                "albumName": "宝宝经典儿歌 - 网趣儿歌",
                "albumUrl": "/ertong/245037/",
                "anchorId": 7618912,
                "canPlay": true,
                "isBaiduMusic": false,
                "isPaid": false,
                "duration": 136,
                "src": "https://fdfs.xmcdn.com/group11/M01/41/89/wKgDa1WiJBWTKv0hABDUQl4pu3U569.m4a",
                "hasBuy": true,
                "albumIsSample": false,
                "sampleDuration": 0,
                "updateTime": "2年前",
                "createTime": "5年前",
                "isLike": false,
                "isCopyright": true,
                "firstPlayStatus": true
            },
            {
                "index": 5,
                "trackId": 3381771,
                "trackName": "丢手巾",
                "trackUrl": "/ertong/245037/3381771",
                "trackCoverPath": "//imagev2.xmcdn.com/group4/M04/B5/C2/wKgDs1PrD7DzMafzAADbM_v7Sf0504.jpg",
                "albumId": 245037,
                "albumName": "宝宝经典儿歌 - 网趣儿歌",
                "albumUrl": "/ertong/245037/",
                "anchorId": 7618912,
                "canPlay": true,
                "isBaiduMusic": false,
                "isPaid": false,
                "duration": 72,
                "src": "https://fdfs.xmcdn.com/group8/M09/37/02/wKgDYVWWSOHwbf40AAju2EXjs7c020.m4a",
                "hasBuy": true,
                "albumIsSample": false,
                "sampleDuration": 0,
                "updateTime": "2年前",
                "createTime": "5年前",
                "isLike": false,
                "isCopyright": true,
                "firstPlayStatus": true
            },
            {
                "index": 4,
                "trackId": 3552930,
                "trackName": "妹妹背着洋娃娃",
                "trackUrl": "/ertong/245037/3552930",
                "trackCoverPath": "//imagev2.xmcdn.com/group4/M05/F2/8D/wKgDs1QFiE7gfOHJAADbM_v7Sf0962.jpg",
                "albumId": 245037,
                "albumName": "宝宝经典儿歌 - 网趣儿歌",
                "albumUrl": "/ertong/245037/",
                "anchorId": 7618912,
                "canPlay": true,
                "isBaiduMusic": false,
                "isPaid": false,
                "duration": 135,
                "src": "https://fdfs.xmcdn.com/group11/M03/2A/95/wKgDbVWGhmfy4IalABDIhefVyLE980.m4a",
                "hasBuy": true,
                "albumIsSample": false,
                "sampleDuration": 0,
                "updateTime": "2年前",
                "createTime": "5年前",
                "isLike": false,
                "isCopyright": true,
                "firstPlayStatus": true
            },
            {
                "index": 3,
                "trackId": 3787120,
                "trackName": "我的好妈妈",
                "trackUrl": "/ertong/245037/3787120",
                "trackCoverPath": "//imagev2.xmcdn.com/group4/M07/2D/61/wKgDs1QiZS2iUkMjAADbM_v7Sf0533.jpg",
                "albumId": 245037,
                "albumName": "宝宝经典儿歌 - 网趣儿歌",
                "albumUrl": "/ertong/245037/",
                "anchorId": 7618912,
                "canPlay": true,
                "isBaiduMusic": false,
                "isPaid": false,
                "duration": 97,
                "src": "https://fdfs.xmcdn.com/group13/M06/27/84/wKgDXlWDEjTThUelAAwROYNwy1A141.m4a",
                "hasBuy": true,
                "albumIsSample": false,
                "sampleDuration": 0,
                "updateTime": "2年前",
                "createTime": "4年前",
                "isLike": false,
                "isCopyright": true,
                "firstPlayStatus": true
            },
            {
                "index": 2,
                "trackId": 3910552,
                "trackName": "好爸爸坏爸爸",
                "trackUrl": "/ertong/245037/3910552",
                "trackCoverPath": "//imagev2.xmcdn.com/group4/M07/58/69/wKgDtFQ077Gj-AgPAADbM_v7Sf0175.jpg",
                "albumId": 245037,
                "albumName": "宝宝经典儿歌 - 网趣儿歌",
                "albumUrl": "/ertong/245037/",
                "anchorId": 7618912,
                "canPlay": true,
                "isBaiduMusic": false,
                "isPaid": false,
                "duration": 92,
                "src": "https://fdfs.xmcdn.com/group9/M03/20/3C/wKgDYlV7N5jSMSKxAAt1vH442gg258.m4a",
                "hasBuy": true,
                "albumIsSample": false,
                "sampleDuration": 0,
                "updateTime": "2年前",
                "createTime": "4年前",
                "isLike": false,
                "isCopyright": true,
                "firstPlayStatus": true
            },
            {
                "index": 1,
                "trackId": 3910822,
                "trackName": "三个和尚",
                "trackUrl": "/ertong/245037/3910822",
                "trackCoverPath": "//imagev2.xmcdn.com/group4/M09/58/71/wKgDtFQ08OvDAYYeAADbM_v7Sf0668.jpg",
                "albumId": 245037,
                "albumName": "宝宝经典儿歌 - 网趣儿歌",
                "albumUrl": "/ertong/245037/",
                "anchorId": 7618912,
                "canPlay": true,
                "isBaiduMusic": false,
                "isPaid": false,
                "duration": 238,
                "src": "https://fdfs.xmcdn.com/group7/M08/50/D7/wKgDWlW0XxfzI_c6AB1-C-GYos0708.m4a",
                "hasBuy": true,
                "albumIsSample": false,
                "sampleDuration": 0,
                "updateTime": "2年前",
                "createTime": "4年前",
                "isLike": false,
                "isCopyright": true,
                "firstPlayStatus": true
            }
        ],
        "hasMore": false
    }
}
"""

data = json.loads(data)
data_list = data.get('data').get('tracksAudioPlay')
print(len(data_list))
content_list = []


def get_data(data_list):
    for content_info in data_list:
        filename = uuid4()
        content = {
            'title': content_info['trackName'],
            'zhuanji': content_info['albumName'],
            'cover': '',
            'music': ''
        }
        url_cover = 'http:' + content_info['trackCoverPath']
        url_music = content_info['src']
        path_cover = os.path.join(COVER_PATH, f'{filename}.jpg')
        path_music = os.path.join(MUSIC_PATH, f'{filename}.mp3')
        content['cover'] = f'{filename}.jpg'
        content['music'] = f'{filename}.mp3'

        # 获取图片流
        cover_res = requests.get(url_cover)
        with open(path_cover, mode='wb') as f:
            f.write(cover_res.content)
        # 获取音乐流
        music_res = requests.get(url_music)
        with open(path_music, mode='wb') as f:
            f.write(music_res.content)
        content_list.append(content)

    mongo.content.insert_many(content_list)


if __name__ == '__main__':
    get_data(data_list)
