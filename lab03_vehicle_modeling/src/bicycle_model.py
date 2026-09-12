"""Starter code for the EEL 4332 kinematic bicycle model."""

from __future__ import annotations
from dataclasses import dataclass
import numpy as np


def _student_todo(description: str):
    """Mark one expression that students must replace in the starter code."""
    raise NotImplementedError(f"Replace this _student_todo expression: {description}")


@dataclass
class BicycleState:
    """Planar bicycle-model pose; x and y are in m and yaw is in rad."""

    x: float
    y: float
    yaw: float


def wheel_speed_to_twist(
    wheel_speed: float,
    wheel_radius: float,
    steering: float,
    wheelbase: float,
) -> tuple[float, float]:
    """Return body-forward speed and yaw rate for the bicycle model."""
    linear_speed = wheel_radius * wheel_speed
    yaw_rate = (linear_speed / wheelbase) * np.tan(steering)
    return linear_speed, yaw_rate


def step_bicycle(
    state: BicycleState,
    wheel_speed: float,
    wheel_radius: float,
    steering: float,
    wheelbase: float,
    dt: float,
) -> BicycleState:
    """Advance the planar kinematic bicycle model by one time step."""
    linear_speed, yaw_rate = wheel_speed_to_twist(
        wheel_speed, wheel_radius, steering, wheelbase
    )
    x_rate = linear_speed * np.cos(state.yaw)
    y_rate = linear_speed * np.sin(state.yaw)

    new_x = state.x + x_rate * dt
    new_y = state.y + y_rate * dt
    new_yaw = state.yaw + yaw_rate * dt
    return BicycleState(x=new_x, y=new_y, yaw=new_yaw)


def simulate(
    initial_state: BicycleState,
    wheel_speed: float,
    wheel_radius: float,
    steering: float,
    wheelbase: float,
    dt: float,
    duration: float,
) -> np.ndarray:
    """Return an N x 3 trajectory for a constant-input experiment."""
    num_steps = int(round(duration / dt))
    trajectory = np.zeros((num_steps + 1, 3))
    trajectory[0] = [initial_state.x, initial_state.y, initial_state.yaw]

    state = initial_state
    for step_index in range(num_steps):
        state = step_bicycle(
            state,
            wheel_speed,
            wheel_radius,
            steering,
            wheelbase,
            dt,
        )
        trajectory[step_index + 1] = [state.x, state.y, state.yaw]

    return trajectory
