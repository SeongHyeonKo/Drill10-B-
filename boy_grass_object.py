from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self): 
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Ball:
    #random_number = random.randint(0, 1)

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.image0 = load_image('ball21x21.png')
        self.image1 = load_image('ball41x41.png')
        self.number = random.randint(0, 1)

    def update(self):
        self.y += 5

    def draw(self):
        if self.number == 0:
            self.image0.clip_draw(0, 0, 21, 21, self.x, self.y)
        else:
            self.image1.clip_draw(0, 0, 41, 41, self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# 초기화 코드 
def reset_world(): 
    global running
    global world

    running = True
    world = []

    # 땅 객체 생성
    global grass
    grass = Grass()
    world.append(grass)

    # global team
    team = [Boy() for i in range(11)]
    world += team

    # global ball 20 
    ball20 = [Ball() for i in range(20)]
    world += ball20

# 게임 루프 코드
def update_world():
    for o in world:
        o.update()

    #grass.update()
    #for boy in team:
     #   boy.update()

# 종료 코드
def render_world():
    clear_canvas()
    for o in world:
        o.draw()
   # grass.draw()
    #for boy in team:
     #   boy.draw()
    update_canvas()


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
