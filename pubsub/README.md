# Publisher and Subscriber 

The Pub-sub application of ROS is a simple workflow for industrial IoT.

This program is referred to following materials
- [Official tutorial instruction](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29)
- [Source code repo](https://github.com/ros/ros_tutorials)


## How to build

Simply build docker image with the Dockerfile here, you will get the whole `roscpp_tutorials` application packages
e.g.

```
$ docker build -t ros:pubsub .
```

This image can be used in all three components we required.

## How to run

### Through docker

Making sure your containers can communicate bi-directionally between each other, no matter through container networking or host networking.
And we should follow the ordering below:

Run ROS Core: 
```
$ docker run -d ros:pubsub source /opt/ros/devel/setup.bash && roscore
```

Run subscriber:
```
$ docker run -it ros:pubsub -e ROS_MASTER_URI='$ROS_CORE_IP:11311' -e ROS_IP='$ROS_SUB_IP' source /opt/ros/devel/setup.bash && rosrun roscpp_tutorials listener
```

Run publisher:
```
$ docker run -it ros:pubsub -e ROS_MASTER_URI='$ROS_CORE_IP:11311' -e ROS_IP='$ROS_PUB_IP' source /opt/ros/devel/setup.bash && rosrun roscpp_tutorials listener
```

### Through Kubernetes

Just run the YAML files under `./k8s`.

