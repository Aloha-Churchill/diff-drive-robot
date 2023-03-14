# Autonomous Mobile Robot
This repo was originally cloned from Articulated Robotics. Lots of credit to that channel!
Example Commit

https://articulatedrobotics.xyz/

Highly based on Making a mobile robot.

## Building
The instructions below are assuming that `~/dev_ws` is the root folder and the package folder is `diff-drive-robot`.
```
cd ~/dev_ws
colcon build --symlink-install
source install/setup.bash
```
Including the flag `--symlink-install` will

## diff-drive-robot Package File Structure
```
+ config
    > depth_lidar_drive.rviz
        - 
    > drive_bot.rviz
    > empty.yaml
    > lidar_drive_bot.rviz
    > view_bot.rviz
+ description
    > camera.xacro
    > colors.xacro
    > depth_camera.xacro
    > gazebo_control.xacro
    > inertial_macros.xacro
    > lidar.xacro
    > robot_core.xacro
    > robot.urdf.xacro
    > tmp_core.xacro
+ launch
    > rsp.launch.py
    > test_sim.launch.py
+ models
    > model.config
    > model.sdf
+ worlds
    > empty.world
    > simple.world
```
## ROS Robot Archiecture
Some aspects of ROS architecture -> not complete yet

https://miro.com/app/board/uXjVPvQsJ5U=/?share_link_id=557058027414

## NAV2
Download and build from NAV2 website:https://navigation.ros.org/build_instructions/index.html


## Sensors
### RPLidar A1
Install driver on RPi
`sudo apt install ros-foxy-rplidar-ros`

Weird step: since sometimes /dev/ttyUSB0 doesn't showup upon restart, disable the braille settings with
`sudo systemctl mask brltty.path`

To find serial path:
```
cd /dev/serial/by-path
ls
```

To run lidar in ros
```
ros2 run rplidar_ros rplidar_composition --ros-args -p serial_port:=/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.2:1.0-port0 -p frame_id:=laser_frame -p angle_compensate:=true -p scan_mode:=Standard
```
To view lidar output in RVIZ
```
ros2 launch rplidar_ros view_rplidar.launch.py
```
RPLidar repository can be found here: https://github.com/allenh1/rplidar_ros.git

IMPORTANT: RPLidar S2 drivers are available here:
https://github.com/Slamtec/sllidar_ros2.git

### Luxonis OAK-D Depth Camera
Follow all instructions from https://github.com/luxonis/depthai-ros in the install from source sections until you hit the git clone command.

```
$ git clone --branch foxy https://github.com/luxonis/depthai-ros.git
$ cd ..
$ rosdep install --from-paths src --ignore-src -r -y
$ source /opt/ros/foxy/setup.bash
$ MAKEFLAGS="-j1 -l1" colcon build --executor sequential
$ source install/setup.bash
$ ros2 launch depthai_examples stereo_inertial_node.launch.py
$ ros2 launch depthai_examples rgb_publisher.launch.py
```

* Note: RVIZ is still not capturing image on this, but topics seem to be publishing

## Launch File Descriptions

* Open RVIZ to view bot
    * `rviz2 /path/to/config/.rviz`

* individaul run files for robot state publisher with sim time enabled (for gazebo)
    * `ros2 launch diff-drive-robot rsp.launch.py use_sim_time:=true`
    * `ros2 launch gazebo_ros gazebo.launch.py`
    * `ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity bot_name`
* Or, just run the launch file
    * `ros2 launch diff-drive-robot launch_sim.launch.py`

## ROS2 Installation
This project uses ROS2 foxy distribution. Installation instructions

https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html

* Note: on both RPi and Server install full desktop

## Raspberry Pi OS Installation
The raspberry pi is using the Ubuntu MATE 20.04 LTS 64 bit OS. 

Steps taken to install this:
- Because Ubuntu no longer has the images for MATE 20.04 for RPi this has to be done in a roundabout fasion
- Download RPi Imager
    - Other general purpose OS
    - Choose Ubuntu Server 20.04
- In Ubuntu Server
    - https://itsfoss.com/install-mate-desktop-ubuntu/
    - be sure to select MATE


## Server
- SSD Running Ubuntu 20.04 with ROS2 Foxy

## Networking
### Setup
On server
* make sure openssh server is installed

On Raspberry pi
* Make sure openssh server is installed
* Had to run below commands to start SSH
```
cd /dev/ssh
sudo ssh-keygen -A
sudo service ssh --full-restart
```
* Run `ip a` to get ip address

### General Connection
* Connect both raspberry pi and server to WANCO2 wifi network
    * TODO: make sure raspberry pi always connects to WANCO2 network
* SSH into raspberry pi from server
    * `ssh ubuntu@192.168.0.101`

## Gazebo Simulation
* To create a simulation gazebo environment, the building editor was used in an empty world and exported as a model. Then the world was saved into the `simple.world` file which was then reconfigured in `test_sim.launch.py`

## Running Gazebo Simulation + Controller
`ros2 launch diff-drive-robot test_sim.launch.py`
`ros2 run teleop_twist_keyboard teleop_twist_keyboard`

# Packages

Gazebo:

Controller:
`sudo apt install ros-foxy-ros2-control ros-foxy-ros2-controllers ros-foxy-gazebo-ros2-control`


