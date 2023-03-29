# Rutils (ROS utils) 

このパッケージは、ROSのユーティリティです。
ROSスクリプトでないプログラムを、簡単にROSのサブスクライバやパブリッシャに仕立て直すことができるプログラムを作成します。



https://user-images.githubusercontent.com/129230448/228406595-3fc3f2df-c0d6-4c31-bab0-65b0ae3b8530.mov


## Installation
インストールは次のコマンドでできます。
なお、ROSで使用しているpythonのpipをご使用ください。
``` bash
pip install git+https://github.com/t2penguin/rutils.git
```


## Usage
使い方の例は次のとおりです。
まずはじめに、インストールしたrutilsを使うためのROSパッケージを作成します。
``` bash
cd ~/catkin_ws/src
catkin_create_pkg hello_pkg std_msgs rospy
mkdir hello_pkg/script
catkin build
```

次に、hello_pkg/scriptの中に、rutils/apps/keyboard2twist.pyをコピペします。
以下のような状態になります。
新しいプログラムの中でrutilsを使用する場合は、このkeyboard2twist.pyを参考にしてください。

``` bash
~/catkin_ws/src/hello_pkg/script
❯ ls
keyboard2twist.py
```

このままですと、rosrunでkeyboard2twist.pyを実行できないので権限を追加します。
``` bash
chmod +x keyboard2twist.py
```

最後に、次のように使用します。
- ターミナル1
``` bash
roslaunch jackal_gazebo empty_world.launch config:=front_laser
```

- ターミナル2
``` bash
rosrun hello_pkg keyboard2twist.py
```
このプログラムはCtrl + Cを長押しすると止まります。


## Contributing
1. ROSのサブスクライバとパブリッシャを作るためのclassをプログラムしました。
2. キーボード入力からtwistメッセージを作成するアプリケーションをプログラムしました。
