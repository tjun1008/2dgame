import random
from pico2d import *
import gfw
import gobj
from BehaviorTree import BehaviorTree, SelectorNode, LeafNode

class Monster2:

    ACTIONS = ['Attack', 'Dead', 'Idle', 'Walk']
    CHASE_DISTANCE_SQ = 250 ** 2
    IDLE_INTERVAL = 2.0
    images = {}
    FPS = 12
    Over = False
    # FCOUNT = 10
    def __init__(self):

        n = random.randint(0, 1)

        if n == 0:
            self.PAT_POSITIONS = [(0, 100), (256, 100)]
        else:
            self.PAT_POSITIONS = [(480, 356), (1200, 356)]

        print(n)

        if len(Monster2.images) == 0:
            Monster2.load_all_images()

        if n == 0:
            self.pos = (random.randint(100,256),100)
        else:
            self.pos = (random.randint(710,1200),356)



        self.delta = 0.1, 0.1
        # self.find_nearest_pos()
        self.char = random.choice(['male', 'female'])
        self.images = Monster2.load_images(self.char)
        self.action = 'Idle'
        self.speed = random.randint(100, 150)
        self.fidx = 0
        self.time = 0
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
            # print(':', index, (x,y), '-', (px, py), dsq)
            if nearest_dsq > dsq:
                nearest_dsq = dsq
                nearest_index = index
                # print('nearest:', index)
            index += 1
        self.patrol_order = nearest_index
        self.set_patrol_target()

    def set_patrol_target(self):
        if self.patrol_order < 0:
            self.find_nearest_pos()
            return BehaviorTree.SUCCESS
        self.set_target(self.PAT_POSITIONS[self.patrol_order])
        # print('pos=', self.pos, "patrol order = ", self.patrol_order, " target =", self.target)
        self.patrol_order = (self.patrol_order + 1) % len(self.PAT_POSITIONS)
        return BehaviorTree.SUCCESS

    def move_to_target(self):
        x,y = self.pos
        self.speed = 100
        self.update_position()

        if self.ball != None:
            collides = gobj.collides_box(self, self.ball)

            if collides:
                gfw.world.remove(self.ball)
                self.ball = None
                Monster2.cc.append((x,y))

                if len(Monster2.cc) ==1:
                    self.action = 'Dead'
                    self.time = 0
                else:
                    self.ball = None
                    for (a, b) in Monster2.cc:
                        if (a, b) != (x, y):
                            self.action = 'Dead'
                            self.time = 0
                print(Monster2.cc)

        collides = gobj.collides_box(self, self.player)
        if collides:
            #print("충돌")
            dead = self.player.decrease_life()
            if dead:
                Monster2.Over = True
                self.remove()

        if Monster2.Over == True:
            self.remove()

        for (px, py) in self.PAT_POSITIONS:
            dsq = (px-x)**2 + (py- y)**2
            if dsq < Monster2.CHASE_DISTANCE_SQ ** 2:
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
        # print(x,y, tx,ty, dx,dy, '/',distance, dx/distance, dy/distance, 'target=', self.target, ' delta=', self.delta)



    def do_idle(self):
        if self.action != 'Idle':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Monster2.FPS)
        if self.time >= Monster2.IDLE_INTERVAL:
            self.action = 'Walk'
            return BehaviorTree.FAIL
        return BehaviorTree.SUCCESS

    def do_dead(self):
        if self.action != 'Dead':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Monster2.FPS)

        if self.fidx >= len(self.images['Dead']):
            self.remove()



        return BehaviorTree.SUCCESS

    @staticmethod
    def load_all_images():
        Monster2.load_images('male')
        Monster2.load_images('female')
        # Monster2.font = gfw.font.load(gobj.RES_DIR + '/ENCR10B.TTF', 20)

    @staticmethod
    def load_images(char):
        if char in Monster2.images:
            return Monster2.images[char]

        images = {}
        count = 0
        file_fmt = '%s/Zombiefiles/%s/%s (%d).png'
        for action in Monster2.ACTIONS:
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
        Monster2.images[char] = images
        print('%d images loaded for %s' % (count, char))
        return images

    def update(self):
        if gfw.world.count_at(gfw.layer.ball) > 0:
            self.ball = gfw.world.object(gfw.layer.ball, 0)
        self.bt.run()

    def update_position(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * Monster2.FPS)

        x,y = self.pos
        dx,dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time

        # print(self.pos, self.delta, self.target, x, y, dx, dy)

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
        # Monster2.font.draw(x-40, y+50, self.action + str(round(self.time * 100) / 100))

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
        self.images = Monster2.load_images(self.char)

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
                    "name": "Move",
                    "class": LeafNode,
                    "function": self.move_to_target,
                },

            ],
        })
