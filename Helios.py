import re

_MAX_BRIGHTNESS = 254
_HALF_BRIGHTNESS = 127
_FAST_TRANSITION = 1
_MEDIUM_TRANSITION = 15
_SLOW_TRANSITION = 30

_MAX_COLORTEMP_K = 6500
_MIN_COLORTEMP_K = 2000

_BRIDGE

#Color XY values for specific gamuts
_GAMUT_A = {'blue':[0.139,0.081], 'red':[0.7,0.2986], 'green':[0.214,0.709], 'yellow':[0.4432,0.5154], 'white':[0.3227,0.329]}
_GAMUT_B = {'blue':[0.168,0.041], 'red':[0.674,0.322], 'green':[0.408,0.517], 'yellow':[0.4317,0.4996] , 'white':[0.3227,0.329]}
_GAMUT_C = {'blue':[0.153,0.048], 'red':[0.692,0.308], 'green':[0.17,0.7], 'yellow':[0.4334,0.5022],  'white':[0.3227,0.329]}

WORDS = []

def isValid(text):
    return bool(re.search(r'\bCommand\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    if saturation:
	    bulbs = ask_for_group()
		mic.say("What would you like to set the saturation to?")
		saturation_level = int(mic.activeListen())
		set_saturation(bulbs, saturation_level)
	
	elif color:
	    bulbs = ask_for_group()
		mic.say("What would you like to set the color to?")
		color = mic.activeListen()
		gamut = get_gamut(profile['Gamut'])
		set_color(bulbs, color, gamut)
	
	elif brightness:
	    bulbs = ask_for_group()
		mic.say("What would you like to set the brightness to?")
		brightness_level = int(mic.activeListen())
		set_brightness(bulbs, brightness_level)
	
	elif hue:
	    bulbs = ask_for_group()
		mic.say("What would you like to set the hue to?")
		hue_level = int(mic.activeListen())
		set_hue(bulbs, hue_level)
	
	elif colortemp_k:
	    bulbs = ask_for_group()
		mic.say("What would you like to set the color temp to?")
		color_temp_k_level = int(mic.activeListen())
		set_colortemp_k(bulbs,colortemp_k)
		
		

def set_saturation(bulbs, saturation):
    for bulb in bulbs:
        bulb.saturation(saturation)

def set_color(bulbs, color, gamut):
    for bulb in bulbs
	    bulb.xy(gamut[color])

def set_brightness(bulbs, brightness):
    for bulb in bulbs:
        bulb.brightness(brightness)

def set_hue(bulbs, hue):
    for bulb in bulbs:
	    bulb.hue(hue)

def set_color_temp_k(bulbs, colortemp_k):
    if colortemp_k < _MIN_COLORTEMP_K:
	    colortemp_k = MIN_COLORTEMP_K
	if colortemp_k > _MAX_COLORTEMP_k:
	    colortemp_k = _MAX_COLORTEMP_K
	
	for bulb in bulbs:
	    bulb.colortemp_k(colortemp_k)

def ask_for_group(mic):
    mic.say("Which bulbs would you like to perform this action on?")
    bulb_group = mic.activeListen()
    if bulb_group != 'ALL':
        return get_bulbs_in_group(bulb_group)
	else:
	    return get_all_bulbs()
		
def get_all_bulbs():
    return bridge.get_light_objects('list')

def get_bulbs_in_group(group_name):
    bulb_names = bridge.get_light_objects('name')
	if group_name in bulb_names:
	    return bulb_names[group_name]
	else:
	    return []
		
def get_gamut(gamut_letter):
    if gamut_letter = 'A':
	    return _GAMUT_A
	elif gamut_letter = 'B':
	    return _GAMUT_B
	elif gamut_letter = 'C':
	    return _GAMUT_C
	
	