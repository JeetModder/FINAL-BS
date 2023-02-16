from .Handlers import handlemsg, handlemsg_all
import ba, _ba
from ba import _gameutils
import random
from ba import animate
from typing import TYPE_CHECKING
from tools import corelib
from bastd.actor.bomb import Bomb
from typing import Any, Sequence, Optional

Commands = ['fly', 'invisible', 'headless', 'creepy', 'celebrate', 'spaz', 'speed', 'floater',  '3dfly', 'hug', 'box', 'mine', 'egg', 'character', 'disco', 'reset']
CommandAliases = ['inv', 'hl', 'creep', 'celeb', 'flo', 'ch', 'ugly', 'dis', 'rst']




def ExcelCommand(command, arguments, clientid, accountid):
	"""
	Checks The Command And Run Function

	Parameters:
		command : str
		arguments : str
		clientid : int
		accountid : int

	Returns:
		None
	"""

	if command=='speed':
		speed(arguments)

	elif command == 'fly':
		fly(arguments)

	elif command in ['inv', 'invisible']:
		invi(arguments)

	elif command in ['hl', 'headless']:
		headless(arguments)

	elif command in ['creepy', 'creep']:
		creep(arguments)

	elif command in ['celebrate', 'celeb']:
		celeb(arguments)

	elif command == 'spaz':
		spaz(arguments)

	elif command in ['floater','flo']:
		floater(arguments,clientid)

	elif command == 'hug':
		hug(arguments)

	elif command == '3dfly':
		dfly(arguments)

	elif command in ['disco','dis']:
		disco(arguments)

	elif command in ['reset', 'rst']:
		reset(arguments)

	elif command == 'box':
		box(clientid, accountid, arguments)

	elif command == 'mine':
		mine(clientid, accountid, arguments)

	elif command == 'egg':
		egg(clientid, accountid, arguments)

	elif command in ['character', 'ch', 'ugly']:
		character(clientid, accountid, arguments)

def box(clientid,accountid,arguments):
    if arguments == [] or arguments == ['']:
        return


    elif arguments[0] == 'all':

        with ba.Context(_ba.get_foreground_host_activity()):
            for i in _ba.get_foreground_host_activity().players:
                try:
                    body = i.actor.node
                    if body.torso_model != ba.getmodel('tnt'):
                        body.head_model = None
                        body.torso_model = ba.getmodel('tnt')
                        body.color_texture = ba.gettexture('tnt')
                        body.style = 'cyborg'

                except:
                    pass


    else:

        player = int(arguments[0])
        with ba.Context(_ba.get_foreground_host_activity()):
            body = _ba.get_foreground_host_activity().players[
                player].actor.node
            if body.torso_model != ba.getmodel('tnt'):
                body.head_model = None
                body.torso_model = ba.getmodel('tnt')
                body.color_texture = ba.gettexture('tnt')
                body.style = 'cyborg'

def mine(clientid,accountid,arguments):
    if arguments == [] or arguments == ['']:
        return


    elif arguments[0] == 'all':

        with ba.Context(_ba.get_foreground_host_activity()):
            for i in _ba.get_foreground_host_activity().players:
                try:
                    body = i.actor.node
                    if body.torso_model != ba.getmodel('landMine'):
                        body.head_model = None
                        body.torso_model = ba.getmodel('landMine')
                        body.color_texture = ba.gettexture('landMine')
                        body.style = 'cyborg'

                except:
                    pass


    else:

        player = int(arguments[0])
        with ba.Context(_ba.get_foreground_host_activity()):
            body = _ba.get_foreground_host_activity().players[
                player].actor.node
            if body.torso_model != ba.getmodel('landMine'):
                body.head_model = None
                body.torso_model = ba.getmodel('landMine')
                body.color_texture = ba.gettexture('landMine')
                body.style = 'cyborg'

def egg(clientid,accountid,arguments):
    if arguments == [] or arguments == ['']:
        return


    elif arguments[0] == 'all':

        with ba.Context(_ba.get_foreground_host_activity()):
            for i in _ba.get_foreground_host_activity().players:
                try:
                    body = i.actor.node
                    if body.torso_model != ba.getmodel('egg'):
                        body.head_model = None
                        body.torso_model = ba.getmodel('egg')
                        body.color_texture = ba.gettexture('eggTex1')
                        body.style = 'cyborg'

                except:
                    pass


    else:

        player = int(arguments[0])
        with ba.Context(_ba.get_foreground_host_activity()):
            body = _ba.get_foreground_host_activity().players[
                player].actor.node
            if body.torso_model != ba.getmodel('egg'):
                body.head_model = None
                body.torso_model = ba.getmodel('egg')
                body.color_texture = ba.gettexture('eggTex1')
                body.style = 'cyborg'

