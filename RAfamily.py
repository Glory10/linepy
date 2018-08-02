from LINEPY import *
from akad.ttypes import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse

# Untuk Login Via Qr link 
#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#line.log("Timeline Token : " + str(line.tl.channelAccessToken))

# Untuk Login Via Email & password
#line = LINE('EMAIL', 'PASSWORD')
#line.log("Auth Token : " + str(line.authToken))
#line.log("Timeline Token : " + str(line.tl.channelAccessToken))

kingbii = LINE() 
kingbii.log("Auth Token : " + str(kingbii.authToken)) 
kingbii.log("Timeline Token : " + str(kingbii.tl.channelAccessToken)) 

assist1 = LINE() 
assist1.log("Auth Token : " + str(assist1.authToken)) 
assist1.log("Timeline Token : " + str(assist1.tl.channelAccessToken)) 

assist2 = LINE() 
assist2.log("Auth Token : " + str(assist2.authToken)) 
assist2.log("Timeline Token : " + str(assist2.tl.channelAccessToken)) 

assist3 = LINE() 
assist3.log("Auth Token : " + str(assist3.authToken)) 
assist3.log("Timeline Token : " + str(assist3.tl.channelAccessToken)) 

assist4 = LINE() 
assist4.log("Auth Token : " + str(assist4.authToken)) 
assist4.log("Timeline Token : " + str(assist4.tl.channelAccessToken))

kingbii = kingbii
oepoll = OEPoll(kingbii)
All = [assist1,assist2,assist3,assist4]
mid = kingbii.profile.mid
Amid = assist1.getProfile().mid
Bmid = assist2.getProfile().mid
Cmid = assist3.getProfile().mid
Dmid = assist4.getProfile().mid
RABots = [mid,Amid,Bmid,Cmid,Dmid]
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
    kingbii.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)


