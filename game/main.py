import pyxel
import logging as log
from pyxelunicode import PyxelUnicode

class App:
    def __init__(self):
        self.window_size_x = 256
        self.window_size_y = 224
        pyxel.init(self.window_size_x, self.window_size_y, title="sucaraction", fps=60)
        pyxel.cls(0)
        #Set PyxelUnicode
        self.font_path = "assets/misaki_gothic_2nd.ttf"
        self.font_size = 8
        self.font_size_2x = 16
        self.pyuni = PyxelUnicode(self.font_path, self.font_size)
        self.pyuni_2x = PyxelUnicode(self.font_path, self.font_size_2x)
        #Set logging
        log.basicConfig(format="%(asctime)s - %(levelname)s:%(name)s - %(message)s") #ログをファイルに保存する場合basicConfigにfilename="scaraction.log"を追加
        #System status
        self.error_num_list = []
        #Opening menu
        self.op_menu_1 = "Start"
        self.op_menu_2 = "Load"
        self.op_menu_3 = "Quit"
        self.menu_items = [self.op_menu_1, self.op_menu_2, self.op_menu_3]
        self.menu_selected_item = 0
        #Key input status
        self.key_right = False
        self.key_left = False
        self.key_up = False
        self.key_down = False
        #Player status
        self.px = 50.0
        self.py = 100.0
        self.player_x_speed = 1.5
        self.player_y_speed = 1.5
        self.check_move_x_right = False #Falseなら移動できる
        self.check_move_x_left = False
        self.check_move_y_up = False
        self.check_move_y_down = False
        #Map status
        self.is_game_start = False
        self.stage_flag = 1
        self.gravity = -1
        #Load
        pyxel.load("assets/my_resource.pyxres")
        self.wanderer_normal_list = [0, 18, 1, 28, 34, 3] #img, u, v, w幅, h高さ, colkey
        self.wanderer_hat_icon_list = [0, 0, 0, 17, 17, 7]

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        self.key_input()
        if self.is_game_start == False:
            #タイトル画面での操作を記述
            #爆速メニューになっちゃうからここはbtnpじゃないとダメ
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
                    pyxel.blt(self.BLT_X, self.BLT_Y+self.YI*i, *self.wanderer_hat_icon_list[:5], colkey=self.wanderer_hat_icon_list[5])
                else:
                    self.pyuni_2x.text(self.X, self.Y+self.YI*i, item, 13)
        else:
            #ゲーム本編での描画を実行
            self.main_draw()

    def main(self):
        #ゲーム本編での操作を記述
        #プレイヤー本体の操作
        self.check_move()
        if self.key_right and self.key_left:
            pass
        elif self.key_right and not self.check_move_x_right:
            self.px += self.player_x_speed
        elif self.key_left and not self.check_move_x_left:
            self.px -= self.player_x_speed
        if self.key_up and self.key_down:
            pass
        elif self.key_up and not self.check_move_y_up:
            self.py -= self.player_y_speed
        elif self.key_down and not self.check_move_y_down:
            self.py += self.player_y_speed
        #当たり判定縦
        #当たり判定横

    def main_draw(self):
        #ゲーム本編での描画を記述
        pyxel.cls(13)
        pyxel.blt(self.px, self.py, *self.wanderer_normal_list[:5], colkey=self.wanderer_normal_list[5])

    def key_input(self):
        self.key_right = pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)
        self.key_left = pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)
        self.key_up = pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_SPACE)
        self.key_down = pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_SHIFT)

    def handle_menu_selection(self):
        #opening menuでEnterを押した時の動作を記述
        self.menu_selected_item_text = self.menu_items[self.menu_selected_item]
        if self.menu_selected_item_text == self.op_menu_1:
            #はじめから
            self.is_game_start = True
        elif self.menu_selected_item_text == self.op_menu_2:
            #つづきから
            pass
        elif self.menu_selected_item_text == self.op_menu_3:
            pyxel.quit()
            #確認画面を表示してもいいかも

    def check_move(self):
        #とりあえず画面外へ行きそうなときTrueにする
        #x軸方向
        if self.px < 0:
            self.check_move_x_left = True
        else:
            self.check_move_x_left = False
        if self.px+self.wanderer_normal_list[3]+1 > self.window_size_x:
            self.check_move_x_right = True
        else:
            self.check_move_x_right = False
        #エラー処理(warning)
        if self.check_move_x_right and self.check_move_x_left:
            if "wM01" not in self.error_num_list:
                self.error_num_list.append("wM01")
            self.error()
        #y軸方向
        if self.py-1 < 0:
            self.check_move_y_up = True
        else:
            self.check_move_y_up = False
        if self.py+self.wanderer_normal_list[4]+1 > self.window_size_y:
            self.check_move_y_down = True
        else:
            self.check_move_y_down = False
        #エラー処理(warning)
        if self.check_move_y_up and self.check_move_y_down:
            if "wM02" not in self.error_num_list:
                self.error_num_list.append("wM02")
            self.error()
        #エラー処理(error)
        if self.check_move_x_right and self.check_move_x_left and self.check_move_y_up and self.check_move_y_down:
            if "eM03" not in self.error_num_list:
                self.error_num_list.append("eM03")
            self.error()

    def error(self):
        ###エラー発生時の処理###
        #リリース版(ダウンロード向け)の場合ログファイルを生成(方法は__init__のコメント参照)
        #エラーログ出力
        for self.error_num in self.error_num_list:
            if "c" in self.error_num:
                log.critical(self.error_num)
            elif "e" in self.error_num:
                log.error(self.error_num)
            elif "w" in self.error_num:
                log.warning(self.error_num)
            elif "i" in self.error_num:
                log.info(self.error_num)
            elif "d" in self.error_num:
                log.debug(self.error_num)
        #エラー画面の表示
        """
        エラー番号一覧
        none(要素なし):エラーなし
        <playerの動作関連はm>
        wM01:self.check_move_x_rightとself.check_move_x_leftが同時にTrueになっている
        wM02:self.check_move_y_upとself.check_move_y_downが同時にTrueになっている
        eM02:self.check_move_x_rightとself.check_move_x_leftとself.check_move_y_upとself.check_move_y_downが同時にTrueになっている
        """

App().run()