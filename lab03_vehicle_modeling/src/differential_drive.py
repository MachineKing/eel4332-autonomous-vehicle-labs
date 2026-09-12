"""Starter code for Lab 3 differential-drive kinematics and odometry."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def _student_todo(description: str):
    """Mark one expression that students must replace in the starter code."""
    raise NotImplementedError(f"Replace this _student_todo expression: {description}")


@dataclass
class DifferentialDriveState:
    """Planar pose in meters and radians."""

    x: float
    y: float
    yaw: float


def wheel_speeds_to_twist(
    left_speed: float,
    right_speed: float,
    wheel_radius: float,
    track_width: float,
) -> tuple[float, float]:
    """Return body-forward speed and vehicle yaw rate from wheel angular velocities."""
    linear_speed = (wheel_radius / 2.0) * (right_speed + left_speed)
    yaw_rate = (wheel_radius / track_width) * (right_speed - left_speed)
    return linear_speed, yaw_rate


def step_differential_drive(
    state: DifferentialDriveState,
    left_speed: float,
    right_speed: float,
    wheel_radius: float,
    track_width: float,
    dt: float,
) -> DifferentialDriveState:
    """Advance wheel-odometry pose by one fixed Euler time step."""
    linear_speed, yaw_rate = wheel_speeds_to_twist(
        left_speed, right_speed, wheel_radius, track_width
    )
    x_rate = linear_speed * np.cos(state.yaw)
    y_rate = linear_speed * np.sin(state.yaw)

    new_x = state.x + x_rate * dt
    new_y = state.y + y_rate * dt
    new_yaw = state.yaw + yaw_rate * dt
    return DifferentialDriveState(x=new_x, y=new_y, yaw=new_yaw)


def simulate_differential_drive(
    initial_state: DifferentialDriveState,
    left_speed: float,
    right_speed: float,
    wheel_radius: float,
    track_width: float,
    dt: float,
    duration: float,
) -> np.ndarray:
    """Return an N x 3 array [x, y, yaw] for constant wheel speeds."""
    num_steps = int(round(duration / dt))
    trajectory = np.zeros((num_steps + 1, 3))
    trajectory[0] = [initial_state.x, initial_state.y, initial_state.yaw]

    state = initial_state
    for step_index in range(num_steps):
        state = step_differential_drive(
            state,
            left_speed,
            right_speed,
            wheel_radius,
            track_width,
            dt,
        )
        trajectory[step_index + 1] = [state.x, state.y, state.yaw]

    return trajectory
