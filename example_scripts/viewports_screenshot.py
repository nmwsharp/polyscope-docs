"""
Demo / docs-screenshot script for multiple viewports.

A 2x2 grid of viewports, each showing a different view of the same object:
  top-left:     a mesh colored by a scalar field
  top-right:    a point cloud sampled from the mesh surface
  bottom-left:  the mesh edges as a curve network
  bottom-right: surface normals as a vector field
Navigation is shared, so all views move together.

usage: python viewports_screenshot.py [mesh_path] [--screenshot out.png] [--no-show]
"""

import argparse
import os

import igl
import numpy as np

import polyscope as ps

parser = argparse.ArgumentParser()
parser.add_argument("mesh", nargs="?", default=os.path.expanduser("~/mesh/nonmanifold/angle_gear_w_shaft_71380.ply"))
parser.add_argument("--screenshot", default=None, help="save a screenshot to this path")
parser.add_argument("--no-show", action="store_true", help="don't enter the interactive loop")
parser.add_argument("--n-points", type=int, default=20000)
parser.add_argument("--n-vectors", type=int, default=1500)
args = parser.parse_args()

# Load the mesh and build some data
V, F = igl.read_triangle_mesh(args.mesh)
E = igl.edges(F)
_, _, P = igl.random_points_on_mesh(args.n_points, V, F)  # (barycentric coords, face inds, positions)

# A few points on the surface, with the normal of the face they lie on
_, FI, P_vec = igl.random_points_on_mesh(args.n_vectors, V, F)
N = np.cross(V[F[FI, 1]] - V[F[FI, 0]], V[F[FI, 2]] - V[F[FI, 0]])
N /= np.linalg.norm(N, axis=1, keepdims=True) + 1e-12

# A simple scalar field that varies across the object: distance from a corner of the bounding box
bb_min, bb_max = V.min(axis=0), V.max(axis=0)
center, diag = 0.5 * (bb_min + bb_max), np.linalg.norm(bb_max - bb_min)
scalar = np.linalg.norm(V - bb_min, axis=1)

ps.init()
ps.set_ground_plane_mode("shadow_only")
ps.set_window_size(2400, 1400)  # a big window, so the fixed-size UI panel takes up less of each viewport

# Register the data, each structure will be shown in only one viewport
mesh = ps.register_surface_mesh("mesh", V, F)
mesh.add_scalar_quantity("distance", scalar, enabled=True, cmap="viridis")
cloud = ps.register_point_cloud("samples", P, radius=0.002, color=(0.25, 0.45, 0.85))
edges = ps.register_curve_network("edges", V, E, radius=0.0007, color=(0.2, 0.2, 0.25))
normals = ps.register_point_cloud("normals", P_vec, radius=0.0015, color=(0.6, 0.6, 0.6))
normals.add_vector_quantity("normal", N, enabled=True, length=0.03, radius=0.002, color=(0.9, 0.4, 0.2))

ps.create_viewport_grid(2, 2)  # 2 wide, 2 tall
ps.set_viewports_share_navigation(True)

for i, structure in enumerate([mesh, cloud, edges, normals]):
    structure.set_viewport_visibility_exclusive(i)

# An oblique view of the object (shared by all viewports)
cam_offset = diag * np.array([1.0, 0.3, 0.5]) * 1.45
cam_right = np.cross([0.0, 1.0, 0.0], cam_offset)
cam_right /= np.linalg.norm(cam_right)
shift = -0.1 * diag * cam_right  # slide the object right in the frame, to clear the UI panel overlaid on the left viewports
ps.set_vertical_fov_degrees(25)  # narrow fov + far camera: less perspective distortion
ps.look_at(center + cam_offset + shift, center + shift)

if args.screenshot:
    ps.screenshot(args.screenshot, transparent_bg=False, include_UI=True)
if not args.no_show:
    ps.show()
