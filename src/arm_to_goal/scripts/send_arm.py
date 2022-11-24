#!/usr/bin/env python3
 
# Author: Automatic Addison https://automaticaddison.com
# Description: Uses the ROS action lib to move a robotic arm to a goal location
 
from __future__ import print_function 
import rospy 
import actionlib 
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal 
from std_msgs.msg import Float64 
from trajectory_msgs.msg import JointTrajectoryPoint 
 
 
def move_robot_arm(joint_values):
  """
  ロボットアームを任意の関節角度に動かす関数
  :param: joint_values ロボットアームの関節の希望角度のリスト。
  """
  # SimpleActionClient を作成し、コンストラクタにアクションの型を渡します。
  arm_client = actionlib.SimpleActionClient('arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
 
  # サーバーが起動し、ゴールのリッスンを開始するのを待ちます。
  arm_client.wait_for_server()
     
  # Action Server に送信する新しいゴールを作成します。
  arm_goal = FollowJointTrajectoryGoal()
 
  # ロボットアームの各関節の名称を格納する
  arm_goal.trajectory.joint_names = ['arm_base_joint', 'shoulder_joint','bottom_wrist_joint' ,'elbow_joint', 'top_wrist_joint']
   
  # 軌跡点の作成   
  point = JointTrajectoryPoint()
 
  # 望みのジョイント値を格納する
  point.positions = joint_values
 
  # アームを目的の関節角度に動かすのに必要な時間を秒単位で設定します。
  point.time_from_start = rospy.Duration(3)
 
  # 望みのジョイント値をゴールに追加する
  arm_goal.trajectory.points.append(point)
 
  # タイムアウト値の定義
  exec_timeout = rospy.Duration(10)
  prmpt_timeout = rospy.Duration(5)
 
  # ActionServerにゴールを送り、サーバーがアクションの実行を終えるのを待つ
  arm_client.send_goal_and_wait(arm_goal, exec_timeout, prmpt_timeout)
 
 
if __name__ == '__main__':
  import sys

  try:
    rospy.init_node('send_goal_to_arm_py')
 
    # ロボットアームの関節をラジアン単位で希望の角度に動かす
    move_robot_arm([-0.1, 0.5, 0.02, 0, 0])
 
    print("Robotic arm has successfully reached the goal!")
     
  except rospy.ROSInterruptException:
    print("Program interrupted before completion.", file=sys.stderr)