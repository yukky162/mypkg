import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

rclpy.init()                     #rclpyの初期化（最初に1回）
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
pub = node.create_publisher(Int16, "countup", 10)   #パブリッシャ作成（型、トピック名、キュー長）
n = 0
def cb():               #タイマーで定期的に呼ばれるコールバック関数
    global n            #関数を抜けてもnがリセットされないようにしている
    msg = Int16()       #メッセージの「オブジェクト」
    msg.data = n        #msgの持つdataにnを入れる
    pub.publish(msg)    #pubの持つpublishでメッセージ送信（パブリッシュ）
    n += 1


def main():
    node.create_timer(0.5, cb)  #0.5秒ごとにcbを呼ぶタイマー
    rclpy.spin(node)
