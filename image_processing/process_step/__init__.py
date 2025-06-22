from .alpha_beta_enhance import AlphaBetaEnhance

# Available processes
from .image_load import ImageLoad
from .process_parameters import Parameter  # Exposed for typing purposes
from .sobel_gradient_interp import SobelGradientInterp
from .step_abc import ProcessStep
from .v_threshold import VThreshold

AVAILABLE_PROCESSES: list[ProcessStep] = [
    ImageLoad,
    VThreshold,
    SobelGradientInterp,
    AlphaBetaEnhance,
]


######## Sanity checks #########
if not all(issubclass(process, ProcessStep) for process in AVAILABLE_PROCESSES):
    raise TypeError(
        f"All processes must be subclasses of ProcessStep. Got {AVAILABLE_PROCESSES}.",
    )

if len(AVAILABLE_PROCESSES) != len(
    set(process.name for process in AVAILABLE_PROCESSES),
):
    raise ValueError("All processes must have a unique name.")

########## Constants derived from AVAILABLE_PROCESSES ##########

PROCESSES_NAME_TO_CLASSES_HASHMAP = {
    process.name: process for process in AVAILABLE_PROCESSES
}
