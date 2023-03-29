# Rutils (ROS utils) 

このパッケージは、ROSのユーティリティです。
ROSスクリプトでないプログラムを、簡単にROSのサブスクライバやパブリッシャに仕立て直すことができるプログラムを作成します。


## Installation

``` bash
pip install git+https://github.com/t2penguin/rutils.git

catkin_create_pkg hello_pkg std_msgs rospy
mkdir hello_pkg/script
# スクリプトの作成

catkin build
```
