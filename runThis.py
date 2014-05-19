# BaconCodeJam MkII
# /u/BritishColour
# PyGame - Let's Keep this Clean

import pygame, random, time, math # Import Modules

pygame.init() # Initalise Pygame
pygame.mixer.init() # Initalise Mixer

SCREEN = (400,400) # Set Screen Dimentions (X,Y)
FPS = 30 # Set FPS Cap
TITLE = "/u/BritishColour | /r/BaconGameJam" # Set Title
DEBUG = False # Set Debug Mode - If True Show FPS, quit via ESC and hide menus
CLOCK = pygame.time.Clock() # Define the Clock - allows FPS limit

screen = pygame.display.set_mode(SCREEN) # Setup Display
pygame.display.set_caption(TITLE) # Set Window Caption

# Colour Scheme
RED    = 190,  70,  46 # Background
JUICE  = 183, 102,  49 # First
POPPY  = 239, 160,  68 # Second
SUN    = 232, 212, 161 # Third
SPOTS  =  63,  82, 158 # Foreground

imgBaconGameJam = pygame.image.load('assets/bacon.png') # Load BaconGameJam Logo

pygame.mixer.music.load('assets/background.wav') # Load Background Music

titlefont = pygame.font.Font('assets/font.otf', 30) # Load font (Raleway Regular)
font      = pygame.font.Font('assets/font.otf', 20) # Load font smaller

upDown=0;leftDown=0;downDown=0;rightDown=0

def Hexagon(Radius, SCREENX, SCREENY, Side=0):
    # Moar Crazy Math, returns co-ords for a single side of the Hexagon
    a = int(math.sin(math.radians(30)) * (Radius / math.sin(math.radians(60))))
    x = SCREENX / 2; y = SCREENY / 2; r = Radius
    if Side == 0: return [(x + r,y + a), (x + r,y - a), (x,y - 2 * a), (x - r,y - a), (x - r,y + a), (x,y + 2 * a)]
    if Side == 1: return [(x + r,y + a), (x + r,y - a)]
    if Side == 2: return [(x + r,y - a), (x,y - 2 * a)]
    if Side == 3: return [(x,y - 2 * a), (x - r,y - a)]
    if Side == 4: return [(x - r,y - a), (x - r,y + a)]
    if Side == 5: return [(x - r,y + a), (x,y + 2 * a)]
    if Side == 6: return [(x,y + 2 * a), (x + r,y + a)]

def Input(): # Returns a list of inputs
    global upDown, downDown, leftDown, rightDown
    INPUT = [] # Initalise INPUT
    for event in pygame.event.get(): # Get Inputs and Append List
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP): INPUT.append('up');upDown = True
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT): INPUT.append('left');leftDown = True
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN): INPUT.append('down');downDown = True
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT): INPUT.append('right');rightDown = True
        if event.type == pygame.KEYUP and (event.key == pygame.K_UP): upDown = False
        if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT): leftDown = False
        if event.type == pygame.KEYUP and (event.key == pygame.K_DOWN): downDown = False
        if event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT): rightDown = False
        if upDown: INPUT.append('up')
        if downDown: INPUT.append('down')
        if leftDown: INPUT.append('left')
        if rightDown: INPUT.append('right')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: INPUT.append('space')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: pygame.quit();quit()
        if event.type == pygame.QUIT: pygame.quit();quit()
    if INPUT == []: return [''] # Return a list if no inputs
    return INPUT

def Startup(time): # Show BaconJam Logo
    screen.fill(RED) # Fill Screen
    screen.blit(imgBaconGameJam, (SCREEN[0]/2 - 150,SCREEN[1]/2 - 270/2)) # Blit BGJ Logo
    pygame.display.flip() # Flip Buffers
    pygame.time.wait(time * 1000) # Wait for 'time' seconds

def Menu():
    screen.fill(RED) # Fill Screen
    pygame.draw.polygon(screen, JUICE,   Hexagon(160, SCREEN[0], SCREEN[1])) # Draw Hexagon GOLD
    pygame.draw.polygon(screen, POPPY,   Hexagon(140, SCREEN[0], SCREEN[1])) # Draw Hexagon MOSS
    pygame.draw.polygon(screen, SUN, Hexagon(120, SCREEN[0], SCREEN[1])) # Draw Hexagon CLOVER
    screen.blit(titlefont.render('POLYGON', 1, SPOTS), (SCREEN[0]/2 - titlefont.size('POLYGON')[0]/2, SCREEN[1]/2 - titlefont.size('POLYGON')[1]/2)) # Blit Title
    screen.blit(font.render('Press Space', 1, SPOTS), (SCREEN[0]/2-font.size('Press Space')[0]/2, SCREEN[1]/2-font.size('Press Space')[1]/2+30)) # Blit instructions
    pygame.display.flip() # Flip Buffer
    while True: # Wait for SPACE
        if 'space' in Input(): return

