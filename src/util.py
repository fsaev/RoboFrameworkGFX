import enum
 


class box_states(enum.IntEnum):
    UNSOLVED = 0
    IN_PROGRESS = 1
    TIMEOUT = 2
    SOLVED = 3

def state_to_color(box_state):
    if(box_state == box_states.UNSOLVED):
        return (255, 0, 0) # RGB red
    elif(box_state == box_states.IN_PROGRESS):
        return (255, 161, 0) # RGB amber
    elif(box_state == box_states.TIMEOUT):
        return (255, 0, 0) # RGB red
    elif(box_state == box_states.SOLVED):
        return (0, 255, 0) # RGB green