def bot(op):
    try:
        if op.type == 5:
            if Setmain["RAautoadd"] == True:
                ra = kingbii.getContact(op.param1)
                kingbii.findAndAddContactsByMid(ra.mid)
                kingbii.sendMessageWithMention(op.param1, op.param1,"Hai","\nsudah ku addback ya\n\n{}".format(str(Setmain["RAmessage"])))
                
        if op.type == 22:
            if mid in op.param3:
                if Setmain["RAautojoin"] == True:
                    cl.leaveRoom(op.param1)        
                
        if op.type == 13:
            if mid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = kingbii.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            cl.acceptGroupInvitation(op.param1)
                            ra = kingbii.getGroup(op.param1)
                            kingbii.sendText(op.param1,"Sorry jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            kingbii.leaveGroup(op.param1)
                        else:
                            kingbii.acceptGroupInvitation(op.param1)
                            ra = kingbii.getGroup(op.param1)
                            kingbii.sendMessageWithMention(op.param1, ra.creator.mid,"Haii","\nSalam Kenal yah :)")
                            
            if Amid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = assist1.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            assist1.acceptGroupInvitation(op.param1)
                            ra = assist1.getGroup(op.param1)
                            assist1.sendText(op.param1,"Sorry jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            assist1.leaveGroup(op.param1)
                        else:
                            assist1.acceptGroupInvitation(op.param1)
                            ra = assist1.getGroup(op.param1)
                            assist1.sendMessageWithMention(op.param1, ra.creator.mid,"Haii","\nSalam Kenal yah :)")
                            
            if Bmid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = assist2.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            assist2.acceptGroupInvitation(op.param1)
                            ra = assist2.getGroup(op.param1)
                            assist2.sendText(op.param1,"Sorry jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            assist2.leaveGroup(op.param1)
                        else:
                            assist2.acceptGroupInvitation(op.param1)
                            ra = assist2.getGroup(op.param1)
                            assist2.sendMessageWithMention(op.param1, ra.creator.mid,"Haii","\nSalam kenal yah :)")
                            
            if Cmid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = assist3.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            assist3.acceptGroupInvitation(op.param1)
                            ra = assist3.getGroup(op.param1)
                            assist3.sendText(op.param1,"Sorry jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            assist3.leaveGroup(op.param1)
                        else:
                            assist3.acceptGroupInvitation(op.param1)
                            ra = assist3.getGroup(op.param1)
                            assist3.sendMessageWithMention(op.param1, ra.creator.mid,"Haii","\nSalam Kenal yah :)")
                            
            if Dmid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = assist4.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            assist4.acceptGroupInvitation(op.param1)
                            ra = assist4.getGroup(op.param1)
                            assist4.sendText(op.param1,"Sorry jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            assist4.leaveGroup(op.param1)
                        else:
                            assist4.acceptGroupInvitation(op.param1)
                            ra = assist4.getGroup(op.param1)
                            assist4.sendMessageWithMention(op.param1, ra.creator.mid,"Haii","\nSalam Kenal yah :).")
                            
        if op.type == 46:
            if op.param2 in RABots:
                assist1.removeAllMessages()
                assist2.removeAllMessages()
                assist3.removeAllMessages()
                assist4.removeAllMessages() 
                
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            #receiver = msg.to
            #sender = msg._from
            if msg.toType == 2:
                if msg.contentType == 13:
                    if Setmain["RAautoscan"] == True:
                        msg.contentType = 0
                        kingbii.sendText(msg.to,msg.contentMetadata["mid"])
                        
                elif msg.contentType == 0:
                    if Setmain["RAautoread"] == True:
                        kingbii.sendChatChecked(msg.to, msg_id)
                        assist1.sendChatChecked(msg.to, msg_id)
                        assist2.sendChatChecked(msg.to, msg_id)
                        assist3.sendChatChecked(msg.to, msg_id)
                        assist4.sendChatChecked(msg.to, msg_id)
                    if text is None:    
                        return
                    else:
                        
            #---------------------- Start Command ------------------------#
                        
                        if text.lower() == "menu":
                            md = "🔰|RA|Family Version\n\n"
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
                            kingbii.sendText(msg.to, md)
                            
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
                            kingbii.sendText(msg.to, "%s " % (elapsed_time))
                            
                            start2 = time.time()
                            assist1.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start2
                            assist1.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start3 = time.time()
                            assist2.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start3
                            assist2.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start4 = time.time()
                            assist3.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start4
                            assist3.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start5 = time.time()
                            assist4.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start5
                            assist4.sendText(msg.to, "%s" % (elapsed_time))
                            
                        elif text.lower() == ".tagall":
                            group = cl.getGroup(msg.to)
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
                                kingbii.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                
                        elif text.lower() == ".restart":
                            if msg._from in RASelf:
                                kingbii.sendMessageWithMention(msg.to,msg._from,"","Tunggu Sebentar..")
                                python3 = sys.executable
                                os.execl(python3, python3, *sys.argv)
                                
                        elif text.lower() == ".removechat":
                            if msg._from in RASelf:
                                try:
                                    assist1.removeAllMessages(op.param2)
                                    assist2.removeAllMessages(op.param2)
                                    assist3.removeAllMessages(op.param2)
                                    assist4.removeAllMessages(op.param2)
                                    assist1.sendMessageWithMention(msg.to,msg._from,"","Sudah Di Bersihkan")
                                except:
                                    pass        
                            
                        elif text.lower() == ".asupkan":
                            if msg._from in RASelf:
                                G = kingbii.getGroup(msg.to)
                                ginfo = kingbii.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kingbii.updateGroup(G)
                                invsend = 0
                                Ticket = kingbii.reissueGroupTicket(msg.to)
                                assist1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                assist2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                assist3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                assist4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kingbii.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kingbii.updateGroup(G)
                                G.preventedJoinByTicket(G)
                                kingbii.updateGroup(G)
                        
                        elif text.lower() == ".crotkan":
                            if msg._from in RASelf:
                                ra = assist1.getGroup(msg.to)
                                assist1.sendMessageWithMention(msg.to,ra.creator.mid,"Haii bro","\nAku pamit dulu bye muach")
                                assist1.leaveGroup(msg.to)
                                assist2.sendMessageWithMention(msg.to,ra.creator.mid,"Haii bro","\nAku pamit dulu bye muach")
                                assist2.leaveGroup(msg.to)
                                assist3.sendMessageWithMention(msg.to,ra.creator.mid,"Haii bro","\nAku pamit dulu bye muach")
                                assist3.leaveGroup(msg.to)
                                assist4.sendMessageWithMention(msg.to,ra.creator.mid,"Haii bro","\nAku pamit dulu bye muach")
                                assist4.leaveGroup(msg.to)
                                
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
                                            assist1.sendMessageWithMention(msg.to,target,"Sorry Bro","Aku kick anda karna anda jelek makasih")
                                            klist = [assist1,assist2,assist3,assist4]
                                            kicker = random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                        except:
                                            pass        
                                
                        elif '/ti/g/' in msg.text.lower():
                            if msg._from in RASelf:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Setmain["RAautojoin"] == True:
                                        ra = kingbii.findGroupByTicket(ticket_id)
                                        kingbii.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        assist1.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        assist1.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        assist1.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        assist1.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        
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
