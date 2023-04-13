from board import board
from solver import solver
# import pygame library
import pygame

# initialise the pygame
pygame.init()

# screen dimension
screen_width = 470
screen_height = 550

# Total window
screen = pygame.display.set_mode((screen_width,screen_height ))

# Title and Icon
pygame.display.set_caption("SUDOKU")
# img = pygame.image.load('icon.png')
# pygame.display.set_icon(img)


# sudoku dimension
sudoku_size = 450
screen_offset = 10
box_size = sudoku_size / 9


# Load test fonts for future use
font_large = pygame.font.SysFont("comicsans", 40)
font_small = pygame.font.SysFont("comicsans", 20)

# colours
box_bg = (0, 153, 153)
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_blue = (0,0,255)
color_green = (0,255,0)

KEYS_LIST = [
        [pygame.K_KP0,pygame.K_0],
        [pygame.K_KP1,pygame.K_1],
        [pygame.K_KP2,pygame.K_2],
        [pygame.K_KP3,pygame.K_3],
        [pygame.K_KP4,pygame.K_4],
        [pygame.K_KP5,pygame.K_5],
        [pygame.K_KP6,pygame.K_6],
        [pygame.K_KP7,pygame.K_7],
        [pygame.K_KP8,pygame.K_8],
        [pygame.K_KP9,pygame.K_9],
]

# initialize the board
board = board()

fps = 30
clock = pygame.time.Clock()

def solve(board):
    pos = board.get_empty()

    if not pos: return True

    for i in range(1,10):
        if board.check_valid(i,*pos):
            board.fill_cell(i,*pos)

            if solve(board):
                return True

            board.fill_cell(0,*pos)

    return False

def get_box_cord(pos):
    x = int( ( (pos[0] - screen_offset) // box_size) ) 
    y = int( ( (pos[1] - screen_offset) // box_size ) )
    return (x,y)

def get_cord(x,y):
    x = x* box_size + screen_offset + 2
    y = y* box_size + screen_offset + 2
    return (x,y)

# Highlight the hovered cell
def cell_hover(pos):
    if mouse_over_sudoku(pos):
        x,y = get_cord(*get_box_cord(pos))
        pygame.draw.rect(screen,box_bg,[x,y,box_size - 4,box_size - 4])

# Highlight the selected 
def highlight_selected(selected_x,selected_y):
    if (selected_x > -1  and selected_y > -1):
        x,y = get_cord(selected_x,selected_y)
        pygame.draw.rect(screen,box_bg,[x,y,box_size - 4,box_size - 4])

# Checks if mouse is over the board
def mouse_over_sudoku(pos):
    return (sudoku_size > pos[0] > screen_offset and sudoku_size > pos[1] > screen_offset)


# Fill gird with default numbers specified
def fill_defaults():
    for i,j in board.get_def_val():

        val = board.get_val(i,j)

        def_num = font_large.render(str(val), 1, color_black)
        screen.blit(def_num, ( i * box_size + 28,j * box_size + 23))

# Fill grids with entered value
def fill_entered():

    for i,j in board.get_used():
        val = board.get_val(i,j)

        if board.check_valid(val,i,j):
            temp_num = font_large.render(str(val), 1, color_green)
        else:
            temp_num = font_large.render(str(val), 1, color_blue)

        screen.blit(temp_num, ( i * box_size + 28,j * box_size + 23))

# Draw lines horizontally and verticallyto form grid
def draw_board():
    for i in range(10):
        if i % 3 == 0 :
           thick = 3
        else:
            thick = 1

        pygame.draw.line(screen, color_black, (screen_offset, i * box_size + screen_offset), 
                (sudoku_size + screen_offset , i * box_size + screen_offset) , thick)
        pygame.draw.line(screen, color_black, (i * box_size + screen_offset, screen_offset), 
                        (i * box_size + screen_offset, sudoku_size + screen_offset), thick)


# Fill value entered in cell	
def fill_val(val,x,y):
    board.fill_cell(val,x,y)


# Game specific variables
run = True

selected_x = -1
selected_y = -1

# The loop thats keep the window running
while run:

    # White color background
    screen.fill(color_white)

    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False

        # Get the mouse postion of selected
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_over_sudoku(pygame.mouse.get_pos()):
                selected_x , selected_y = get_box_cord(pygame.mouse.get_pos())
        
        # When key is pressed
        if event.type == pygame.KEYDOWN:

            # Direction keys
            if event.key == pygame.K_LEFT:
                if not( (selected_x <= 0) or (selected_x > 8) ):
                    selected_x -=1
            if event.key == pygame.K_RIGHT:
                if not( (selected_x < 0) or (selected_x > 7) ):
                    selected_x +=1
            if event.key == pygame.K_UP:
                if not( (selected_y <= 0) or (selected_y > 8) ):
                    selected_y -=1
            if event.key == pygame.K_DOWN:
                if not( (selected_y < 0) or (selected_y > 7) ):
                    selected_y +=1

            # if Enter key is pressed
            if event.key == pygame.K_RETURN:
                pass

            # If s pressed, solve the sudoku board
            if event.key == pygame.K_s:
                board.reset_board()
                solve(board)

            # If D is pressed reset the board to default
            if event.key == pygame.K_d:
                pass

            # Get the number to be inserted if key pressed
            if (selected_x > -1  and selected_y > -1):
                for i,sublist in enumerate(KEYS_LIST):
                    if event.key in sublist:
                        fill_val(i,selected_x,selected_y)

    # draws empty board
    draw_board()

    # Hovers the cell
    cell_hover(pygame.mouse.get_pos())
    
    # Highlights the cell selected
    highlight_selected(selected_x,selected_y)

    # Fill the values
    fill_entered()
    fill_defaults()

    # Update window
    pygame.display.update()

    # frames per second in loop
    clock.tick(fps)

# Quit pygame window	
pygame.quit()	

