# -*- coding: utf-8 -*-
print '***水果问答***'

fortune = {
    '草莓':'幸运',
    '橘子':'努力',
    '苹果':'骄傲'
    }

while True:
    ans = raw_input('请你说出你喜欢的水果:')
    if not ans:
        print '****再见****'
        break
    if fortune.has_key(ans):
        print ('喜欢%s的你%s.'%(ans,fortune[ans]))
    else:
        fortune[ans] = raw_input('不知道什么是%s请回答:'%ans)
