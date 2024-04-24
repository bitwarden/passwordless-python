import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "passwordless_auth",
        url="http://localhost:5173",  # vite dev server port
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component("passwordless_auth", path=build_dir)


def passwordless_auth_component(key, data):
    component_value = _component_func(key=key, default=None, data=data)
    return component_value
