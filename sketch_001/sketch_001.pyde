def setup():
    size(500,280)
    noStroke()
    fill(0)
    
def draw():
    background(204)
    if (mouseX < 50):
        fill(204, 166, 127)
        rect(0, 0, 50, 100)   # Left
    else:
        fill(216,185,152)
        rect(50, 0, 50, 100) #Right
        
        
    textSize(16)
    fill(0, 0, 0)
    text("corpo preto de alma", 10, 30)
    fill(178, 34, 34)
    textAlign(CENTER)
    text("rubra", 50, 50)
    fill(0,0,0)
    textAlign(LEFT)
    text("que nem a lava de um", 50, 70)
    fill(178, 34, 34)
    textAlign(LEFT)
    text("vulcao.", 70, 100)
    fill(0,0,0)
    textAlign(LEFT)
    text("me sinto", 105, 120)
    
    
    base = height * 0.75
    scalar = 0.8  # Different for each font
    textSize(32)  # Set initial text size
    a = textAscent() * scalar  # Calc ascent
    line(0, base - a, width, base - a)
    fill(255)
    text("e em erupcao", 225, base)  # Draw text on baseline
    textSize(20)
    fill(255)
    text("incompreendida", 0, base)  # Draw text on baseline
    textSize(64)  # Increase text size
    a = textAscent() * scalar  # Recalc ascent
    line(40, base - a, width, base - a)
    fill(126,57,47)
    text("sufocada", 40, base)  # Draw text on baseline
    
    # d_base = height * 1.5
    # textSize(32)
    # d = textDescent() * scalar
    # line(0, base + a, width, base + a)
    # fill(255)
    # text("db", 0, base)    

def keyPressed():
    if key == 's':
        saveFrame("cover_001-2.png")
