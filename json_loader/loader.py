__author__ = 'alex'
import json
import sys

'''
Json does not have syntax to define unordered bucket. So '{{' or '(' cannot be changed into json
FacebookUsers: key id
FacebookMessages: key message-id
TwitterUsers: key screen-name
TweetMessages: key tweetid
'''


def L(a, b, c):
    filename = a+'.adm'
    file=open(filename,'r')
    outfile=open(a+'.json','w')
    outfile.write('[\n')
    line=file.readline()
    while line:
        line=line.replace('{{','[')
        line=line.replace('}}',']')
        line=line.replace('[{','{');
        line=line.replace('}]','}')
        while line.find('(\"')>=0:
            i=line.find('(\"')
            z=line.rfind(':',0,i)
            line=line.replace('(\"',' ',1)
            line=line.replace('\")','\"',1)
            line=line[0:z+1]+'\"'+line[z+1:]
        outfile.write(line)
        line=file.readline()
        if line:
            outfile.write(',')
    outfile.write(']')
    file.close()
    outfile.close()
    filename = a+'.json'
    data = json.load(open(str(filename)))
    for i in range(0, len(data)):
        key = data[i][c]
        outfile = open(b+'/' + str(key) + '.json', 'w')
        json.dump(data[i], outfile)
        outfile.close()
    return


L('fbm','FacebookMessages','message-id')

L('fbu','FacebookUsers','id')

L('twu','TwitterUsers','screen-name')

L('twm','TweetMessages','tweetid')
