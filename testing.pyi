def btn(id: int) -> bool: ...
def btnp(id: int, hold=-1, period=-1) -> bool: ...
def circ(x: int, y: int, radius: int, color: int): ...
def circb(x: int, y: int, radius: int, color: int): ...
def clip(x: int, y: int, width: int, height: int): ...
def cls(color=0): ...
def elli(x: int, y: int, a: int, b: int, color: int): ...
def ellib(x: int, y: int, a: int, b: int, color: int): ...
def exit(): ...
def fget(sprite_id: int, flag: int) -> bool: ...
def fset(sprite_id: int, flag: int, b: bool): ...
def font(text: str, x: int, y: int, chromakey: int, char_width=8, char_height=8, fixed=False, scale=1, alt=False) -> int: ...
def key(code=-1) -> bool: ...
def keyp(code=-1, hold=-1, period=-17) -> int: ...
def line(x0: int, y0: int, x1: int, y1: int, color: int): ...
def map(x=0, y=0, w=30, h=17, sx=0, sy=0, colorkey=-1, scale=1, remap=None): ...
def memcpy(dest: int, source: int, size: int): ...
def memset(dest: int, value: int, size: int): ...
def mget(x: int, y: int) -> int: ...
def mset(x: int, y: int, tile_id: int): ...
def mouse() -> tuple[int, int, bool, bool, bool, int, int]: ...
def music(track=-1, frame=-1, row=-1, loop=True, sustain=False, tempo=-1, speed=-1): ...
def peek(addr: int, bits=8) -> int: ...
def peek1(addr: int) -> int: ...
def peek2(addr: int) -> int: ...
def peek4(addr: int) -> int: ...
def pix(x: int, y: int, color: int=None) -> int | None: ...
def pmem(index: int, value: int=None) -> int: ...
def poke(addr: int, value: int, bits=8): ...
def poke1(addr: int, value: int): ...
def poke2(addr: int, value: int): ...
def poke4(addr: int, value: int): ...
def print(text, x=0, y=0, color=15, fixed=False, scale=1, alt=False): ...
def rect(x: int, y: int, w: int, h: int, color: int): ...
def rectb(x: int, y: int, w: int, h: int, color: int): ...
def reset(): ...
def sfx(id: int, note=-1, duration=-1, channel=0, volume=15, speed=0): ...
def spr(id: int, x: int, y: int, colorkey=-1, scale=1, flip=0, rotate=0, w=1, h=1): ...
def sync(mask=0, bank=0, tocart=False): ...
def ttri(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, u1: float, v1: float, u2: float, v2: float, u3: float, v3: float, texsrc=0, chromakey=-1, z1=0.0, z2=0.0, z3=0.0): ...
def time() -> int: ...
def trace(message, color=15): ...
def tri(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, color: int): ...
def trib(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, color: int): ...
def tstamp() -> int: ...
def vbank(bank: int=None) -> int: ...
