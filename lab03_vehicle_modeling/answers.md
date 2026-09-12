# Lab 3 Answers

## Part 1 predictions

Record the predicted motion and signs of body-forward speed and vehicle yaw rate for each wheel-angular-velocity case.

Case 1: wl = 5 rad/s, wr = 5 rad/s. Velocity is positive. Time derivative of theta: 0. Predicted motion: straight forward motion without rotating.

Case 2: wl = 0 rad/s, wr = 5 rad/s. Velocity is positive. Time derivative of theta: positive. Predicted motion: foward counterclockwise curve (pivoting around left wheel).

Case 3: wl = -3 rad/s, wr = 3 rad/s. Velocity is zero. Time derivative of theta: positive. Predicted motion: counterclockwise in-place rotation w/ no translation.

Case 4: wl = 5 rad/s, wr = 4.8 rad/s. Velocity is positive. Time derivative of theta: negative. Predicted motion: gentle forward clockwise curve (towards the right) 

## Differential-drive validation

Summarize the final pose of each special case and explain any disagreement with your hand prediction.

Final Poses (T = 8.0s)
equal positive: x = 1.32 m, y = 0 m, theta = 0 rad
left wheel stationary: x = 0.0749 m, y = 0.1101 m, theta = 8.25 rad
equal and opposite: x = 0 m, y = 0 m, theta = 9.9 rad
slight mismatch: x = 1.2703 m, y = -0.211 m, theta = -0.33 rad

I had no major disagreements, as equal positive only moves forward in the +x direction, left wheel stationary moves counterclockwise while moving, equal and opposite rotates around the origin while x and y equal zero, and the slight mismatch case drifts into the negative y direction due to the yaw rate.

## Student motion-design challenge

Select one target. Before running the program, record the wheel-speed relationship or calculation you used. After running it, record the chosen values and resulting final pose.

| Motion target | Predicted wheel-speed relationship or calculation | Chosen $\omega_L$ [rad/s] | Chosen $\omega_R$ [rad/s] | Final $(x,y,\theta)$ | Target met? |
|---|---|---:|---:|---|---|

| selected target: 1 CCW in-place spin | For target theta = 2pi/8, thetadot = 2pi/8 = 0.7854 rad/s. Using wr = -wl = b*thetadot/(2r) = (0.16*0.7854)/(2*0.033) = 1.904 rad/s. Eqiual and opposite speeds give a pure roation. | -3.0 | 3.0 | (0,0,9.9) | Yes |

## TurtleBot visual checkpoint

Insert one screenshot showing TurtleBot during a commanded motion case and identify whether it shows straight motion, curved motion, or in-place rotation.

PLACEHOLDER

Record the `pose.pose.position.x` and `.y` values from `/odom` before and after the straight command. Briefly explain how this change relates to the pose integration in `differential_drive.py`.

Initial pose: position.x = 0.0000, position.y = 0.0000
Final pose: position.x = 1.3200, position.y = 0.0000

Explanation: The change in x represents the integral of the world-frame forward velocity over time, directly matching the Euler integration in differential_drive.py


## Bicycle-model observations

Record the body-forward speed and yaw rate produced by `wheel_speed_to_twist` for each case. Explain the effects of zero steering and increasing steering magnitude.

straight: w = 5, delta = 0, v = 1.5 m/s, thetadot = 0 rad/s
gentle_turn: w = 5, delta = 0.12, v = 1.5 m/s, thetadot = 0.065 rad/s
tighter_turn: w = 5, delta = 0.25, v = 1.5 m/s, thetadot = 0.137 rad/s

Effects: Zero steering (delta = 0) produces a yar rate of zero (thetadot = 0) which drives the vehicle straight ahead. For increased steering magnitude, the forward speed v = rw remains constant (1.5 m/s) becuase thw wheel speed is fixed, but the yaw rate increases with the steering angle in a non-linear way due to the tan(delta) geometry.

## Model comparison

Compare the inputs, motion capabilities, and limitations of ideal differential drive and the kinematic bicycle model.

Inputs: The differential drive accepts independent left and right angular velocities. The bicycle model accepts a driven wheel speed and front steering angle only.

Motion capabilities: Differential drive can rotate in place by setting wl = -wr, whereas the bicycle model cannot spin in place and requires translational velocity to turn.

Limitations: Differential drive is susceptible to wheel slip during turns and pivots. The bicycle model assumes zero side-slip on its wheels, but its constrained by the mechanical steering angle limits as to not "tip over."

## Engineering questions

Answer Questions 1–6 from the README. Use equations, units, plots, or table values where they support your explanation.

1. Equations in plain text:
   v = (v_R + v_L) / 2 = (r * omega_R + r * omega_L) / 2 = (r / 2) * (omega_R + omega_L)
   d_theta/dt = (v_R - v_L) / b = (r * omega_R - r * omega_L) / b = (r / b) * (omega_R - omega_L)

2. In-place rotation only occurs when the body's forward linear speed v = 0. Setting the equation equal to zero gives us that wl = -wr, so the wheels must rotate at equal speeds in opposite directions.

3. The bicycle model's eqwuation for yaw rate is (thetadot) = v/L * tan(delta). Becuase tan(delta) is non-linear, doubling delta does not double thetadot. For very small angles tan(delta) is about equal to delta, but as the delta increases, the yaw rate grows faster than delta.

4. The Euler integration assumes the vx, vy, and thetadot to remain constant across the step size dt. For curved motion, the vehicle's header changes continuously, which causes drift errors to occur especially with larger values of dt.

5. Ideal odometry assumes perfect wheel rolling with no slipping and exact measurements for wheel geometry. We know this is not the case in real life, however, due to wheel slip, unequal tire inflation/wear, roughness, etc. This leads to an accumulation of error over time.

6. For differential drive: the minimum turning radius Rmin = 0 m  as it can rotate in place. For the bicycle model: the minimum turning radius Rmin = L/tan(deltamax), as it is constrained by the physical steering angle deltamax.
