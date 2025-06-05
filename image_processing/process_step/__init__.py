from .step_abc import ProcessStep

from .process_parameters import Parameter  # Exposed for typing purposes

# Available processes
from .image_load import ImageLoad
from .v_threshold import VThreshold
from .sobel_gradient_interp import SobelGradientInterp
from .alpha_beta_enhance import AlphaBetaEnhance

AVAILABLE_PROCESSES: list[ProcessStep] = [
    ImageLoad,
    VThreshold,
    SobelGradientInterp,
    AlphaBetaEnhance,
]


######## Sanity checks #########
if not all(issubclass(process, ProcessStep) for process in AVAILABLE_PROCESSES):
    raise TypeError(
        "All processes must be subclasses of ProcessStep. "
        f"Got {AVAILABLE_PROCESSES}."
    )

if len(AVAILABLE_PROCESSES) != len(
    set(process.name for process in AVAILABLE_PROCESSES)
):
    raise ValueError("All processes must have a unique name.")

########## Constants derived from AVAILABLE_PROCESSES ##########

PROCESSES_NAME_TO_CLASSES_HASHMAP = {
    process.name: process for process in AVAILABLE_PROCESSES
}
