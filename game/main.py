import pyxel
from pyxelunicode import PyxelUnicode

class App:
    def __init__(self):
        pyxel.init(256, 224, title="sucaraction", fps=60)
        pyxel.cls(0)
        #load PyxelUnicode
        self.font_path = "assets/misaki_gothic_2nd.ttf"
        self.font_size = 8
        self.font_size_2x = 16
        self.pyuni = PyxelUnicode(self.font_path, self.font_size)
        self.pyuni_2x = PyxelUnicode(self.font_path, self.font_size_2x)
        #Opening menu
        self.op_menu_1 = "Start"
        self.op_menu_2 = "Load"
        self.op_menu_3 = "Quit"
        self.menu_items = [self.op_menu_1, self.op_menu_2, self.op_menu_3]
        self.menu_selected_item = 0
        #Player status
        self.px = 50.0
        self.py = 100.0
        #Map status
        self.is_game_start = False
        self.stage_flag = 1
        self.gravity = -1
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
                self.handle_menu_selection()
        else:
            #ゲーム本編での操作を実行
            self.main()

    def draw(self):
        #タイトル画面での描画を記述
        #ローカル変数定義
        self.X = 110
        self.BLT_X = self.X-21
        self.Y = 120
        self.YI = 20
        self.BLT_Y = self.Y-1
        #処理
        if self.is_game_start == False:
            pyxel.cls(1)
            #menu button
            for i, item in enumerate(self.menu_items):
                if i == self.menu_selected_item:
                    self.pyuni_2x.text(self.X, self.Y+self.YI*i, item)
                    pyxel.blt(self.BLT_X, self.BLT_Y+self.YI*i, 0, 0, 0, 17, 17, colkey=7)
                else:
                    self.pyuni_2x.text(self.X, self.Y+self.YI*i, item, 13)
        else:
            #ゲーム本編での描画を実行
            self.main_draw()

    def main(self):
        #ゲーム本編での操作を記述
        #プレイヤーの操作
        if pyxel.btn(pyxel.KEY_D or pyxel.KEY_RIGHT):
            self.px += 1.5
        elif pyxel.btn(pyxel.KEY_A or pyxel.KEY_LEFT):
            self.px -= 1.5
        if pyxel.btn(pyxel.KEY_SPACE or pyxel.KEY_UP):
            self.py -= 1.5
        elif pyxel.btn(pyxel.KEY_SHIFT or pyxel.KEY_DOWN):
            self.py += 1.5
        

    def main_draw(self):
        #ゲーム本編での描画を記述
        pyxel.cls(6)
        pyxel.blt(self.px, self.py, 0, 18, 0, 16, 16)

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