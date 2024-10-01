# Publisher and Subscriber 

The Pub-sub application of ROS is a simple workflow for industrial IoT.

This program is referred to following materials
- [Official tutorial instruction](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29)
- [Source code repo](https://github.com/ros/ros_tutorials)

### To change the publishing frequency

In this example, we only show the usage of the program `talker` and `listener`. 
The frequency of "talking" is in the **line 89** of `roscpp_tutorials/talker/talker.cpp`:

```
:
ros:Rate loop_rate(1000);
:
```

`1000` means Hz, so the delay between each message is 1/1000 second, 1 millisecond.
Anytime you change the program, you need to recompile/build the new docker image.

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

Simply run the YAML files under `./k8s`.
There are pairs of K8s configuration files for running the server-client model: `core_pub.yml` with `sub.yml`, 
and `core_sub.yml` with `pub.yml`.
These deployments indicate that either subscriber or publisher components running with core is supposed to 
run on the server side.
The difference lies in the message-passing direction: either from the server or to the server.


