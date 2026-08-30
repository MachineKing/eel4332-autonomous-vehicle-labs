# Lab 1 Answers

## Recorded Measurements

1. Measured `/chatter` publication rate: 1.000 Hz

2. Measured `/practice/count` rate with `rate_hz:=5.0`: 5.000 Hz

3. Measured `/practice/count` rate with `rate_hz:=2.0`: 2.000 Hz

4. Original red-box pose: 0 0 1.5 0 0 0

5. Modified red-box pose: -1 0 1.5 0 0 0

6. Observation of simulation time while Gazebo was playing and paused: When Gazebo was playing, the /clock time kept ticking up (reaching sec: 5, nanosec: 29000000). As soon as I paused it, the clock froze completely (sec: 0, nanosec: 0), showing that simulation time only moves forward while the sim is active.

## Engineering Questions

1. In your own words, distinguish a ROS topic, service, action, and parameter. Give one appropriate use for each. A topic is a one-way, continuous stream of data, without the need of a listener, like a radio station. It is used in camera feeds and LiDAR scanners. A service is a one-on-one temporary handshake, where one node asks for something, gets it, and moves on. It is like an order at a drive-thru. It is used in spot requests, like triggering a hardware self-check. An action sends progress updates while working and lets you cancel halfway if necessary. It is like ordering a package online, where you can track it and cancel the order if you need to. It is used in navigation, ssuch as telling a robot to drive 50 feet away, and you can track it as it drives. A parameter is a settings variable that configures a node's behavior. It is like the volume buttons on a phone. It is used for setting safety variables, like a limit for maximum speed.

2. Why must a newly built workspace be sourced before `ros2 run` or `ros2 launch` can find its packages? When you compile new ROS2 code, Linux doesn't know where the new files are. Sourcing sets up the environment variables, so that Linux can find custom packages without errors.

3. What evidence showed that Gazebo Transport and the ROS graph are separate communication systems? When I ran gz topic -, I saw /clock. But when I ran the topics list in a separate terminal, /clock didn't show up at all. This means that Gazebo was running its own data using transport, isolated from ROS. The ROS graph only saw /clock after I launched ros_gz_bridge to bridge the gap.

4. What did the `/clock` bridge do? What happened on the ROS side when the bridge stopped? Gazebo generates its own simulation time, burt ROS 2 cannot read it directly, so the bridge translated it for ROS 2 so that the nodes could sync with simulation time. When you stop the bridge, Gazebo keeps running but the ROS 2 /clock topic stops outputting data.

5. Explain how the measured message rates changed when the launch argument changed. Changing the rate_hz launch argument directly changed the publisher's output frequency. Setting the hz rate to 5.0 set the node's timer to publish at 5.0 Hz, and changing it to 2.0 slowed the timer down to publish at 2.0 Hz.
