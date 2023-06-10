import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="sucaraction", fps=60)
        #opening menu
        self.op_menu_1 = "Start"
        self.op_menu_2 = "Load"
        self.op_menu_3 = "Quit"
        self.menu_items = [self.op_menu_1, self.op_menu_2, self.op_menu_3]
        self.menu_selected_item = 0
        #Player status
        self.mx = 0.0
        self.my = 0.0
        #Map status
        self.game_start = False
        self.stage_flag = 1
        #read
        pyxel.load("my_resource.pyxres")

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_start == False:
            #タイトル画面での操作を記述
            if pyxel.btnp(pyxel.KEY_S):
                self.menu_selected_item = (self.menu_selected_item + 1) % len(self.menu_items)
            elif pyxel.btnp(pyxel.KEY_W):
                self.menu_selected_item = (self.menu_selected_item - 1) % len(self.menu_items)
            elif pyxel.btnp(pyxel.KEY_RETURN):
                self.handle_menu_selection()
        else:
            #ゲーム本編での操作を記述
            self.game_base()

    def game_base():
        #ゲーム本編での操作を記述
        1*1


    def draw(self):
        #ゲーム本編での描画を記述
        pyxel.cls(0)
        #タイトル画面での描画を記述
        if self.game_start == False:
            pyxel.cls(1)
            pyxel.blt(28, 30, 0, 0, 32, 96, 16, colkey=1)
            #menu button
            for i, item in enumerate(self.menu_items):
                if i == self.menu_selected_item:
                    pyxel.text(58, 65+10*i, "<"+item+">", 7)
                else:
                    pyxel.text(58, 65+10*i, item, 13)

    def handle_menu_selection(self):
        #opening menuでEnterを推した時の動作を記述
        self.menu_selected_item_text = self.menu_items[self.menu_selected_item]
        if self.menu_selected_item_text == self.op_menu_1:
            #はじめから
            self.game_start = True
        elif self.menu_selected_item_text == self.op_menu_2:
            #つづきから
            1*1
        elif self.menu_selected_item_text == self.op_menu_3:
            pyxel.quit()
            #確認画面を表示してもいいかも


App().run()