## Xarmの制御プログラム(Python)

### 実行環境
+ Ubuntu20.04LTS
+ ROS Noetic
+ Python3.8.10

※ ROS Noeticのインストールは[こちら](https://qiita.com/vivy/items/7f8d932350175e8c0858)から

※ xArmのパッケージインストール&セットアップは[こちら](https://github.com/hiroarkMani/xArm_manipulation)から



### 実行方法
1. ターミナルでGazeboとMoveIt!を立ち上げる

    ```
    roslaunch xarm_gazebo xarm6_beside_table.launch add_gripper:=true
    ```
  
    ```
    roslaunch xarm6_gripper_moveit_config xarm6_gripper_moveit_gazebo.launch
    ```

   
2. 別ターミナルを開き、Pythonプログラムを実行

     ```
     python3 [実行ファイル名(~.py)]
     ```
