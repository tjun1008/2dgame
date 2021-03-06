import random
from pico2d import *
import gfw
import gobj
from BehaviorTree import BehaviorTree, SelectorNode, LeafNode
from item import Item

class Monster:

    ACTIONS = ['Attack', 'Dead', 'Idle', 'Walk']
    CHASE_DISTANCE_SQ = 250 ** 2
    IDLE_INTERVAL = 2.0
    images = {}
    FPS = 12
    cc = []
    Over = False
    Items= False
    score =0
    # FCOUNT = 10
    def __init__(self):

        n = random.randint(0, 1)

        global wav_dead
        wav_dead = load_wav('image/monster_dead.wav')

        if n == 0:
            self.PAT_POSITIONS = [(480, 350), (960, 350)]
        else:
            self.PAT_POSITIONS = [(0, 100), (1200, 100)]



        if len(Monster.images) == 0:
            Monster.load_all_images()

        if n == 0:
            self.pos = (random.randint(480,960),350)
        else:
            self.pos = (random.randint(0,1100),100)



        self.delta = 0.1, 0.1
        # self.find_nearest_pos()
        self.char = random.choice(['male', 'female'])
        self.images = Monster.load_images(self.char)
        self.action = 'Idle'
        self.speed = random.randint(100, 150)
        self.fidx = 0
        self.time = 0
        #self.item = None
        self.ball = None
        if gfw.world.count_at(gfw.layer.player) > 0:
            self.player = gfw.world.object(gfw.layer.player, 0)


        self.patrol_order = -1
        self.build_behavior_tree()

    def find_nearest_pos(self):
        x, y = self.pos
        nearest_dsq = 1000000000
        index = 0
        nearest_index = 0
        for (px, py) in self.PAT_POSITIONS:
            dsq = (x-px)**2 + (y-py)**2

            if nearest_dsq > dsq:
                nearest_dsq = dsq
                nearest_index = index

            index += 1
        self.patrol_order = nearest_index
        self.set_patrol_target()

    def set_patrol_target(self):
        if self.patrol_order < 0:
            self.find_nearest_pos()
            return BehaviorTree.SUCCESS
        self.set_target(self.PAT_POSITIONS[self.patrol_order])

        self.patrol_order = (self.patrol_order + 1) % len(self.PAT_POSITIONS)
        return BehaviorTree.SUCCESS

    def move_to_target(self):
        x,y = self.pos
        self.speed = 100
        self.update_position()

        if self.ball != None:

            collides = gobj.collides_box(self, self.ball)

            if collides and gfw.world.count_at(gfw.layer.ball)>0:
                Monster.Items = True

                #gfw.world.remove(self.ball)
                #self.ball = None
                Monster.cc.append((x,y))

                if len(Monster.cc) ==1:
                    self.action = 'Dead'
                    self.time = 0
                else:
                    self.ball = None
                    for (a, b) in Monster.cc:
                        if (a, b) != (x, y):
                            self.action = 'Dead'
                            self.time = 0



        collides = gobj.collides_box(self, self.player)
        if collides:
            self.action = 'Dead'
            Monster.Items = False

            dead = self.player.decrease_life()
            if dead:
                Monster.Over = True
                self.remove()


        if Monster.Over == True:
            self.remove()



        for (px, py) in self.PAT_POSITIONS:
            dsq = (px-x)**2 + (py- y)**2
            if dsq < Monster.CHASE_DISTANCE_SQ ** 2:
                return BehaviorTree.SUCCESS
            else:
                return BehaviorTree.RUNNING

    def follow_patrol_positions(self):
        if self.patrol_order < 0:
            self.find_nearest_pos()
        done = self.update_position()
        if done:
            self.set_patrol_target()

    def get_next_position(self):
        self.target_x, self.target_y = self.patrol_positions[self.patrol_order % len(self.patrol_positions)]
        self.patrol_order += 1
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)
        return BehaviorTree.SUCCESS

    def set_target(self, target):
        x,y = self.pos
        tx,ty = target
        dx, dy = tx - x, ty - y
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0: return

        self.target = target
        self.delta = dx / distance, dy / distance




    def do_idle(self):
        if self.action != 'Idle':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Monster.FPS)
        if self.time >= Monster.IDLE_INTERVAL:
            self.action = 'Walk'
            return BehaviorTree.FAIL
        return BehaviorTree.SUCCESS

    def do_dead(self):
        global wav_dead
        x, y = self.pos
        if self.action != 'Dead':
            return BehaviorTree.FAIL
        else:
            gfw.world.remove(self.ball)


        self.time += gfw.delta_time
        self.fidx = round(self.time * Monster.FPS)

        if self.fidx >= len(self.images['Dead']):

            #1번
            wav_dead.play()
            self.remove()
            if Monster.Items == True:
                Monster.score += 10
                self.itemnum = random.randint(0, 2)


                self.item = Item(self.itemnum, x, y)
                gfw.world.add(gfw.layer.item, self.item)



            #return BehaviorTree.FAIL




    @staticmethod
    def load_all_images():
        Monster.load_images('male')
        Monster.load_images('female')
        # Monster.font = gfw.font.load(gobj.RES_DIR + '/ENCR10B.TTF', 20)

    @staticmethod
    def load_images(char):
        if char in Monster.images:
            return Monster.images[char]

        images = {}
        count = 0
        file_fmt = '%s/Zombiefiles/%s/%s (%d).png'
        for action in Monster.ACTIONS:
            action_images = []
            n = 0
            while True:
                n += 1
                fn = file_fmt % (gobj.RES_DIR, char, action, n)
                if os.path.isfile(fn):
                    action_images.append(gfw.image.load(fn))
                else:
                    break
                count += 1
            images[action] = action_images
        Monster.images[char] = images

        return images

    def update(self):
        global wav_item

        if gfw.world.count_at(gfw.layer.ball) > 0:
            self.ball = gfw.world.object(gfw.layer.ball, 0)

        #if gfw.world.count_at(gfw.layer.item) > 0:
            #self.item = gfw.world.object(gfw.layer.item, 0)

        self.bt.run()
        #if gfw.world.count_at(gfw.layer.item)>0:



        #좀비 다 죽으면 작동 안함







    def update_position(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * Monster.FPS)

        x,y = self.pos
        dx,dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time



        done = False
        tx,ty = self.target
        if dx > 0 and x >= tx or dx < 0 and x <= tx:
            x = tx
            done = True
        if dy > 0 and y >= ty or y < 0 and y <= ty:
            y = ty
            done = True

        self.pos = x,y

        return done

    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        flip = 'h' if self.delta[0] < 0 else ''
        image.composite_draw(0, flip, *self.pos, image.w // 5, image.h // 5)

        # x,y = self.pos
        # Monster.font.draw(x-40, y+50, self.action + str(round(self.time * 100) / 100))

    def get_bb(self):
        x,y = self.pos
        return x - 40, y - 50, x + 40, y + 40

    def __getstate__(self):
        dict = self.__dict__.copy()
        del dict['images']
        # del dict['player']
        return dict

    def __setstate__(self, dict):
        # self.__init__()
        self.__dict__.update(dict)
        self.images = Monster.load_images(self.char)

    def build_behavior_tree(self):
        # node_gnp = LeafNode("Get Next Position", self.set_patrol_target)
        # node_mtt = LeafNode("Move to Target", self.update_position)
        # patrol_node = SequenceNode("Patrol")
        # patrol_node.add_children(node_gnp, node_mtt)
        # self.bt = BehaviorTree(patrol_node)

        self.bt = BehaviorTree.build({
            "name": "PatrolChase",
            "class": SelectorNode,
            "children": [
                {
                    "class": LeafNode,
                    "name": "Idle",
                    "function": self.do_idle,
                },
                {
                    "class": LeafNode,
                    "name": "Dead",
                    "function": self.do_dead,
                },

                {
                    "class": LeafNode,
                    "name": "Follow Patrol positions",
                    "function": self.follow_patrol_positions,
                },

                {
                    "class": LeafNode,
                    "name": "Move",
                    "function": self.move_to_target,
                },

            ],
        })
