add-apt-repository universe
add-apt-repository multiverse
add-apt-repository restricted
sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
apt update
apt install ros-noetic-ros-base
. /opt/ros/noetic/setup.bash
echo "echo 'ROSINSTALL'" >> ~/.bashrc
echo ". /opt/ros/noetic/setup.bash" >> ~/.bashrc
apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
apt install python3-rosdep
rosdep init
rosdep update
