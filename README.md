## Robot Package Template

This is a GitHub template. You can make your own copy by clicking the green "Use this template" button.

It is recommended that you keep the repo/package name the same, but if you do change it, ensure you do a "Find all" using your IDE (or the built-in GitHub IDE by hitting the `.` key) and rename all instances of `diff-drive-robot` to whatever your project's name is.

Note that each directory currently has at least one file in it to ensure that git tracks the files (and, consequently, that a fresh clone has direcctories present for CMake to find). These example files can be removed if required (and the directories can be removed if `CMakeLists.txt` is adjusted accordingly).

------------------ Building -----------------------
```
cd ~/dev_ws
colcon build --symlink-install
source install/setup.bash
```

------------------ Robot Chassis ----------------------------
* Open RVIZ to view bot
    * `rviz2 /path/to/config/.rviz`

* individaul run files for robot state publisher with sim time enabled (for gazebo)
    * `ros2 launch diff-drive-robot rsp.launch.py use_sim_time:=true`
    * `ros2 launch gazebo_ros gazebo.launch.py`
    * `ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity bot_name`
* Or, just run the launch file
    * `ros2 launch diff-drive-robot launch_sim.launch.py`