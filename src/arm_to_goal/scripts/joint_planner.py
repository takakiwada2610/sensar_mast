#!/usr/bin/env python
# coding: UTF-8
import sys
from math import pi

import moveit_commander
import rospy


def main():
    # MoveitCommanderの初期化
    moveit_commander.roscpp_initialize(sys.argv)

    # ノードの生成
    rospy.init_node("joint_planner")

    # MoveGroupCommanderの準備
    move_group = moveit_commander.MoveGroupCommander("arm")

    # 関節の角度でゴール状態を指定
    joint_goal = [0, 0.5, -0.5, -0.5,0.5]
    move_group.set_joint_value_target(joint_goal)

    # モーションプランの計画と実行
    move_group.go(wait=True)

    # 後処理
    move_group.stop()


if __name__ == "__main__":
    main()