def Game():
    HexagonRadius = [300, 400, 500]
    HexagonColour = [RED, JUICE, POPPY]
    HexagonSides  = [[None, None, None, None, None, None, None], [None, None, None, None, None, None, None], [None, None, None, None, None, None, None]]
    
    for i in range(3):
        for j in range(7):
            HexagonSides[i][j] = random.randint(0,1)

    pos = 0
    posSide = 1
    score = 0
    
    pygame.mixer.music.play()
    
    while True:
        INPUT = Input() # Get list of Inputs
        for x in range(len(HexagonRadius)): # Animate BG Hexagons
            if HexagonRadius[x] > 0: HexagonRadius[x] -= 5 # Animate
            else:
                HexagonRadius[x] = 300 # Reset Hexagon
                for i in range(7): HexagonSides[x][i] = random.randint(0,1) # Genorate new lines
        
        c = HexagonSides[0]
        if c[0] and c[2] and c[3] and c[4] and c[5]: HexagonSides[0][3] = 0
        c = HexagonSides[1]
        if c[0] and c[2] and c[3] and c[4] and c[5]: HexagonSides[1][3] = 0
        c = HexagonSides[2]
        if c[0] and c[2] and c[3] and c[4] and c[5]: HexagonSides[2][3] = 0
        
        if 50 in HexagonRadius:# Increace Score if survived
            if HexagonRadius[0] == 50:
                if not HexagonSides[0][posSide]: score += 1
                else: return score
            if HexagonRadius[1] == 50:
                if not HexagonSides[1][posSide]: score += 1
                else: return score
            if HexagonRadius[2] == 50:
                if not HexagonSides[2][posSide]: score += 1
                else: return score
        
        if HexagonRadius[2] > HexagonRadius[1] > HexagonRadius[0]: # Render
            screen.fill(HexagonColour[0])
            pygame.draw.polygon(screen, HexagonColour[2], Hexagon(HexagonRadius[2], SCREEN[0], SCREEN[1]))
            pygame.draw.polygon(screen, HexagonColour[1], Hexagon(HexagonRadius[1], SCREEN[0], SCREEN[1]))
            pygame.draw.polygon(screen, HexagonColour[0], Hexagon(HexagonRadius[0], SCREEN[0], SCREEN[1]))
        
        if HexagonRadius[1] > HexagonRadius[0] > HexagonRadius[2]: # Background
            screen.fill(HexagonColour[2])
            pygame.draw.polygon(screen, HexagonColour[1], Hexagon(HexagonRadius[1], SCREEN[0], SCREEN[1]))
            pygame.draw.polygon(screen, HexagonColour[0], Hexagon(HexagonRadius[0], SCREEN[0], SCREEN[1]))
            pygame.draw.polygon(screen, HexagonColour[2], Hexagon(HexagonRadius[2], SCREEN[0], SCREEN[1]))
        
        if HexagonRadius[0] > HexagonRadius[2] > HexagonRadius[1]: # Hexagons
            screen.fill(HexagonColour[1])
            pygame.draw.polygon(screen, HexagonColour[0], Hexagon(HexagonRadius[0], SCREEN[0], SCREEN[1]))
            pygame.draw.polygon(screen, HexagonColour[2], Hexagon(HexagonRadius[2], SCREEN[0], SCREEN[1]))
            pygame.draw.polygon(screen, HexagonColour[1], Hexagon(HexagonRadius[1], SCREEN[0], SCREEN[1]))
        
        for i in range(3): # Draw the Obsticles
            for j in range(7):
                if HexagonSides[i][j]: pygame.draw.line(screen, SUN, Hexagon(HexagonRadius[i], SCREEN[0], SCREEN[1], j)[0], Hexagon(HexagonRadius[i], SCREEN[0], SCREEN[1], j)[1], 5)
        
        pygame.draw.polygon(screen, SPOTS, Hexagon(40, SCREEN[0], SCREEN[1])) # Draw Middle Island
        
        pygame.draw.arc(screen, SPOTS, (SCREEN[0]/2-115/2, SCREEN[1]/2-115/2, 115, 115), math.radians(pos), math.radians(pos + 10), 5) # Draw the player
        
        if DEBUG: pygame.draw.line(screen, SUN, Hexagon(40, SCREEN[0], SCREEN[1], posSide)[0], Hexagon(40, SCREEN[0], SCREEN[1], posSide)[1])
        
        if 20  <= pos < 80 : posSide = 2
        elif 80  <= pos < 140: posSide = 3
        elif 140 <= pos < 200: posSide = 4
        elif 200 <= pos < 260: posSide = 5
        elif 260 <= pos < 320: posSide = 6
        else: posSide = 1
        
        if ('left' in INPUT) or leftDown:
            if pos == 350: pos = 0
            else: pos += 10 # Handle Inputs
        if ('right' in INPUT) or rightDown:
            if pos == 0: pos = 360
            else: pos -= 10 # Handle Inputs
        
        screen.blit(font.render(str(score), 1, SUN), (SCREEN[0]/2-font.size(str(score))[0]/2, SCREEN[1]/2-font.size(str(score))[1]/2)) # Draw Score
        
        pygame.display.flip() # Flip Buffers
        
        CLOCK.tick(FPS) # Limit FPS

if not DEBUG: Startup(2)
while True:
    if not DEBUG: Menu()
    Game()
    pygame.mixer.music.stop()