# Lab 3 Answers

## Part 1 predictions

Record the predicted motion and signs of body-forward speed and vehicle yaw rate for each wheel-angular-velocity case.

Case 1: wl = 5 rad/s, wr = 5 rad/s. Velocity is positive. Time derivative of theta: 0. Predicted motion: straight forward motion without rotating.

Case 2: wl = 0 rad/s, wr = 5 rad/s. Velocity is positive. Time derivative of theta: positive. Predicted motion: foward counterclockwise curve (pivoting around left wheel).

Case 3: wl = -3 rad/s, wr = 3 rad/s. Velocity is zero. Time derivative of theta: positive. Predicted motion: counterclockwise in-place rotation w/ no translation.

Case 4: wl = 5 rad/s, wr = 4.8 rad/s. Velocity is positive. Time derivative of theta: negative. Predicted motion: gentle forward clockwise curve (towards the right) 

## Differential-drive validation

Summarize the final pose of each special case and explain any disagreement with your hand prediction.

## Student motion-design challenge

Select one target. Before running the program, record the wheel-speed relationship or calculation you used. After running it, record the chosen values and resulting final pose.

| Motion target | Predicted wheel-speed relationship or calculation | Chosen $\omega_L$ [rad/s] | Chosen $\omega_R$ [rad/s] | Final $(x,y,\theta)$ | Target met? |
|---|---|---:|---:|---|---|
| selected target: | | | | | |

## TurtleBot visual checkpoint

Insert one screenshot showing TurtleBot during a commanded motion case and identify whether it shows straight motion, curved motion, or in-place rotation.

Record the `pose.pose.position.x` and `.y` values from `/odom` before and after the straight command. Briefly explain how this change relates to the pose integration in `differential_drive.py`.

## Bicycle-model observations

Record the body-forward speed and yaw rate produced by `wheel_speed_to_twist` for each case. Explain the effects of zero steering and increasing steering magnitude.

## Model comparison

Compare the inputs, motion capabilities, and limitations of ideal differential drive and the kinematic bicycle model.

## Engineering questions

Answer Questions 1–6 from the README. Use equations, units, plots, or table values where they support your explanation.
