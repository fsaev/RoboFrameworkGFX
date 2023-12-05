from util import box_states, state_to_color

def map(pygame, surface, matrix):
    return 1

def stage_boxes(pygame, surface, states):
    t = 12
    spacing = 20
    size = 344
    y_pos = surface.get_height()/2
    x_pos = 60
    # Initializing Color
    black = (0, 0, 0)

    font = pygame.font.SysFont('noto', 290)

    # Draw A
    selected_color = state_to_color(states[0])
    pygame.draw.rect(surface, selected_color, pygame.Rect(x_pos, y_pos, size, size)) # Draw outer
    pygame.draw.rect(surface, black, pygame.Rect(x_pos + t, y_pos + t, size - (t * 2), size - (t * 2))) # Draw inner

    text = font.render("A" , True, selected_color, black)
    textRect = text.get_rect(center=(x_pos + size/2, y_pos + size/2 + t))
    surface.blit(text, textRect)

    x_pos = x_pos + size + spacing
    # Draw B
    selected_color = state_to_color(states[1])
    pygame.draw.rect(surface, selected_color, pygame.Rect(x_pos, y_pos, size, size))
    pygame.draw.rect(surface, black, pygame.Rect(x_pos + t, y_pos + t, size - (t * 2), size - (t * 2))) # Draw inner

    text = font.render("B" , True, selected_color, black)
    textRect = text.get_rect(center=(x_pos + size/2, y_pos + size/2 + t))
    surface.blit(text, textRect)

    x_pos = x_pos + size + spacing
    # Draw C
    selected_color = state_to_color(states[2])
    pygame.draw.rect(surface, selected_color, pygame.Rect(x_pos, y_pos, size, size))
    pygame.draw.rect(surface, black, pygame.Rect(x_pos + t, y_pos + t, size - (t * 2), size - (t * 2))) # Draw inner

    text = font.render("C" , True, selected_color, black)
    textRect = text.get_rect(center=(x_pos + size/2, y_pos + size/2 + t))
    surface.blit(text, textRect)

    x_pos = x_pos + size + spacing
    # Draw D
    selected_color = state_to_color(states[3])
    pygame.draw.rect(surface, selected_color, pygame.Rect(x_pos, y_pos, size, size))
    pygame.draw.rect(surface, black, pygame.Rect(x_pos + t, y_pos + t, size - (t * 2), size - (t * 2))) # Draw inner

    text = font.render("D" , True, selected_color, black)
    textRect = text.get_rect(center=(x_pos + size/2, y_pos + size/2 + t))
    surface.blit(text, textRect)

    x_pos = x_pos + size + spacing

    # Draw E
    selected_color = state_to_color(states[4])
    pygame.draw.rect(surface, selected_color, pygame.Rect(x_pos, y_pos, size, size))
    pygame.draw.rect(surface, black, pygame.Rect(x_pos + t, y_pos + t, size - (t * 2), size - (t * 2))) # Draw inner

    text = font.render("E" , True, selected_color, black)
    textRect = text.get_rect(center=(x_pos + size/2, y_pos + size/2 + t))
    surface.blit(text, textRect)


def timer_line(pygame, surface, ts, end_ts):
    pct = 1 - ts/end_ts

    green = (0, 255, 0)
    red = (255, 0, 0)
    height_pos = 400
    line_length = surface.get_width() * pct
    pygame.draw.line(surface, red, (0, height_pos), (surface.get_width(), height_pos), 12)
    pygame.draw.line(surface, green, (0, height_pos), (surface.get_width() - line_length, height_pos), 12)

def timer_text(pygame, surface, ts, warning_minute):
    millis = int(ts)
    rem_millis = millis % 1000
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24

    # define the RGB value
    green = (0, 255, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)
    render_text = True

    if(ts/1000/60 < warning_minute): # Less than 5 minutes
        selected_color = red
        if(rem_millis < 500):
            render_text = False
        else:
            render_text = True
    else:
        selected_color = green

    font = pygame.font.SysFont('consolas', 180)

    text = font.render("%02d:%02d:%02d.%03d" % (hours, minutes, seconds, rem_millis) , True, selected_color, black)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect(center=(surface.get_width()/2, surface.get_height()/4))

    # set the center of the rectangular object.
    #textRect.center = (X // 2, Y // 2)
    if render_text:
        surface.blit(text, textRect)
    else:
        surface.fill(black, textRect)

def timer_decals(pygame, surface, ts, warning_minute):
    green = (0, 255, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)

    x_pos = surface.get_width()/100 * 85
    y_pos = surface.get_height()/4

    size = 80
    t = 12
    c_size = 30

    millis = int(ts)
    rem_millis = millis % 1000

    triangle = ((x_pos, y_pos + size/2), (x_pos + size, y_pos - size), (x_pos + size*2, y_pos + size/2))

    if(ts/1000/60 < warning_minute):
        if(rem_millis < 500):
            pygame.draw.polygon(surface, black, triangle, t)
            pygame.draw.line(surface, black, (x_pos + size, y_pos - size/2), (x_pos + size, y_pos), t)
            pygame.draw.line(surface, black, (x_pos + size, y_pos + (size/10) * 1), (x_pos + size, y_pos + (size/10) * 2), t)
        else:
            pygame.draw.polygon(surface, red, triangle, t)
            pygame.draw.line(surface, red, (x_pos + size, y_pos - size/2), (x_pos + size, y_pos), t)
            pygame.draw.line(surface, red, (x_pos + size, y_pos + (size/10) * 1), (x_pos + size, y_pos + (size/10) * 2), t)
    else:
        if(rem_millis < 500):
            pygame.draw.circle(surface, black, (x_pos, y_pos), c_size)
        else:
            pygame.draw.circle(surface, green, (x_pos, y_pos), c_size)