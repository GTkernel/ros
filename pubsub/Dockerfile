FROM ros:melodic

ARG PKG_DIR=/opt/ros/

RUN apt-get update && \
    apt-get install -y ros-melodic-catkin \
                       python-catkin-tools \
                       libboost-all-dev


RUN mkdir -p $PKG_DIR/src

COPY ./ $PKG_DIR/src

WORKDIR $PKG_DIR/src

RUN rosdep install -y --from-paths . --ignore-src --rosdistro melodic

WORKDIR $PKG_DIR
RUN catkin config --extend /opt/ros/${ROS_DISTRO} --cmake-args -DCMAKE_BUILD_TYPE=Release && \
    catkin build

RUN echo "source $PKG_DIR/devel/setup.bash" >> ~/.bashrc
