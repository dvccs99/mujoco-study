import mujoco
import mujoco.viewer
import tyro
from dataclasses import dataclass


@dataclass
class Args:
    model_path: str = "mujoco_study/denso_test.xml"


args = tyro.cli(Args)
mujoco_model = mujoco.MjModel.from_xml_path(args.model_path)

data = mujoco.MjData(mujoco_model)
with mujoco.viewer.launch(mujoco_model) as viewer:
    while viewer.is_running():
        mujoco.mj_step(mujoco_model, data)
        viewer.sync()
