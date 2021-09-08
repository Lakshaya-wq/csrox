from requests import get
import re

BASE_URL = "https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.hpp"
OFFSET_NAMES = ['dwLocalPlayer', 'm_flFlashMaxAlpha', 'dwEntityList', 'm_iTeamNum', 'dwGlowObjectManager', 'm_iGlowIndex']
OFFSETS = {}

r = get(BASE_URL).text

def get_offsets():
    for i in OFFSET_NAMES:
        value = re.search(f"{i} = (.*?);", r).groups()[0]
        OFFSETS[i] = int(value, base=16)
    return OFFSETS