from logging import getLogger, DEBUG, StreamHandler
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False
import numpy as np
import time

STAGE_SIZE = (20, 20)
INITIAL_LIFE_EXISTANCE = 0.3

def to_next(stage):
    next_stage = []
    
    for row in range(STAGE_SIZE[0]):
        next_stage_row = []
        
        for column in range(STAGE_SIZE[1]):
            above = stage[(row-1)%STAGE_SIZE[0]][column]
            right = stage[row][(column+1)%STAGE_SIZE[1]]
            below = stage[(row+1)%STAGE_SIZE[0]][column]
            left = stage[row][(column-1)%STAGE_SIZE[1]]
            neighborhoods = [above, right, below, left]
            
            if stage[row][column]==0 :
                next_stage_row.append(1) if sum(neighborhoods)==3 else next_stage_row.append(0)
            else:
                next_stage_row.append(0) if sum(neighborhoods)==1 or sum(neighborhoods)==4 else next_stage_row.append(1)
                
        next_stage.append(next_stage_row)
        
    return next_stage

def to_str(stage):
    str_stage = "".join(["".join(["■" if stage[row][column]==1 else "□" for row in range(STAGE_SIZE[0])])+"\n" for column in range(STAGE_SIZE[1])])
    return str_stage

next_stage = np.random.binomial(1, INITIAL_LIFE_EXISTANCE, STAGE_SIZE).tolist()
stage = None
while stage != next_stage:
    if stage!=None:
        print("\033["+str(STAGE_SIZE[0]+1)+"A",end="")
    stage = next_stage
    str_stage = to_str(stage)
    print(str_stage)
    next_stage = to_next(stage)
    time.sleep(1)