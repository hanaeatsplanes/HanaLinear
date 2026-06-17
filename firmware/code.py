print("starting!!!")
import board

from kmk.scanners import DiodeOrientation

row_pins = (board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6)
col_pins = (board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21) 
diode_orientation = DiodeOrientation.ROW2COL

# because i cant like. actually send fn. we're gonna replace fn with an emoji key. 
EMOJI = KC.MACRO(KC.LGUI(KC.LCTL(KC.SPC)))


keymap = [
[KC.ESC, KC.NO, KC.NO, KC.F3, KC.F4, KC.NO, KC.NO, KC.F7, KC.F8, KC.F9, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO],
[KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.NO, KC.BSPACE],
[KC.TAB, KC.NO, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH],
[KC.CAPS, KC.NO, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.NO, KC.ENTER],
[KC.NO, KC.LSHIFT, KC.NO, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.NO, KC.RSHIFT],
[EMOJI, KC.LCTRL, KC.LALT, KC.LGUI, KC.NO, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.NO, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT]
]