def character(clientid,accountid,arguments):
    if arguments == [] or arguments == ['']:
        return


    elif arguments[0] == 'all':

        with ba.Context(_ba.get_foreground_host_activity()):
            for i in _ba.get_foreground_host_activity().players:
                try:
                    body = i.actor.node
                    torso = random.choice(['penguinTorso','santaTorso','bunnyTorso','aliTorso','cyborgTorso','neoSpazTorso','jackTorso','agentTorso','zoeTorso','ninjaTorso','bearTorso','bonesTorso','pixieTorso'])
                    head = random.choice(['penguinHead','santaHead','bunnyHead','aliHead','cyborgHead','neoSpazHead','jackHead','agentHead','zoeHead','ninjaHead','bearHead','bonesHead','pixieHead'])
                    if body.torso_model != ba.getmodel(torso):
                        body.head_model = ba.getmodel(head)
                        body.torso_model = ba.getmodel(torso)
                        body.color_texture = ba.gettexture(random.random()*2,random.random()*2,random.random()*2)
                        body.color_mask = ba.gettexture(random.random()*2,random.random()*2,random.random()*2)
                        body.style = 'cyborg'

                except:
                    pass


    else:

        player = int(arguments[0])
        with ba.Context(_ba.get_foreground_host_activity()):
            body = _ba.get_foreground_host_activity().players[
                player].actor.node
            torso = random.choice(['penguinTorso','santaTorso','bunnyTorso','aliTorso','cyborgTorso','neoSpazTorso','jackTorso','agentTorso','zoeTorso','ninjaTorso','bearTorso','bonesTorso','pixieTorso'])
            head = random.choice(['penguinHead','santaHead','bunnyHead','aliHead','cyborgHead','neoSpazHead','jackHead','agentHead','zoeHead','ninjaHead','bearHead','bonesHead','pixieHead'])
            if body.torso_model != ba.getmodel(torso):
                        body.head_model = ba.getmodel(head)
                        body.torso_model = ba.getmodel(torso)
                        body.color_texture = ba.gettexture(random.random()*2,random.random()*2,random.random()*2)
                        body.color_mask = ba.gettexture(random.random()*2,random.random()*2,random.random()*2)
                        body.style = 'cyborg'

def dfly(arguments):
	from .. import flycmd
	if arguments == []:
		return
	else:
		flycmd.assignfly(arguments[0])

def disco(arguments):
	from .. import discolight
	if arguments == []:
		return
	else:
		discolight.start()

def reset(arguments):
	from .. import discolight
	if arguments == []:
		return
	else:
		discolight.stop()

def hug(arguments):
	activity = _ba.get_foreground_host_activity()
	if arguments == [] or arguments == ['']:
		return
	if arguments[0] == 'all':
		try:
			activity.players[0].actor.node.hold_node = activity.players[1].actor.node
		except:
			pass
		try:
			activity.players[1].actor.node.hold_node = activity.players[2].actor.node
		except:
			pass
		try:
			activity.players[2].actor.node.hold_node = activity.players[3].actor.node
		except:
			pass
		try:
			activity.players[3].actor.node.hold_node = activity.players[4].actor.node
		except:
			pass
		try:
			activity.players[4].actor.node.hold_node = activity.players[5].actor.node
		except:
			pass
		try:
			activity.players[5].actor.node.hold_node = activity.players[6].actor.node
		except:
			pass
		try:
			activity.players[6].actor.node.hold_node = activity.players[7].actor.node
		except:
			pass
		try:
			activity.players[7].actor.node.hold_node = activity.players[8].actor.node
		except:
			pass
		try:
			activity.players[8].actor.node.hold_node = activity.players[9].actor.node
		except:
			pass
		try:
			activity.players[9].actor.node.hold_node = activity.players[10].actor.node
		except:
			pass
		try:
			activity.players[10].actor.node.hold_node = activity.players[11].actor.node
		except:
			pass
		try:
			activity.players[11].actor.node.hold_node = activity.players[12].actor.node
		except:
			pass
		try:
			activity.players[12].actor.node.hold_node = activity.players[13].actor.node
		except:
			pass
		try:
			activity.players[13].actor.node.hold_node = activity.players[14].actor.node
		except:
			pass
		try:
			activity.players[14].actor.node.hold_node = activity.players[15].actor.node
		except:
			pass
		try:
			activity.players[15].actor.node.hold_node = activity.players[0].actor.node
		except:
			pass
	else:
		try:
			activity.players[(arguments[0])].actor.node.hold_node = activity.players[(arguments[1])].actor.node
		except:
			pass

def floater(arguments,clientid):
	try:
		from .. import floater
		if arguments ==[]:
			floater.assignFloInputs(clientid)
		else:
			floater.assignFloInputs(arguments[0])
	except:
		pass

def speed(arguments):
	if arguments ==[] or arguments==['']:
		return
	else:
		corelib.set_speed(float(arguments[0]))


