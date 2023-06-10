import pyxel
from pyxelunicode import PyxelUnicode

class App:
    def __init__(self):
        pyxel.init(256, 224, title="sucaraction", fps=60)
        pyxel.cls(0)
        #load PyxelUnicode
        self.font_path = "assets/misaki_gothic_2nd.ttf"
        self.font_size = 8
        self.pyuni = PyxelUnicode(self.font_path, self.font_size)
        #Opening menu
        self.op_menu_1 = "Start"
        self.op_menu_2 = "Load"
        self.op_menu_3 = "Quit"
        self.menu_items = [self.op_menu_1, self.op_menu_2, self.op_menu_3]
        self.menu_selected_item = 0
        #User status
        self.mx = 0.0
        self.my = 0.0
        #Map status
        self.is_game_start = False
        self.stage_flag = 1
        #load
        pyxel.load("assets/my_resource.pyxres")

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.is_game_start == False:
            #タイトル画面での操作を記述
            if pyxel.btnp(pyxel.KEY_S):
                self.menu_selected_item = (self.menu_selected_item + 1) % len(self.menu_items)
            elif pyxel.btnp(pyxel.KEY_W):
                self.menu_selected_item = (self.menu_selected_item - 1) % len(self.menu_items)
            elif pyxel.btnp(pyxel.KEY_RETURN):
                self.handle_menu_selection(self)
        else:
            #ゲーム本編での操作を実行
            self.game_main(self)

    def draw(self):
        #タイトル画面での描画を記述
        if self.is_game_start == False:
            pyxel.cls(1)
            pyxel.blt(28, 30, 0, 0, 32, 96, 16, colkey=1)
            #menu button
            for i, item in enumerate(self.menu_items):
                if i == self.menu_selected_item:
                    self.pyuni.text(120, 65+10*i, "<"+item+">")
                    pyxel.blt(94, 65+10*i, 0, 0, 0, 24, 24)#, colkey=0)
                else:
                    self.pyuni.text(120, 65+10*i, item, 13)
        else:
            #ゲーム本編での描画を実行
            self.game_main_draw(self)

    def game_main(self):
        #ゲーム本編での操作を記述
        1*1

    def game_main_draw(self):
        #ゲーム本編での描画を記述
        pyxel.cls(0)

    def handle_menu_selection(self):
        #opening menuでEnterを押した時の動作を記述
        self.menu_selected_item_text = self.menu_items[self.menu_selected_item]
        if self.menu_selected_item_text == self.op_menu_1:
            #はじめから
            self.is_game_start = True
        elif self.menu_selected_item_text == self.op_menu_2:
            #つづきから
            1*1
        elif self.menu_selected_item_text == self.op_menu_3:
            pyxel.quit()
            #確認画面を表示してもいいかも

App().run()