
# ba_meta require api 6
from __future__ import annotations
from typing import TYPE_CHECKING

import ba
import _ba
from ba._generated.enums import InputType

if TYPE_CHECKING:
    from typing import Union, Sequence


def flying(actor: ba.Actor):
    if actor.node.exists():
        actor.node.handlemessage(
          'impulse', actor.node.position[0], actor.node.position[1], actor.node.position[2],
          0.0, 0.0, 0.0, 200.0, 200.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def assignfly(args):
    foreground_act = _ba.get_foreground_host_activity()
    with ba.Context(foreground_act):
        try:
            if args == 'all':
                for player in foreground_act.players:
                    player.assigninput(InputType.JUMP_PRESS,
                                       ba.Call(flying, player.actor))
            else:
                pID = int(args)
                foreground_act.players[pID].assigninput(InputType.JUMP_PRESS,
                                                        ba.Call(flying, foreground_act.players[pID].actor))
        except Exception as e:
            print(e)