def fly(arguments):

	if arguments == [] or arguments == ['']:
		return


	elif arguments[0] == 'all':

		activity = _ba.get_foreground_host_activity()

		for players in activity.players:
			if players.actor.node.fly != True:
				players.actor.node.fly = True
			else:
				players.actor.node.fly = False

	else:
		try:

			activity = _ba.get_foreground_host_activity()
			player = int(arguments[0])

			if activity.players[player].actor.node.fly != True:
				activity.players[player].actor.node.fly = True
			else:
				activity.players[player].actor.node.fly = False

		except:
			return




def invi(arguments):

	if arguments == [] or arguments == ['']:
		return

	elif arguments[0] == 'all':

		activity = _ba.get_foreground_host_activity()

		for i in activity.players:
			if i.actor.exists() and i.actor.node.torso_model != None:
				body = i.actor.node
				body.head_model = None
				body.torso_model = None
				body.upper_arm_model = None
				body.forearm_model = None
				body.pelvis_model = None
				body.hand_model = None
				body.toes_model = None
				body.upper_leg_model = None
				body.lower_leg_model = None
				body.style = 'cyborg'
	else:

		player = int(arguments[0])
		activity = _ba.get_foreground_host_activity()

		body = activity.players[player].actor.node

		if body.torso_model != None:
			body.head_model = None
			body.torso_model = None
			body.upper_arm_model = None
			body.forearm_model = None
			body.pelvis_model = None
			body.hand_model = None
			body.toes_model = None
			body.upper_leg_model = None
			body.lower_leg_model = None
			body.style = 'cyborg'




def headless(arguments):

	if arguments == [] or arguments == ['']:
		return

	elif arguments[0] == 'all':

		activity = _ba.get_foreground_host_activity()

		for players in activity.players:

			node = players.actor.node
			if node.head_model != None:
				node.head_model = None
				node.style='cyborg'

	else:
		try:
			player = int(arguments[0])
			activity = _ba.get_foreground_host_activity()

			node = activity.players[player].actor.node

			if node.head_model != None:
				node.head_model = None
				node.style='cyborg'
		except:
			return



def creep(arguments):

	if arguments == [] or arguments == ['']:
		return

	elif arguments[0] == 'all':

		activity = _ba.get_foreground_host_activity()

		for players in activity.players:
			node = players.actor.node

			if node.head_model != None:
				node.head_model = None
				node.handlemessage(ba.PowerupMessage(poweruptype='punch'))
				node.handlemessage(ba.PowerupMessage(poweruptype='shield'))

	else:
		try:
			player = int(arguments[0])
			activity = _ba.get_foreground_host_activity()

			node = activity.players[player].actor.node

			if node.head_model != None:
				node.head_model = None
				node.handlemessage(ba.PowerupMessage(poweruptype='punch'))
				node.handlemessage(ba.PowerupMessage(poweruptype='shield'))
		except:
			return



def celeb(arguments):

	if arguments == [] or arguments == ['']:
		return

	elif arguments[0] == 'all':
		handlemsg_all(ba.CelebrateMessage())

	else:
		try:
			player = int(arguments[0])
			handlemsg(player, ba.CelebrateMessage())
		except:
			return


def spaz(arguments):
	if arguments == [] or arguments == ['']:
		return
	skin = str(arguments[1])
	try:
		if arguments[0] == "all":
			for players in _ba.get_foreground_host_activity().players:
				node = players.actor.node
				if node.head_model != None:
					node.color_mask_texture = _ba.gettexture(skin + "ColorMask")
					node.color_texture = _ba.gettexture(skin + "Color")
					node.hand_model = _ba.getmodel(skin + "Head")
					node.forearm_model = _ba.getmodel(skin + "Forearm")
					node.pelvis_model = _ba.getmodel(skin + "Pelvis")
					node.torso_model = _ba.getmodel(skin + "Torso")
					node.lower_leg_model = _ba.getmodel(skin + "LowerLeg")
					node.upper_arm_model = _ba.getmodel(skin + "UpperArm")
					node.upper_leg_model = _ba.getmodel(skin + "UpperLeg")
					node.toes_model = _ba.getmodel(skin + "Toes")
		else:
			player = int(arguments[0])
			node = _ba.get_foreground_host_activity().players[player].actor.node
			if node.head_model != None:
				node.color_mask_texture = _ba.gettexture(skin + "ColorMask")
				node.color_texture = _ba.gettexture(skin + "Color")
				node.hand_model = _ba.getmodel(skin + "Head")
				node.forearm_model = _ba.getmodel(skin + "Forearm")
				node.pelvis_model = _ba.getmodel(skin + "Pelvis")
				node.torso_model = _ba.getmodel(skin + "Torso")
				node.lower_leg_model = _ba.getmodel(skin + "LowerLeg")
				node.upper_arm_model = _ba.getmodel(skin + "UpperArm")
				node.upper_leg_model = _ba.getmodel(skin + "UpperLeg")
				node.toes_model = _ba.getmodel(skin + "Toes")
	except Exception as e:
		print(e)
		pass
