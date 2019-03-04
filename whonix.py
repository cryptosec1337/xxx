# coding: utf-8
# -*- coding: utf-8 -*-
import discord

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


    if message.content.lower().startswith("torgateway"):
        usageHELP = discord.Embed(

            title="Dedsec Project TOR Service",
            color=0x3A9AFA,
            description="RELOAD NETWORK: reloadtor\n"
                        "RESTART NETWORK: restartor\n"
                        "RELOAD FIREWALL: firewallreload\n"
                        "Project Coded by Crypto/Keyron.")

        await client.send_message(message.channel, embed=usageHELP)

    # reload firewall
    elif message.content.lower().startswith('/firewall'):
        import subprocess
        global data

        scriptreloadfirewall = message.content.lower()
        scriptreloadfirewall = scriptreloadfirewall.replace("/firewall", "whonix-reloadfirewall.desktop")

        #print(scriptreloadfirewall)

        #subprocess.Popen("sudo sh " + scriptreloadfirewall, stdout=subprocess.PIPE, shell=True)
        processFIREWALL = subprocess.Popen(
            "sudo sh " + scriptreloadfirewall,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        RELOADFIREWALLMSG = discord.Embed(
            title="Your Firewall Has Reloaded!",
            color=0xE62228,
            description="")

        await client.send_message(message.channel, embed=RELOADFIREWALLMSG)


    #reload tor
    elif message.content.lower().startswith('/reloadtor'):

        import subprocess

        global data

        scriptreloadTOR = message.content.lower()

        scriptreloadTOR = scriptreloadTOR.replace("/reloadtor", "gateway-reloadtor.desktop")

        # print(scriptreloadfirewall)

        #subprocess.Popen("sudo sh " + scriptreloadfirewall, stdout=subprocess.PIPE, shell=True)

        processtor = subprocess.Popen(
            "sudo sh " + scriptreloadTOR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )

        RELOADTORMSG = discord.Embed(

            title="Tor: Server Has Reloaded!",

            color=0xE62228,

            description="")

        await client.send_message(message.channel, embed=RELOADTORMSG)


    elif message.content.lower().startswith('/restartor'):

        import subprocess

        global data

        scriptrestartTOR = message.content.lower()

        scriptrestartTOR = scriptrestartTOR.replace("/restartor", "restart-tor-gui.desktop")

        # print(scriptreloadfirewall)

        # subprocess.Popen("sudo sh " + scriptreloadfirewall, stdout=subprocess.PIPE, shell=True)

        processrestarttor = subprocess.Popen(
            "sudo sh " + scriptrestartTOR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )

        RESTARTTORMSG = discord.Embed(

            title="Tor: Tor Gateway Has Restarted!",

            color=0xE62228,

            description="")

        await client.send_message(message.channel, embed=RESTARTTORMSG)







client.run('NDEyMjI5Mzc4NTEzMzA1NjAw.DrTtuA.u-0RNafh3E5xJCK--U2s9xsqT0Q')
