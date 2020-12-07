import random
from pico2d import *
import gfw
import gobj
from BehaviorTree import BehaviorTree, SelectorNode, LeafNode


class Boss_monster:
    ACTIONS = ['Dead', 'Idle', 'Walk']
    CHASE_DISTANCE_SQ = 250 ** 2
    IDLE_INTERVAL = 2.0
    images = {}
    FPS = 12
    count = 0
    finish = False
    cc = []

    # FCOUNT = 10
    def __init__(self):


        self.PAT_POSITIONS = [(0, 150),(1200, 250)]


        if len(Boss_monster.images) == 0:
            Boss_monster.load_all_images()


        self.pos = (random.randint(300, 1200), 250)


        self.delta = 0.1, 0.1
        # self.find_nearest_pos()
        self.char = 'sprites'
        self.images = Boss_monster.load_images(self.char)
        self.action = 'Idle'
        self.speed = random.randint(100, 150)
        self.fidx = 0
        self.time = 0
        self.ball = None
        # if gfw.world.count_at(gfw.layer.player) > 0:
        # self.player = gfw.world.object(gfw.layer.player, 0)

        self.patrol_order = -1
        self.build_behavior_tree()

    def find_nearest_pos(self):
        x, y = self.pos
        nearest_dsq = 1000000000
        index = 0
        nearest_index = 0
        for (px, py) in self.PAT_POSITIONS:
            dsq = (x - px) ** 2 + (y - py) ** 2
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
        x, y = self.pos
        self.speed = 100
        self.update_position()

        if self.ball != None:
            collides = gobj.collides_box(self, self.ball)

            if collides:
                gfw.world.remove(self.ball)
                self.ball = None
                Boss_monster.cc.append((x, y))

                if len(Boss_monster.cc) == 5:
                    self.action = 'Dead'
                    self.time = 0


        for (px, py) in self.PAT_POSITIONS:
            dsq = (px - x) ** 2 + (py - y) ** 2
            if dsq < Boss_monster.CHASE_DISTANCE_SQ ** 2:
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
        x, y = self.pos
        tx, ty = target
        dx, dy = tx - x, ty - y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0: return

        self.target = target
        self.delta = dx / distance, dy / distance


    def do_idle(self):
        if self.action != 'Idle':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Boss_monster.FPS)
        if self.time >= Boss_monster.IDLE_INTERVAL:
            self.action = 'Walk'
            return BehaviorTree.FAIL
        return BehaviorTree.SUCCESS

    def do_dead(self):
        if self.action != 'Dead':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Boss_monster.FPS)
        if self.fidx >= len(self.images['Dead']):
            self.remove()
            Boss_monster.finish = True

        return BehaviorTree.SUCCESS

    @staticmethod
    def load_all_images():
        Boss_monster.load_images('male')
        Boss_monster.load_images('female')
        # Boss_monster.font = gfw.font.load(gobj.RES_DIR + '/ENCR10B.TTF', 20)

    @staticmethod
    def load_images(char):
        if char in Boss_monster.images:
            return Boss_monster.images[char]

        images = {}
        count = 0
        file_fmt = '%s/walking_little_monster_sprites/%s/w_%d.png'
        for action in Boss_monster.ACTIONS:
            action_images = []
            n = 0
            while True:
                n += 1
                fn = file_fmt % (gobj.RES_DIR, char, n)
                if os.path.isfile(fn):
                    action_images.append(gfw.image.load(fn))
                else:
                    break
                count += 1
            images[action] = action_images
        Boss_monster.images[char] = images
        return images

    def update(self):
        if gfw.world.count_at(gfw.layer.ball) > 0:
            self.ball = gfw.world.object(gfw.layer.ball, 0)
        self.bt.run()

    def update_position(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * Boss_monster.FPS)

        x, y = self.pos
        dx, dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time


        done = False
        tx, ty = self.target
        if dx > 0 and x >= tx or dx < 0 and x <= tx:
            x = tx
            done = True
        if dy > 0 and y >= ty or y < 0 and y <= ty:
            y = ty
            done = True

        self.pos = x, y

        return done

    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        flip = 'h' if self.delta[0] < 0 else ''
        image.composite_draw(0, flip, *self.pos, image.w*2.5 , image.h*2.5)
        # x,y = self.pos
        # Boss_monster.font.draw(x-40, y+50, self.action + str(round(self.time * 100) / 100))

    def get_bb(self):
        x, y = self.pos
        return x - 40, y - 50, x + 40, y + 40

    def __getstate__(self):
        dict = self.__dict__.copy()
        del dict['images']
        # del dict['player']
        return dict

    def __setstate__(self, dict):
        # self.__init__()
        self.__dict__.update(dict)
        self.images = Boss_monster.load_images(self.char)

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
