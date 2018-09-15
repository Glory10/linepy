from LINEPY import *
from akad.ttypes import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse

ra = LINE() 
ra.log("Auth Token : " + str(kingbii.authToken)) 
ra.log("Timeline Token : " + str(kingbii.tl.channelAccessToken)) 

ra = ra
oepoll = OEPoll(ra)
All = [ra]
mid = ra.profile.mid
RABots = [mid]
RASelf = ["Mid Kamu"]
RAFamily = RASelf + RABots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    ra.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)


def bot(op):
    try:
        if op.type == 5:
            if Setmain["RAautoadd"] == True:
                ra = ra.getContact(op.param1)
                ra.findAndAddContactsByMid(ra.mid)
                ra.sendMessageWithMention(op.param1, op.param1,"Hai","\nsudah ku addback ya\n\n{}".format(str(Setmain["RAmessage"])))
                
        if op.type == 22:
            if mid in op.param3:
                if Setmain["RAautojoin"] == True:
                    ra.leaveRoom(op.param1)        
                
        if op.type == 13:
            if mid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = kingbii.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            cl.acceptGroupInvitation(op.param1)
                            ra = ra.getGroup(op.param1)
                            ra.sendText(op.param1,"Sorry jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            ra.leaveGroup(op.param1)
                        else:
                            ra.acceptGroupInvitation(op.param1)
                            ra = ra.getGroup(op.param1)
                            ra.sendMessageWithMention(op.param1, ra.creator.mid,"Haii","\nSalam Kenal yah :)")
                            
                            
        if op.type == 46:
            if op.param2 in RABots:
                ra.removeAllMessages()
                
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            #receiver = msg.to
            #sender = msg._from
            if msg.toType == 2:
                if msg.contentType == 13:
                    if Setmain["RAautoscan"] == True:
                        msg.contentType = 0
                        ra.sendText(msg.to,msg.contentMetadata["mid"])
                        
                elif msg.contentType == 0:
                    if Setmain["RAautoread"] == True:
                        ra.sendChatChecked(msg.to, msg_id)
                    if text is None:    
                        return
                    else:
                        
            #---------------------- Start Command ------------------------#
                        
                        if text.lower() == "/help":
                            md = "🔰 |WR|PUBLIC BOT V1.0\n\n"
                            md += "🔰 .cek「@」\n"
                            md += "🔰 .gid\n"
                            md += "🔰 .yid\n"
                            md += "🔰 .me\n"
                            md += "🔰 .spbot\n"
                            md += "🔰 .tagall\n"
                            md += "🔰 .pengaturan\n"
                            md += "🔰 .restart\n"
                            md += "🔰 .removechat\n"
                            md += "🔰 .cekmid 「on/off」\n"
                            md += "🔰 .autoread 「on/off」\n"
                            md += "🔰 .asupkan\n"
                            md += "🔰 .crotkan\n"
                            md += "🔰 .kick「@」\n"
                            ra.sendText(msg.to, md)
                            
                        elif text.lower() == ".pengaturan":
                            if msg._from in RASelf:
                                md = "🔰|RA|Family Version\n\n"
                                if Setmain["RAautoscan"] == True: md+="✅ Cekmid\n"
                                else: md+="❎ Cekmid\n"
                                if Setmain["RAautoread"] == True: md+="✅ Autoread\n"
                                else: md+="❎ Autoread\n"
                                kingbii.sendText(msg.to, md)
                                
            #---------------------- On/Off Command -------------------# 
            
                        elif text.lower() == ".autoread on":
                            if msg._from in RASelf:
                                if Setmain["RAautoread"] == False:
                                    Setmain["RAautoread"] = True
                                    kingbii.sendMessageWithMention(msg.to,msg._from,"","Auto Read Di Aktifkan")
                                else:
                                    kingbii.sendMessageWithMention(msg.to,msg._from,"","Auto Read Sudah Aktif")
                                    
                        elif text.lower() == ".autoread off":
                            if msg._from in RASelf:
                                if Setmain["RAautoread"] == True:
                                    Setmain["RAautoread"] = False
                                    kingbii.sendMessageWithMention(msg.to,msg._from,"","Auto Read Di Matikan")
                                else:
                                    kingbii.sendMessageWithMention(msg.to,msg._from,"","Auto Read Sudah Di Matikan")
                                    
                        elif text.lower() == ".cekmid on":
                            if msg._from in RASelf:
                                if Setmain["RAautoscan"] == False:
                                    Setmain["RAautoscan"] = True
                                    kingbii.sendMessageWithMention(msg.to,msg._from,"","Cekmid diaktifkan")
                                else:
                                    kingbii.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".cekmid off":
                            if msg._from in RASelf:
                                if Setmain["RAautoscan"] == True:
                                    Setmain["RAautoscan"] = False
                                    kingbii.sendMessageWithMention(msg.to,msg._from,"","Cekmid dinonaktifkan")
                                else:
                                    kingbii.sendMessageWithMention(msg.to,msg._from,"","Sudah off")            
                            
            #---------------- Fungsi Command ------------------#
            
                        elif ".cek" in text.lower():
                            key = eval(msg.contentMetadata["MENTION"])
                            keys = key["MENTIONEES"][0]["M"]
                            ra = cl.getContact(keys)
                            try:
                                kingbii.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/{}".format(str(ra.pictureStatus)))
                                kingbii.sendMessageWithMention(msg.to,ra.mid,"[Nama]\n","\n\n[Bio]\n{}".format(str(ra.statusMessage)))
                            except:
                                pass
                            
                        elif text.lower() == ".gid":
                            kingbii.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                            kingbii.sendText(msg.to,msg.to)
                            
                        elif text.lower() == ".yid":
                            kingbii.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                            kingbii.sendText(msg.to,msg._from)
                        
                        elif text.lower() == ".me":
                            kingbii.sendMessageWithMention(msg.to,msg._from,"Hay","\nada apa?")
                            
                        elif text.lower() == ".spbot":
                            start = time.time()
                            kingbii.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start
                            ra.sendText(msg.to, "%s " % (elapsed_time))
                            
                        elif text.lower() == ".tagall":
                            group = ra.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Sange \n'
                                ra.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                
                        elif text.lower() == ".restart":
                            if msg._from in RASelf:
                                ra.sendMessageWithMention(msg.to,msg._from,"","Tunggu Sebentar..")
                                python3 = sys.executable
                                os.execl(python3, python3, *sys.argv)
                                
                        elif text.lower() == ".removechat":
                            if msg._from in RASelf:
                                try:
                                    ra.removeAllMessages(op.param2)
                                except:
                                    pass        
                                                    
                        elif text.lower() == ".crotkan":
                                ra = ra.getGroup(msg.to)
                                ra.leaveGroup(msg.to)
                                
                        elif ".kick" in text.lower():
                            if msg._from in RASelf:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in RAFamily:
                                        pass
                                    else:
                                        try:
                                            ra.sendMessageWithMention(msg.to,target,"Sorry Bro","Aku kick anda karna anda jelek makasih")
                                            klist = [ra]
                                            kicker = random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                        except:
                                            pass        
                                
                        elif '/ti/g/' in msg.text.lower():
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Setmain["RAautojoin"] == True:
                                        ra = ra.findGroupByTicket(ticket_id)
                                        ra.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        
                                    else:    
                                        assist1.sendMessageWithMention(msg.to,msg._from,"Kalau mau Auto Join","\naktifkan auotojoin dulu")

    except Exception as error:
        print (error)
        
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
        print(e)
