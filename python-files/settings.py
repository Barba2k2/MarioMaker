# general setup
TILE_SIZE = 64
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
ANIMATION_SPEED = 8

# editor graphics
EDITOR_DATA = {
	0: {'style': 'player', 'type': 'object', 'menu': None, 'menu_surf': None, 'preview': None, 'graphics': '../graphics/player/idle_right'},
	1: {'style': 'sky',    'type': 'object', 'menu': None, 'menu_surf': None, 'preview': None, 'graphics': None},
	
	2: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/land.png',  'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/land.png',  'graphics': None},
	3: {'style': 'water',   'type': 'tile', 'menu': 'terrain', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/water.png', 'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/water.png', 'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/terrain/water/animation'},
	
	4: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/gold.png',    'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/gold.png',    'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/items/gold'},
	5: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/silver.png',  'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/silver.png',  'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/items/silver'},
	6: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/diamond.png', 'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/diamond.png', 'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/items/diamond'},

	7:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/spikes.png',      'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/spikes.png',      'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/enemies/spikes'},
	8:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/tooth.png',       'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/tooth.png',       'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/enemies/tooth/idle'},
	9:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/shell_left.png',  'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/shell_left.png',  'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/enemies/shell_left/idle'},
	10: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/shell_right.png', 'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/shell_right.png', 'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/enemies/shell_right/idle'},
	
	11: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/small_fg.png', 'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/small_fg.png', 'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/terrain/palm/small_fg'},
	12: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/large_fg.png', 'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/large_fg.png', 'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/terrain/palm/large_fg'},
	13: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/left_fg.png',  'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/left_fg.png',  'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/terrain/palm/left_fg'},
	14: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/right_fg.png', 'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/right_fg.png', 'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/terrain/palm/right_fg'},

	15: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/small_bg.png', 'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/small_bg.png', 'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/terrain/palm/small_bg'},
	16: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/large_bg.png', 'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/large_bg.png', 'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/terrain/palm/large_bg'},
	17: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/left_bg.png',  'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/left_bg.png',  'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/terrain/palm/left_bg'},
	18: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': 'G:/Meu Drive/Pygame/MarioMaker/graphics/menu/right_bg.png', 'preview': 'G:/Meu Drive/Pygame/MarioMaker/graphics/preview/right_bg.png', 'graphics': 'G:/Meu Drive/Pygame/MarioMaker/graphics/terrain/palm/right_bg'},
}

NEIGHBOR_DIRECTIONS = {
	'A': (0,-1),
	'B': (1,-1),
	'C': (1,0),
	'D': (1,1),
	'E': (0,1),
	'F': (-1,1),
	'G': (-1,0),
	'H': (-1,-1)
}

LEVEL_LAYERS = {
	'clouds': 1,
	'ocean': 2,
	'bg': 3,
	'water': 4,
	'main': 5
}

# colors
SKY_COLOR = '#ddc6a1'
SEA_COLOR = '#92a9ce'
HORIZON_COLOR = '#f5f1de'
HORIZON_TOP_COLOR = '#d1aa9d'
LINE_COLOR = 'black'
BUTTON_BG_COLOR = '#33323d'
BUTTON_LINE_COLOR = '#f5f1de'